-- Создание таблиц

CREATE TABLE public.job (
    id BIGINT PRIMARY KEY,
    company_name VARCHAR(255) NOT NULL,
    experience DOUBLE PRECISION,
    title VARCHAR(500),
    max_salary INTEGER,
    min_salary INTEGER
);

CREATE TABLE public.person (
    id BIGINT PRIMARY KEY,
    email VARCHAR(100) NOT NULL,
    first_name VARCHAR(100) NOT NULL,
    last_name VARCHAR(100) NOT NULL,
    phone_number VARCHAR(100)
);

CREATE TABLE public.job_history (
    id BIGINT PRIMARY KEY,
    date_from DATE,
    date_to DATE,
    salary INTEGER,
    job_id BIGINT REFERENCES public.job(id),
    person_id BIGINT REFERENCES public.person(id)
);
