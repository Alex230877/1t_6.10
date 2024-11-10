import psycopg2

# Установление соединения с базой данных PostgreSQL
conn = psycopg2.connect(
    dbname="PostgreSQL_Sokolov", 
    user="your_surname", 
    password="your_password", 
    host="db", 
    port="5432"
)

cursor = conn.cursor()

# Запрос для поиска минимального и максимального возраста для имен длиной менее 6 символов
cursor.execute("""
    SELECT MIN(age), MAX(age)
    FROM test_table
    WHERE LENGTH(name) < 6;
""")

# Получение результата и вывод в терминал
result = cursor.fetchone()
print(f"Минимальный возраст: {result[0]}")
print(f"Максимальный возраст: {result[1]}")

# Закрытие соединения
cursor.close()
conn.close()
