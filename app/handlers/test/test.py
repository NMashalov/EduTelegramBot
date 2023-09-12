from aiogram import Router, F
from aiogram.types import Message, PollAnswer

from app.keyboard import make_row_keyboard
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
from .test_examples import exmaples
from random import choice


class Test(StatesGroup):
    first_question = State()
    question = State()
    results = State()

router = Router(name='test')

@router.test


@router.message(
    Task.choose_task_type, 
    F.text == 'Test'
)
async def food_chosen(message: Message, state: FSMContext):
    await state.update_data(chosen_task=message.text.lower())
    await message.answer(
        text="Начинаем тест"
    )
    await state.set_state(Test.first_question)



@router.message(
   Test.first_question  
)
async def handle_first_question(message: Message, bot,state: FSMContext):

    example = choice(exmaples)
    print(example)

    await bot.send_poll(message.chat.id, example['Question'], example['Answers'], type='quiz', correct_option_id=example['Right_answer'], is_anonymous=False)

    await state.update_data(question_number=1,right_answers=0,correct_option=example['Right_answer'])
    await state.set_state(Test.question)

@router.poll_answer(
   Test.question     
)
async def handle_poll_answer(quiz_answer: PollAnswer, bot,state: FSMContext):
    # проверяем ответ

    state_info = await state.get_data()

    if state_info['correct_option'] == quiz_answer.option_ids[0]:
        await bot.send_message(quiz_answer.user.id,'Правильно! Идём дальше')
        right_answer= 1
    else:
        await bot.send_message(quiz_answer.user.id,'Жаль, но это неправильный ответ. Двигаемся дальше - может потом повезёт')
        right_answer= 0

    await state.update_data(right_answers=state_info['right_answers']+right_answer)    

    # заканчиваем тест, если число вопросов больше 5 
    if state_info['question_number'] >= 5:
        await state.set_state(Test.results)
    # отправляем следующую викторину
    else:
        example = choice(exmaples)
        print(example)
        await bot.send_poll(quiz_answer.user.id, example['Question'],  example['Answers'], type='quiz', correct_option_id=example['Right_answer'], is_anonymous=False)
        await state.update_data(question_number=state_info['question_number']+1,correct_option=example['Right_answer'])


@router.message(
   Test.results   
)
async def print_results(message: Message, state: FSMContext):

    state_info = await state.get_data()

    await message.answer(
        text=f"Правильно ответил {state_info['right_answers']}",
    )
    await state.clear()


