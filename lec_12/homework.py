import random
import time

def create_file():
    with open(file_name, 'w') as file:
        for i in range(100):
            numbers = []
            for j in range(20):
                numbers.append(str(random.randint(1, 50)))
            file.write(" ".join(numbers) + "\n")
     
def read_filter():   
    with open(file_name, 'r') as file:
        data = file.readlines()
        
    for line in data:
        line.replace('\n', '')
        line = line.split()
        line = list(map(int, line))
        
        filtered_numbers = list(filter(lambda x: x > 40, line))
        
        with open(file_name, 'a') as file:
            file.write(f"\nLine: {line}\n")
            file.write(f"Numbers which are > 40 for this line: {filtered_numbers}\n")
            
        print(line)
        print("Numbers which are > 40 for this line: ", filtered_numbers)
    
def execution_time_decorator(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Execution time of {func.__name__}: {end_time - start_time}\n")
        return result
    return wrapper
    
@execution_time_decorator
def file_generator():
    with open(file_name, 'r') as file:
        for line in file:
            yield line
     
file_name = "random_numbers.txt"   
create_file()
read_filter()        

print("\nRead file as generator")
for i in file_generator():
    print(i)
