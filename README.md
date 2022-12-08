# Сравниваем вакансии программистов
Проект собирает данные об вакансиях с сайтов [HeadHunter API](https://dev.hh.ru/) и [SuperJob](https://api.superjob.ru/), структруирует данные для таблицы, а после создает и выводит ее в констоль.

## Как установить код

Python3 должен быть уже установлен. 
Затем используйте `pip` для установки зависимостей:
```
pip install -r requirements.txt
```

## Переменные окружения
Создать этот токен можно [здесь](https://api.superjob.ru/). После вставьте токен super_job_key в .env.
В env нужно написать так:
```
SUPER_JOB_KEY=токен Super_Job
```

## Запуск кода
Для того чтобы код работал, надо открыть терминал, написать cd и путь до вашего проекта.
Для просмотра таблицы с данными об вакансиях програмистов нужно написать:
```
python create_table.py
```

## Цель проекта
Код написан в образовательных целях на онлайн-курсе для веб-разработчиков [dvmn.org](https://dvmn.org).
