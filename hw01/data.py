
def load_data(path):
    try:
        with open(path, 'r', encoding='utf-8') as file:
            salary = []
            for line in file:
                line = line.strip()
                items = line.split(',')
                salary.append(items)

            return salary

    except Exception as e:
        print(f'{e} with file')

