import sqlite3

DB_NAME = "pixelwise.db"

def save_prediction(digit, confidence):
	conn = sqlite3.connect(DB_NAME)

	conn.execute(
		"INSERT INTO predictions (digit, confidence) VALUES (?, ?)",
		(digit, confidence)
	)

	conn.commit()
	conn.close()
