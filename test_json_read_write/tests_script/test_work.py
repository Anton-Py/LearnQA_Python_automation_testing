import json
import csv


def read_from_json():
    with open("../test_data/users.json", "r") as f:
        users = json.loads(f.read())

    users_list = users
    lst_user = []
    for r in users_list:
        user = {"name": r.get('name'), "gender": r.get("gender"), "address": r.get("address"), "age": r.get("age"),
                "books": []}
        lst_user.append(user)
    return lst_user


def read_from_csv():
    with open('../test_data/books.csv', newline='') as f:
        reader = csv.reader(f)

        # Извлекаем заголовок
        header = next(reader)
        lst_books = []
        # Итерируемся по данным делая из них словари
        for row in reader:
            books_dict = (dict(zip(header, row)))
            lst_books.append(books_dict)
        for book in lst_books:
            book.pop("Publisher")
    return lst_books


def test_write_to_json():
    list_books = read_from_csv()
    list_user = read_from_json()
    count = 0
    for book in list_books:
        list_user[count]["books"].append(book)
        count += 1
        if count == 28:
            count = 0

    with open("../test_data/reference_test.json", "w") as f:
        s = json.dumps(list_user, indent=4)
        f.write(s)
