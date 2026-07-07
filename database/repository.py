
from database.database import (
    conn,
    cursor
)


from schemas.product import Product


def get_product_from_db(title):

    cursor.execute("""

    SELECT *

    FROM products

    WHERE title = ?

    """, (title,))
    
    

    row = cursor.fetchone()
    if row is None:
        return None

    return Product(

        title=row[0],

        price=row[1],

        stock=bool(row[2]),

        url=row[3]

    )



def save_product_to_db(product):

    cursor.execute("""

    INSERT OR REPLACE INTO products

    VALUES (?, ?, ?, ?)

    """, (

        product.title,

        product.price,

        product.stock,

        product.url

    ))

    conn.commit()
