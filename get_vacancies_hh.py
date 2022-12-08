from collections import defaultdict
from itertools import count

import requests


def get_vacancies(language='Python', page=0, city_id=1, progremmer_id='1.221', period=30):
    url_vacancies = 'https://api.hh.ru/vacancies'
    params = {
        'period': period,
        'page': page,
        'area': city_id,
        'text': language,
        'specializations': progremmer_id
    }
    response = requests.get(url_vacancies, params=params)
    response.raise_for_status()
    return response.json()
 

def predict_rub_salary(salary_from=None, salary_to=None):
    if salary_from and salary_to:
        average_salary = (salary_from + salary_to) / 2
    elif salary_from:
        average_salary = salary_from * 1.2
    elif salary_to:
        average_salary = salary_to * 0.8
    return average_salary


def get_vacancies_statistics_hh(language='Python'):
    average_salaries = []
    for page in count(0, 1):
        vacancies = get_vacancies(language, page)
        if page >= vacancies['pages']-1:
            break

        for vacancy in vacancies['items']:
            if not vacancy['salary']:
                break
            if not vacancy['salary']['currency'] == 'RUR':
                break
            average_salaries.append(predict_rub_salary(vacancy['salary']['from'], 
                                                        vacancy['salary']['to']))
    if len(average_salaries):
        average_salary = int(sum(average_salaries) / len(average_salaries))
    else:
        average_salary = None

    characteristics_vacancies = { 
        "vacancies_found": vacancies['found'],
        "vacancies_processed": len(average_salaries),
        "average_salary": average_salary
    }
    return characteristics_vacancies


def get_statistics_language_hh():
    programming_languages = ['Python', 'Java', 'Javascript', 'Go', 'C', 'C#', 'C++', 'PHP']
    statistics_language = defaultdict()
    for language in programming_languages:
        statistics_language[language] = get_vacancies_statistics_hh(language)
    return statistics_language
