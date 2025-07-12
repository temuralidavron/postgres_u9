from dastur.db import connect_db


def create_cat(title):
    db = connect_db()
    cursor = db.cursor()
    cursor.execute("""
    insert into category (title )
    values (%s)""", (title,))
    print(f"Inserted {title}")
    db.commit()
    db.close()
    return None


def cat_list():
    db = connect_db()
    cursor = db.cursor()
    cursor.execute("select * from category")
    data = cursor.fetchall()
    for row in data:
        print(f"{row[0]} - {row[1]}")
    return None


def create_product(title, price, description, quantity, cat_id):
    db = connect_db()
    cursor = db.cursor()
    cursor.execute("""
    insert into product (title, price, description, quantity, cat_id )
    values (%s,%s,%s,%s,%s)""", (title, price, description, quantity, cat_id))
    print(f"Inserted {title} product")
    db.commit()
    db.close()
    return None


def expinsive_price():
    db = connect_db()
    cursor = db.cursor()
    cursor.execute("select * from product where price=(select max(price) from product)")
    data = cursor.fetchone()

    answer=(f"{data[0]} - {data[1]} narxi {data[2]}")
    return answer


def cheap_price():
    db = connect_db()
    cursor = db.cursor()
    cursor.execute("select * from product where price=(select min(price) from product)")
    data = cursor.fetchone()
    answer=(f"{data[0]} - {data[1]} narxi {data[2]}")
    return answer

def guruh_b():
    db = connect_db()
    cursor = db.cursor()
    cursor.execute("""
    SELECT DISTINCT ON (cat_id) cat_id, title, price
FROM product
ORDER BY cat_id, price DESC;""")
    data = cursor.fetchall()
    return data



# create_product("sustav", 40000, "yaxshi doruuu", 100, 1)
# create_cat("oziq-ovqat")
