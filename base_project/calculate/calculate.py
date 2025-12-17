def calculate(num1, num2, operation):
    if operation == "+":
        return num1 + num2
    elif operation == "-":
        return num1 - num2
    elif operation == "*":
        return num1 * num2
    elif operation == "/":
        if num2 == 0:
            raise ZeroDivisionError("На ноль делить нельзя!")
        return num1 / num2
    else:
        raise ValueError("Неверная операция. Доступно: +, -, *, /")


def main():
    print("🔢 Простой калькулятор")
    print("Доступные операции: +, -, *, /")
    
    try:
        a = float(input("Первое число: "))
        b = float(input("Второе число: "))
        op = input("Операция: ")
        
        result = calculate(a, b, op)
        print(f"Результат: {result}")
        
    except ValueError as e:
        if "could not convert" in str(e):
            print("❗ Ошибка: введите число!")
        else:
            print(f"❗ {e}")
    except ZeroDivisionError as e:
        print(f"❗ Ошибка: {e}")
    except Exception as e:
        print(f"❗ Непредвиденная ошибка: {e}")


if __name__ == "__main__":
    main()


