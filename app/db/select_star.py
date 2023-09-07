from pathlib import Path
import sqlite3


path_to_db = Path(__file__).parent.parent.parent / 'database' / "telegram.db"
connection = sqlite3.connect(path_to_db.resolve())
cursor = connection.cursor()


cursor.execute('SELECT * FROM questions')

print(cursor.fetchall())