import random
import string


def generate_password(length):
    """Генерирует случ35а777706121198йный пароль заданной длины."""
    # Все возможные символы: буквы (нижний/верхний регистр), цифры, спецсимволы
    characters = string.ascii_letters + string.digits + string.punctuation

    # Генерация пароля
    password = ''.join(random.choice(characters) for i in range(length))
    return password


if __name__ == "__main__":
    print("Генератор случайных паролей")
    try:
        pass_length = int(input("Введите желаемую длину пароля: "))
        if pass_length <= 0:
            print("Длина пароля должна быть положительным числом.")
        else:
            new_password = generate_password(pass_length)
            print(f"Ваш сгенерированный пароль: {new_password}")
    except ValueError:
        print("Некорректный ввод. Пожалуйста, введите целое число для длины.")
