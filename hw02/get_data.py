def get_cats_info(path):
    try:
        with open(path, 'r', encoding='utf-8') as file:
            cat_base = []
            for line in file:
                line = line.strip()
                cat_id, name, age  = line.split(',')
                cat_base.append({"id": cat_id, "name": name, "age": age})

            return cat_base

    except Exception as e:
        print(f'{e} with file')



