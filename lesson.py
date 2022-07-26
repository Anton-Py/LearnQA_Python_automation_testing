# # context_manager
# with open("../test_data/example_r.txt", "r") as file:
#     print(file.read())
#     # No need to call close method
#
# print("\n", 20 * "=", "\n")
#
# with open("../test_data/example_r.txt", "r") as file:
#     for line in file.readlines():
#         # Break line fix end=""
#         print(line)
# context_manager_wr
# with open("../test_data/example_w.txt", "w") as file:
#     for n in range(10):
#         file.write(str(n) + "\n")
#
# csv_reader
# import csv
from csv import DictReader
#
# with open('../test_data/books.csv', newline='') as f:
#     reader = csv.reader(f)
#
#     # Извлекаем заголовок
#     header = next(reader)
#
#     # Итерируемся по данным делая из них словари
#     for row in reader:
#         # pass
#         print(dict(zip(header, row)))
#
# print(100 * "+")
#
# with open('../test_data/books.csv', newline='') as f:
#     reader = DictReader(f)
#     # Итерируемся по данным делая из них словари
#     for row in reader:
#         print(row)
# # csv_writer.py
# import csv
#
# with open('../test_data/eggs.csv', 'w', newline='') as csv_file:
#     writer = csv.writer(csv_file, delimiter=',', )
#
#     writer.writerow(['data', 'result', 'code'])
#     for i in range(10):
#         writer.writerow([i, i * 100, str(bin(i))])
# #
# # # TODO: 3. Попробуйте самостоятельно разобрать работу с методом DictWriter
#
# # json_reader.py
# import json
#
# with open("../files/example.json", "r") as f:
#     users = json.loads(f.read())
#
# users_list = users['users']
#
# for user in users_list:
#     print(user)
#
# some_file = open("../files/example_write.txt", "w")
#
# # txt_writer.py
# import json
#
# data = {
#     "users": [
#         {"login": "Alisa", "email": "alisa.april.one@gmail.ru"},
#         {"login": "Plaksa", "email": "cat@gmail.ru"},
#         {"login": "MMayers", "email": "fromhellwithlove@gmail.com"},
#     ]
# }
#
# with open("example.json", "w") as f:
#     s = json.dumps(data, indent=4)
#     f.write(s)
