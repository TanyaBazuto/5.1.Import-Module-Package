import application.database.people
from application.salary import calculate_salary
from datetime import datetime
from application.prettytable import my_study   # п.4

current_date = datetime.now()

if __name__ == '__main__':
    application.database.people.get_employees()
    calculate_salary()
    print(current_date)
    print(my_study)
