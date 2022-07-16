import random

def request_number(message):
    while True:
        result = input(message)

        if result.isdigit():
            result = int(result)
            break
        else:
            print('Вы должны ввести число!')
    return result


def generate_symbols_list(is_numbers, is_letters_big, is_letters_little=False, is_specials_1=False,
                          is_specials_minus=False):
    symbols = []

    if is_numbers:
        symbols.extend(numbers)

    if is_letters_big:
        symbols.extend(letters_big)

    if is_letters_little:
        symbols.extend(letters_little)

    if is_specials_1:
        symbols.extend(numbers)

    if is_specials_minus:
        symbols = list(set(symbols) - set(specials_minus))

    return symbols


def generate_password(n, length, is_numbers=False, is_letters_big=False, is_letters_little=False, is_specials_1=False,
                      is_specials_minus=False):
    symbols = generate_symbols_list(is_numbers, is_letters_big, is_letters_little, is_specials_1, is_specials_minus)
    passwords1 = []
    for i in range(n):
        passwords1.append(''.join(random.choice(symbols) for _ in range(length)))

    return passwords1


numbers = set([*'0123456789'])
letters_big = set([*'ABCDEFGHIJKLMNOPQRSTUVWXYZ'])
letters_little = set([*'abcdefghijklmnopqrstuvwxyz'])
specials_1 = set([*'!#$%&*+-=?@^_'])
specials_minus = set([*'il1Lo0O'])

print('Приветствую вас в генераторе паролей!')
n = request_number('Количество паролей для генерации: ')
length = request_number('Введите длину пароля: ')

is_numbers = input('Включать ли цифры? [y/n] ').lower() == 'y'
is_letters_big = input('Включать ли прописные буквы? [y/n] ').lower() == 'y'
is_letters_little = input('Включать ли строчные буквы? [y/n] ').lower() == 'y'
is_specials_1 = input('Включать ли символы? [y/n] ').lower() == 'y'
is_specials_minus = input('Исключать ли неоднозначные символы? [y/n] ').lower() == 'y'

print('Ваши  пароли  готовы!')
print(generate_password(n, length, is_numbers, is_letters_big, is_letters_little, is_specials_1, is_specials_minus))