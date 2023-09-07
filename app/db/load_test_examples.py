from pathlib import Path
import sqlite3

examples = [
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
        'Question': 'Есть ли Python типы?',
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

path_to_db = Path(__file__).parent.parent.parent / 'database' / "telegram.db"
connection = sqlite3.connect(path_to_db.resolve())
cursor = connection.cursor()

for example in examples:
    cursor.execute(
    '''
    INSERT INTO questions (question_text,week)
    VALUES 
    (?,?)
    RETURNING  question_id
    ''',
    (example['Question'],example['Week'])
    )
    (question_id,) = cursor.fetchone()

    answers  = example['Answers']
    right_answers = [0]*len(answers)
    right_answers[example['Right_answer']] = 1 

    cursor.executemany(
    '''
        insert into answers (question_id,answer_text,is_right)
        VALUES 
        (?,?,?)
    ''',
    [item for item in zip([question_id]*len(answers),answers,right_answers)]
    )

connection.commit()