import argparse

def main():
    # Создаем парсер с описанием, которое просит Хекслет
    parser = argparse.ArgumentParser(
        description='Compares two configuration files and shows a difference.'
    )
    
    # Добавляем аргументы (обязательно в таком порядке)
    parser.add_argument('first_file')
    parser.add_argument('second_file')

    # Парсим аргументы (это и выведет справку при флаге -h)
    args = parser.parse_args()
    print(args)
if __name__ == '__main__':
    main()
