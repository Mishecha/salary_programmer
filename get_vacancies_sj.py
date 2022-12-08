from collections import defaultdict
from itertools import count

import requests


def get_vacancies(super_job_key, language='Python', page=2, city_id=4, branch_id=48):
    super_job_url = 'https://api.superjob.ru/2.0/vacancies/'
    headers = {
        'X-Api-App-Id': super_job_key
    }

    params = {
        'town': city_id,
        'page': page,
        'keyword' : language,
        'catalogues' : branch_id
    }

    response = requests.get(super_job_url, headers=headers, params=params)
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


def get_vacancies_statistics_sj(super_job_key, language='Python'):
    average_salaries = []
    for page in count(0, 1):
        vacancies = get_vacancies(super_job_key, language, page)        

        for vacancy in vacancies['objects']:
            if not vacancy['payment_from'] and not vacancy['payment_to']:
                continue
            if not vacancy['currency'] == 'rub':
                continue
            average_salaries.append(predict_rub_salary(vacancy['payment_from'], 
                                                        vacancy['payment_to']))
            if vacancies['more'] == False:
                break
                                   
    if len(average_salaries):
        average_salary = int(sum(average_salaries) / len(average_salaries))
    else:
        average_salary = None

    characteristics_vacancies = { 
        "vacancies_found": vacancies['total'],
        "vacancies_processed": len(average_salaries),
        "average_salary": average_salary
    }
    return characteristics_vacancies
    

def get_statistics_language_sj(super_job_key):
    programming_languages = ['Python', 'Java', 'Javascript', 'Go', 'C', 'C#', 'C++', 'PHP']
    
    statistics_language = defaultdict()
    for language in programming_languages:
        statistics_language[language] = get_vacancies_statistics_sj(super_job_key, language)
    return statistics_language
