from dastur.db import connect_db


def register(username, address,password):
    connection = connect_db()
    cursor = connection.cursor()
    cursor.execute("""
    INSERT INTO users (username, address, password)
    VALUES (%s, %s, %s)""",(username,address,password))
    print(f"{username} has been registered successfully")
    connection.commit()
    connection.close()
    return True


# register('admin','qoraqamish','1234')

def login(username, password):
    connection = connect_db()
    cursor = connection.cursor()
    cursor.execute("""
    SELECT * FROM users WHERE username = %s and password=%s""",(username,password))
    user = cursor.fetchone()
    if user is  None:
        return "Not found this user"
    else:
        print(f"{username} login successfully")
        return user


# login('admin','1234')

