import psycopg2


def connect_db():
    return psycopg2.connect(
        dbname='u10_con',
        host='localhost',
        port=5432,
        user='postgres',
        password=1995
    )