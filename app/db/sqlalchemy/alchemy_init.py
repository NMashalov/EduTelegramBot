from homework import homework_Base
from test import test_Base, Question, Answer
from user import user_Base
from sqlalchemy import create_engine, MetaData

from pathlib import Path

path_to_db = Path(__file__).parent.parent.parent.parent / 'database' / "telegram.db"

engine = create_engine(f'sqlite:///{path_to_db}', echo = True)

exmaples = [
    {
        'Week': 1,
        'Question': 'Какой Питон Язык?',
        'Answers': ['Интерпертируемый','Комплируемый'],
        'Right_answer': 0,
    },
    {
        'Week': 1,
        'Question': 'Какое ключевое слово отвечает за подключение модуля?',
        'Answers': ['Import','Include','Inject','Introduce'],
        'Right_answer': 0,
    },
    {
        'Week': 1,
        'Question': 'Какая типизация в Python?',
        'Answers': ['Динамическая','Cтатическая'],
        'Right_answer': 0,
    },
    {
        'Week': 1,
        'Question': 'Какая типизация в Python?',
        'Answers': ['Строгая','Cлабая'],
        'Right_answer': 0,
    },
    {
        'Week': 1,
        'Question': 'Есть ли в Python типы?',
        'Answers': ['Да','Нет'],
        'Right_answer': 0,
    },
    {
        'Week': 1,
        'Question': 'Где не применяются Python?',
        'Answers': ['Научные исследования','В высокопроизводительных системах','Прототипировании проектов', 'Машинном обучении'],
        'Right_answer': 0,
    },
]


def init_db(engine):
    for base in [homework_Base, test_Base, user_Base]:
        base.metadata.create_all(engine)

def insert_examples(engine, exmaples):

    jack = Question()
    jack.addresses  # Пустой список

    # Добавим адресов ему
    jack.addresses = [
            Address(email_address='jack@gmail.com'),
            Address(email_address='j25@yahoo.com'),
            Address(email_address='jack@hotmail.com'),
    ]
    

init_db(engine)
