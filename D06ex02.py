import random


def write_ten_numbers(filename):
    with open(filename, 'a') as file:
        count = 0
        while count < 10:
            ran_num = random.randint(1, 100)
            file.write(str(ran_num)+ " ")
            count+=1


write_ten_numbers('ten_random_numbers.txt')
