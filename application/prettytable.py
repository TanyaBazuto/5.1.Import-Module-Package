from prettytable import PrettyTable


def my_study():
    study = PrettyTable()
    study.field_names = ["Модули курса", "Номер группы", "Количество занятий", "Статус"]
    study.add_row(["Основы языка программирования Python", 'PY-94', 9, 'Завершено'])
    study.add_row(["Git — система контроля версий", 'GIT-85', 6, 'Завершено'])
    study.add_row(["ООП и работа с API", 'PYAPI-94', 7, 'Завершено'])
    study.add_row(["Базы данных для python-разработчиков", 'SQLPY-94', 7, 'Завершено'])
    study.add_row(["Профессиональная работа с Python", 'ADPY-94', 5, 'В процессе'])
    return study

