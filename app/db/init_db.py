import sqlite3
from pathlib import Path 


path_to_db = Path(__file__).parent.parent.parent / 'database' / "telegram.db"
connection = sqlite3.connect(path_to_db.resolve())
cursor = connection.cursor()

cursor.execute('''
    DROP TABLE IF EXISTS user          
''')

cursor.execute('''
    CREATE TABLE user (
        user_id INTEGER primary key autoincrement,
        telegram_id INTEGER 
    )'''
)


cursor.execute('''
    DROP TABLE IF EXISTS questions         
''')
cursor.execute('''
    CREATE TABLE questions (
        question_id INTEGER  primary key autoincrement,
        question_text TEXT,
        week INTEGER
    )'''
)
               
               
cursor.execute('''
    DROP TABLE IF EXISTS answers;         
''')
               
                
cursor.execute('''     
    CREATE TABLE IF NOT EXISTS answers (
        answer_id INTEGER  primary key autoincrement,
        question_id INTEGER,
        answer_text TEXT,
        is_right INTEGER,
        FOREIGN KEY(question_id) REFERENCES questions(question_id)
    )'''
)

cursor.execute('''
    DROP TABLE IF EXISTS quiz_results         
''')

cursor.execute('''   
    CREATE TABLE IF NOT EXISTS quiz_results (
        result_id INTEGER primary key autoincrement,
        user_id INTEGER,
        question_id INTEGER,
        result INTEGER,
        FOREIGN KEY(question_id) REFERENCES questions(question_id),
        FOREIGN KEY(user_id) REFERENCES user(user_id)        
    )''' 
)

   