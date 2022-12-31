import time
def time_wait(n:int)-> None:
    for i in range(3):
        time.sleep(1)
        print(f'{n} : {i + 1} 번째')

def process_time()-> None:
    start = time.time()

    time_wait(n=3)
    time_wait(n=1)

    end = time.time()
    print(f'경과 시간 : {end - start}')

def main()-> None:
    process_time()    


main()