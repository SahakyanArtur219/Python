import random 
import time


with open('random_number.txt', 'w') as file:
    
    for i in range(100):
        test_str = list(str(random.randint(1, 100)) for i in range(20))
        line = ' '.join(test_str)
        file.write(line + '\n')

with open('random_number.txt', 'r') as file:
    lines = file.readlines()



integer_lines = [list(map(int, line.split())) for line in lines]

filtered_lines = [list(filter(lambda x : x > 40, line)) for line in integer_lines]




with open('filtered_number.txt', 'w') as file:
    for l in filtered_lines:
        file.write(' '.join(map(str,l)) + '\n')




def read_file_generator(file_name):
    with open(file_name, 'r') as file:
        for l in file:
            yield list(map(int, l.split()))




def execution_time_decorator(func):
    def wraper(*args, **kwargs):
        time_begin = time.time()
        results = func(*args, **kwargs)
        time_end = time.time()
        print(f" the time of execution is equal {time_end - time_begin} sec")
        return results
    return wraper


@execution_time_decorator
def process_file(file_name):
    for l in read_file_generator(file_name):
        print(l)




process_file('filtered_number.txt')
