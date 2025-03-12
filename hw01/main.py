from calculation import calculate
from data import load_data

def total_salary(path):
    salary = load_data(path)
    result = calculate(salary)

    return result

total, average = total_salary('salary.txt')
print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")

