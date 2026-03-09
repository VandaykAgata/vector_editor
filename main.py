import sys
from random import choice

from models import Point, Line, Circle, Square
from editor import VectorEditor

def show_menu():
    """Простое меню команд для пользователя"""
    print("\n--- Векторный редактор (CLI) ---")
    print("1. Добавить точку (x, y)")
    print("2. Добавить отрезок (x1, y1, x2, y2)")
    print("3. Добавить круг (x, y, radius)")
    print("4. Добавить квадрат (x, y, side)")
    print("5. Показать все фигуры")
    print("6. Удалить фигуру по номеру")
    print("0. Выход")

def get_float_input(prompt):
    """
    Вспомогательная функция для безопасного ввода чисел.
    Если пользователь введет текст вместо числа, программа не 'упадет'.
    """
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Ошибка: пожалуйста, введите цифровое значение.")

def main():
    editor = VectorEditor()

    while True:
        show_menu()
        choice = input("\nВыберите действие:").strip()

        if choice == "1":
            x = get_float_input("Введите x: ")
            y = get_float_input("Введите y: ")
            editor.add_shape(Point(x, y))

        elif choice == '2':
            print("Координаты начала:")
            x1 = get_float_input("  x1: ")
            y1 = get_float_input("  y1: ")
            print("Координаты конца:")
            x2 = get_float_input("  x2: ")
            y2 = get_float_input("  y2: ")
            editor.add_shape(Line(x1, y1, x2, y2))

        elif choice == '3':
            x = get_float_input("Центр x: ")
            y = get_float_input("Центр y: ")
            r = get_float_input("Радиус: ")
            if r <= 0:
                print("Ошибка: радиус должен быть положительным.")
            else:
                editor.add_shape(Circle(x, y, r))

        elif choice == '4':
            x = get_float_input("Угол x: ")
            y = get_float_input("Угол y: ")
            side = get_float_input("Длина стороны: ")
            if side <= 0:
                print("Ошибка: сторона должна быть больше нуля.")
            else:
                editor.add_shape(Square(x, y, side))

        elif choice == '5':
            shapes = editor.get_all_shapes()
            if not shapes:
                print("\n[Инфо] Список фигур пока пуст.")
            else:
                print("\n--- Текущие фигуры ---")
                for i, s in enumerate(shapes):
                    print(f"[{i}] {s}")

        elif choice == '6':
            idx = input("Введите номер фигуры для удаления: ")
            if idx.isdigit():
                editor.delete_shape(int(idx))
            else:
                print("Ошибка: введите целое число (индекс).")

        elif choice == '0':
            print("Завершение работы. До свидания!")
            sys.exit()

        else:
            print("Неизвестная команда, попробуйте еще раз.")

if __name__ == "__main__":
    # Запуск основной логики
    try:
        main()
    except KeyboardInterrupt:
        # Корректный выход при нажатии Ctrl+C
        print("\nПрограмма принудительно остановлена.")
        sys.exit()
