def find_gcd(a, b):
    while b:
        a, b = b, a % b
    return a


def main():
    try:
        num1 = int(input("Введіть перше число: "))
        num2 = int(input("Введіть друге число: "))

        if num1 < 0 or num2 < 0:
            raise ValueError("Числа повинні бути додатніми.")

        gcd_result = find_gcd(num1, num2)
        print(
            f"Найбільший спільний дільник чисел {num1} і {num2} дорівнює {gcd_result}"
        )

    except ValueError as ve:
        print(f"Помилка: {ve}")
    except Exception as e:
        print(f"Виникла помилка: {e}")


if __name__ == "__main__":
    main()
