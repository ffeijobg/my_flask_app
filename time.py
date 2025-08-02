import time

def tictoc(func):
    def wrapper():
        t1 = time.time()
        func()
        t2 = time.time() - t1
        print(f'Took {t2:.2f} seconds')
    return wrapper

@tictoc
def do_this():
    #Test code execution
    time.sleep(60)

@tictoc
def do_that():
    #Test code execution
    time.sleep(120)

def main():
    print("Start")
    do_this()
    print("First status!")
    do_that()
    print("Second status!")


if __name__ == '__main__':
    main()