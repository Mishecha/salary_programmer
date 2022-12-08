import os

from terminaltables import AsciiTable
from dotenv import load_dotenv

from get_vacancies_sj import get_statistics_language_sj
from get_vacancies_hh import get_statistics_language_hh


def create_table_vacancies(title, vacancies):
    about_vacancies = [['Язык программирования', 'Вакансий найдено', 'Вакансий обработано', 'Средняя зарплата']]
    for language, value in vacancies.items():
        about_vacancies.append([
            language, 
            value['vacancies_found'],
            value['vacancies_processed'],
            value['average_salary']
        ])

    table_instance = AsciiTable(about_vacancies, title)
    table_instance.justify_columns[2] = 'right'
    return table_instance.table


def main():
    load_dotenv()
    super_job_key = os.environ['SUPER_JOB_KEY']
    statistics_language_sj = get_statistics_language_sj(super_job_key)
    statistics_language_hh = get_statistics_language_hh()

    title_hh  = 'HeadHunter'
    title_sj  = 'SuperJob'

    table_sj = create_table_vacancies(title_sj, statistics_language_sj)
    table_hh = create_table_vacancies(title_hh, statistics_language_hh)

    print(table_sj, '/n', table_hh)


if __name__ == "__main__":
    main()