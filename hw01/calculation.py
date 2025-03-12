def calculate(salary):
    total = 0

    for item in salary:
        total += int(item[1])

    average = total / len(salary)

    return total, average


