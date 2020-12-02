from application.salary import calculate_salary
from db.people import get_employees
from datetime import datetime as dt

if __name__ == '__main__':
    print(dt.today().date())
    calculate_salary()
    get_employees()
