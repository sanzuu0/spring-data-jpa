import os
import random
import string
from datetime import datetime, timedelta

def random_string(length):
    return ''.join(random.choices(string.ascii_letters + string.digits + ' ', k=length)).strip()

def random_email():
    return f"{random_string(5).lower()}@{random_string(5).lower()}.com"

def random_date(start_year=2000, end_year=2023):
    start_date = datetime(start_year, 1, 1)
    end_date = datetime(end_year, 12, 31)
    delta = end_date - start_date
    random_days = random.randint(0, delta.days)
    return (start_date + timedelta(days=random_days)).date()

def generate_job_inserts(n):
    inserts = []
    for i in range(1, n+1):
        company_name = random_string(20).replace("'", "''")  # Экранирование апострофов
        experience = round(random.uniform(0, 20), 2)
        title = random_string(30).replace("'", "''")
        max_salary = random.randint(30000, 150000)
        min_salary = random.randint(20000, 30000)
        inserts.append(f"({i}, '{company_name}', {experience}, '{title}', {max_salary}, {min_salary})")
    return inserts

def generate_person_inserts(n):
    inserts = []
    for i in range(1, n+1):
        email = random_email()
        first_name = random_string(10).replace("'", "''")
        last_name = random_string(10).replace("'", "''")
        phone_number = ''.join(random.choices(string.digits, k=10))
        inserts.append(f"({i}, '{email}', '{first_name}', '{last_name}', '{phone_number}')")
    return inserts

def generate_job_history_inserts(n, job_n, person_n):
    inserts = []
    for i in range(1, n+1):
        date_from = random_date()
        # Убедимся, что date_to не раньше date_from
        date_to = date_from + timedelta(days=random.randint(30, 365*5))
        salary = random.randint(20000, 150000)
        job_id = random.randint(1, job_n)
        person_id = random.randint(1, person_n)
        inserts.append(f"({i}, '{date_from}', '{date_to}', {salary}, {job_id}, {person_id})")
    return inserts

def main():
    n = 1000  # Количество записей

    # Определяем абсолютные пути для сохранения SQL файлов
    base_dir = os.path.dirname(os.path.abspath(__file__))
    project_root = os.path.abspath(os.path.join(base_dir, '..'))
    dump_dir = os.path.join(project_root, 'dump')

    # Создаем директорию dump, если она не существует
    os.makedirs(dump_dir, exist_ok=True)

    # Генерация INSERT для таблицы job
    job_inserts = generate_job_inserts(n)
    job_file_path = os.path.join(dump_dir, 'job_inserts.sql')
    with open(job_file_path, 'w') as f:
        f.write("INSERT INTO public.job (id, company_name, experience, title, max_salary, min_salary) VALUES\n")
        f.write(",\n".join(job_inserts))
        f.write(";\n")

    # Генерация INSERT для таблицы person
    person_inserts = generate_person_inserts(n)
    person_file_path = os.path.join(dump_dir, 'person_inserts.sql')
    with open(person_file_path, 'w') as f:
        f.write("INSERT INTO public.person (id, email, first_name, last_name, phone_number) VALUES\n")
        f.write(",\n".join(person_inserts))
        f.write(";\n")

    # Генерация INSERT для таблицы job_history
    job_history_inserts = generate_job_history_inserts(n, job_n=n, person_n=n)
    job_history_file_path = os.path.join(dump_dir, 'job_history_inserts.sql')
    with open(job_history_file_path, 'w') as f:
        f.write("INSERT INTO public.job_history (id, date_from, date_to, salary, job_id, person_id) VALUES\n")
        f.write(",\n".join(job_history_inserts))
        f.write(";\n")

    # Объединение всех INSERT запросов в один файл
    database_dump_path = os.path.join(dump_dir, 'database_dump.sql')
    with open(database_dump_path, 'w') as outfile:
        with open(job_file_path, 'r') as infile:
            outfile.write(infile.read())
        with open(person_file_path, 'r') as infile:
            outfile.write(infile.read())
        with open(job_history_file_path, 'r') as infile:
            outfile.write(infile.read())

    print(f"INSERT-запросы сгенерированы и сохранены в {dump_dir}/.")

if __name__ == "__main__":
    main()
