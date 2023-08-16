from tasks.task_1 import test_1
from tasks.task_2 import test_2
from tasks.task_3 import flag_generator


def main():
    test_1()
    print('Тест 1 прошёл успешно')
    test_2()
    print('Тест 2 прошёл успешно')
    list_of_list = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
    ]
    flag_generator(list_of_list)
    print(f'Функция {flag_generator.__name__} залогировалась')


if __name__ == '__main__':
    main()
