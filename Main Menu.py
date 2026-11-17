import pyramid
import calculator


def main():
    while True:
        print("Виберіть дію:")
        print("1. Обчислення двох чисел")
        print("2. Побудувати піраміду")
        print("0. Вийти")
        choice = input("Введіть номер дії (0, 1 або 2): ").strip()

        if choice == "0":
            print("До побачення!")
            break

        if choice == "1":
            try: 
             calculator.calcX()
            except ValueError:
                print("Помилка: введіть числові значення.")
                continue
           
        elif choice == "2":
            try:
                n = int(input("Введіть висоту піраміди (від 1 до 10): "))
            except ValueError:
                print("Помилка: висота має бути цілим числом.")
                continue

            if not 1 <= n <= 10:
                print("Помилка: висота має бути від 1 до 10.")
                continue
            pyramid.buildpyramid(n) 
        else:
            print("Помилка: виберіть 0, 1 або 2.")
            continue 
main ()
          

  

