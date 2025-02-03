import json
import random
import threading
from sympy import isprime
import math


path = input('Введите имя файла: ')




random_list = []
def randomizer(random_list, event_for_set):
    for _ in range(20):
        rand_number = random.randint(1, 10)
        random_list.append(rand_number)
    print(f'Список чисел: {random_list}')

    with open(fr'files\{path}.json', 'w', encoding='utf-8') as file:
        json.dump(random_list, file, ensure_ascii=False, indent=3)
    event_for_set.set()

def simple_number(event_for_wait):
    event_for_wait.wait()
    with open(fr'files\{path}.json', 'r', encoding='utf-8') as file:
        random_list_from_file = json.load(file)
    new_list = []
    for number in random_list_from_file:
        if isprime(number):
            new_list.append(number)
    print(f'Простые числа: {new_list} записаны в файл')
    with open(r'files\simple_numbers', 'w', encoding='utf-8') as file:
        file.write(str(new_list))

def factorial_of_number(event_for_wait):
    event_for_wait.wait()
    with open(fr'files\{path}.json', 'r', encoding='utf-8') as file:
        random_list_from_file = json.load(file)
    new_list = []
    for number in random_list_from_file:
        factorial = math.factorial(number)
        new_list.append(factorial)
    print(f'Факториалы чисел:\n {new_list}\n записаны в файл')

    with open(r'files\factorial_of_numbers', 'w', encoding='utf-8') as file:
        file.write(str(new_list))


event = threading.Event()

thread_1 = threading.Thread(target=randomizer, args=(random_list, event,))
thread_2 = threading.Thread(target=simple_number, args=(event,))
thread_3 = threading.Thread(target=factorial_of_number, args=(event,))

thread_1.start()
thread_2.start()
thread_3.start()

thread_1.join()
thread_2.join()
thread_3.join()
