import psycopg2


conn = psycopg2.connect(
    host="localhost",
    port=5432,
    database="testdb",
    user="postgres",
    password="3984068e"
)