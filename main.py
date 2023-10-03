def input_error(func):
    def inner(*user):
        try:
            return func(*user)
        except IndexError:
            return "Give me name and phone please" 
        except KeyError:
            return 'User not in dict'
    return inner

dict_phone = {}

@input_error
def add_func(*user):
    dict_phone.setdefault(user[1], user[2])
    return f'Add {user[1]} and phone {user[2]}'

@input_error
def change_func(*user):
    if user[1] not in dict_phone:
        raise KeyError
    dict_phone[user[1]] = user[2]
    return f'Change phone {user[1]}'

@input_error
def phone_func(*user):
    return dict_phone[user]

def hello_func(*user):
    return 'How can I help you?'

@input_error
def show_all_func(*user):
    return f'All dict {dict_phone}'


def main(*user):
    if user[0] == 'add':
        return add_func(*user)
    elif user[0] == 'change':
        return change_func(*user)
    elif user[0] == 'phone':
        return phone_func(*user)
    elif user[0] == 'hello':
        return hello_func(*user)
    elif user[0] == 'show' and user[1] == 'all':
        return show_all_func(*user)
    else:
        return "There is no such request"


while True:
    input_user = input('>>>').lower()
    if input_user == 'exit':
        print('Good bye')
        break
    print(main(*input_user.split()))