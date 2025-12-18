# Функции
def celsius_to_fahrenheit(c):
    return (c * 9/5) + 32

def fahrenheit_to_celsius(f):
    return (f - 32) * 5/9

# Основной код
def main():
    print("🌡️ Конвертер температур")
    print("Введите температуру и единицу: 25 C или 77 F")
    
    try:
        user_input = input("Температура: ").strip()
        value_str, unit = user_input.split()
        value = float(value_str)
        unit = unit.upper()
        
        if unit == "C":
            result = celsius_to_fahrenheit(value)
            print(f"{value}°C = {result:.1f}°F")
        elif unit == "F":
            result = fahrenheit_to_celsius(value)
            print(f"{value}°F = {result:.1f}°C")
        else:
            print("❗ Единица должна быть C или F")
            
    except ValueError:
        print("❗ Неверный формат. Пример: 25 C")
    except Exception as e:
        print(f"❗ Ошибка: {e}")

# цикл
while True:
    main()
    again = input("\nПродолжить? (да/нет): ").lower()
    if again != "да":
        print("До встречи!")
        break
    