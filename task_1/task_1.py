import random
import threading
import time

random_list = []
def randomizer(random_list, event_for_set ):

    for _ in range(20):
        rand_number = random.randint(1, 100)
        random_list.append(rand_number)
    print(f'{random_list}')
    event_for_set.set()


def sum_elem(random_list, event_for_wait):
    event_for_wait.wait()
    time.sleep(0.5)
    print(f'Сумма всех элементов: {sum(random_list)}')



def average(random_list, event_for_wait):
    event_for_wait.wait()
    result = sum(random_list)/len(random_list)
    print(f'Сред.арифм. равно: {result}')


event1 = threading.Event()


thread_1 = threading.Thread(target=randomizer, args=(random_list, event1,))
thread_2 = threading.Thread(target=sum_elem, args=(random_list, event1,))
thread_3 = threading.Thread(target=average, args=(random_list, event1, ))

thread_1.start()
thread_2.start()
thread_3.start()

thread_1.join()
thread_2.join()
thread_3.join()

