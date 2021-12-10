#!/usr/bin/env python
# nevl 2021

def is_number(data, type, check_zero=False):
    try:
        if (check_zero and type(data) == 0) or \
                (type == int and data.find('.') >= 0) or \
                data.find('-') >= 0:
            raise ValueError
        return type(data)
    except:
        return None

def input_number(type, text, check_zero=False):
    while True:
        data = is_number(input(text), type, check_zero)
        if data is None:
            print(f'Enter number in {type} format. {"" if not check_zero else "Not zero."}')
        else:
            return data

if __name__ == '__main__':
    while True:
        # fetch name
        while True:
            name = input('Enter name: ')
            strings = name.split()
            flag = strings[0].isalpha() and True if len(strings) < 2 else strings[1].isalpha()
            if not flag or name.count(' ') > 1:
                print('Not a name. Enter only letters and one space.')
                print(name.count(' '), not name.isalpha())
            else:
                break

        # check name
        if name.lower() == 'stop':
            quit(0)

        # fetch numbers
        number1 = input_number(int, 'Enter number 1: ')
        number2 = input_number(int, 'Enter number 2: ')
        number3 = input_number(float, 'Enter number 3: ', check_zero=True)

        print('{}, hi!\nSum = {}'.format(name.title(), (int(f'{number1}'*3) + int(f'{number2}'*2)) / float(number3)))
