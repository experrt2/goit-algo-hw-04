from get_data import get_cats_info

cats_info = get_cats_info("cats.txt")

print(*cats_info, sep='\n')