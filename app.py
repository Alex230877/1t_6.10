import psycopg2
from time import sleep

for attempt in range(10):
    try:
        conn = psycopg2.connect(
            dbname="PostgreSQL_Sokolov",
            user="your_surname",
            password="your_password",
            host="db",
            port="5432"
        )
        break
    except psycopg2.OperationalError:
        print("PostgreSQL не готов, повтор через 5 секунд...")
        sleep(5)
else:
    raise Exception("Не удалось подключиться к базе данных.")

cursor = conn.cursor()

cursor.execute("""
    SELECT MIN(age), MAX(age)
    FROM test_table
    WHERE LENGTH(name) < 6;
""")

result = cursor.fetchone()
print(f"Минимальный возраст: {result[0]}")
print(f"Максимальный возраст: {result[1]}")

cursor.close()
conn.close()
