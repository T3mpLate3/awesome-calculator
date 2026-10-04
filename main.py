import sys
from math_utils import pentagonal_number
from fibonacci_module import calculate_fibonacci

def print_usage():
    print("Использование: python main.py <команда> <число>")
    print("Доступные команды:")
    print("  fib <N>   - вычислить N-е число Фибоначчи")
    print("  pent <N>  - вычислить N-е пятиугольное число")

def main():
    if len(sys.argv) != 3:
        print("Ошибка: Неверное количество аргументов.")
        print_usage()
        sys.exit(1)

    command = sys.argv[1].lower()
    try:
        n = int(sys.argv[2])
        if n < 0:
            raise ValueError
    except ValueError:
        print(f"Ошибка: Аргумент '{sys.argv[2]}' должен быть целым неотрицательным числом.")
        sys.exit(1)

    try:
        if command == 'fib':
            result = calculate_fibonacci(n)
            print(f"Число Фибоначчи для N={n}: {result}")
        elif command == 'pent':
            result = pentagonal_number(n)
            print(f"Пятиугольное число для N={n}: {result}")
        else:
            print(f"Ошибка: Неизвестная команда '{command}'.")
            print_usage()
            sys.exit(1)
    except ValueError as e:
        print(f"Ошибка вычисления: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()