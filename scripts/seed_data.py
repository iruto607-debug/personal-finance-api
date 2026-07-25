import sqlite3
from pathlib import Path


DB_PATH = Path(__file__).resolve().parents[1] / "finance.db"


def seed():
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()

    cur.execute(
        """
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL
    )
    """
    )

    cur.execute(
        """
    CREATE TABLE IF NOT EXISTS finances (
        id INTEGER PRIMARY KEY,
        user_id INTEGER,
        amount REAL,
        description TEXT
    )
    """
    )

    cur.execute("DELETE FROM users")
    cur.execute("DELETE FROM finances")

    cur.executemany("INSERT INTO users (id, name) VALUES (?,?)", [(1, "Alice"), (2, "Bob")])
    cur.executemany(
        "INSERT INTO finances (id, user_id, amount, description) VALUES (?,?,?,?)",
        [
            (1, 1, 1200.0, "Salary"),
            (2, 1, -50.0, "Groceries"),
            (3, 2, -20.5, "Coffee"),
        ],
    )

    conn.commit()
    conn.close()


if __name__ == "__main__":
    seed()
    print(f"Seeded database at: {DB_PATH}")
