import random
import string

# Функция генерации
def generate_password(length=8):
    if length < 4:
        raise ValueError("Длина пароля должна быть не менее 4 символов")
    
    # Набор символов
    chars = string.ascii_letters + string.digits + "!@#$%^&*"
    
    # Гарантируем хотя бы по одному из каждого типа
    password = [
        random.choice(string.ascii_lowercase),
        random.choice(string.ascii_uppercase),
        random.choice(string.digits),
        random.choice("!@#$%^&*")
    ]
    
    # Дополняем до нужной длины
    for _ in range(length - 4):
        password.append(random.choice(chars))
    
    # Перемешиваем
    random.shuffle(password)
    
    return ''.join(password)

# Основной код
def main():
    print("🔐 Генератор паролей")
    print("Пароль будет содержать: строчные, заглавные буквы, цифры и спецсимволы")
    
    try:
        length = int(input("Длина пароля (минимум 4): "))
        password = generate_password(length)
        print(f"Ваш пароль: {password}")
        
    except ValueError as e:
        print(f"❗ Ошибка: {e}")
    except Exception as e:
        print(f"❗ Ошибка ввода: введите число")

# Улучшение: копирование в буфер
# Для этого можно использовать pyperclip, но пока просто выводим. 











