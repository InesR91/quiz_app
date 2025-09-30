import sqlite3

class Question:
    def __init__(self, position: int, title: str, text: str, image: str = None, id: int = None):
        self.id = id
        self.position = position
        self.title = title
        self.text = text
        self.image = image

    # ---- Sérialisation vers JSON
    def to_dict(self):
        return {
            "id": self.id,
            "position": self.position,
            "title": self.title,
            "text": self.text,
            "image": self.image
        }

    # ---- Sauvegarde en BDD
    def save(self, db_path):
        conn = sqlite3.connect(db_path)
        cur = conn.cursor()
        cur.execute(
            "INSERT INTO Question (position, title, text, image) VALUES (?, ?, ?, ?)",
            (self.position, self.title, self.text, self.image)
        )
        conn.commit()
        self.id = cur.lastrowid
        conn.close()