import time


def func_001():
    time.sleep(2)
    return 'r001'


def func_002():
    time.sleep(2)
    return 'r002'


def main():
    print(f'main: start')
    p001 = func_001()
    print(f'main: p001 = {p001}')
    p002 = func_002()
    print(f'main: p002 = {p002}')
    print(f'main: end')

if __name__ == '__main__':
    main()
