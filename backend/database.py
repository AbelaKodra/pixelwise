import sqlite3

DB_NAME = "pixelwise.db"

def init_db():
	conn = sqlite3.connect(DB_NAME)

	conn.execute("""
		CREATE TABLE IF NOT EXISTS predictions (
			id INTEGER PRIMARY KEY AUTOINCREMENT,
			digit INTEGER,
			confidence REAL
		)
	""")

	conn.commit()
	conn.close()
