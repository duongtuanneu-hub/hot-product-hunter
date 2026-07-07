
import sqlite3



conn = sqlite3.connect("products.db")



cursor = conn.cursor()


cursor.execute("""
CREATE TABLE IF NOT EXISTS products(

    title TEXT PRIMARY KEY,

    price INTEGER,

    stock INTEGER,

    url TEXT

)
""")

conn.commit()