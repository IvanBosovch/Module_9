def input_error(func):
    def inner(*user):
        try:
            return func(*user)
        except IndexError:
            return "Not enough params"
    return inner


dict_phone = {}

@input_error
def main(*user):
    if user[0] == 'add':
        dict_phone.setdefault(user[1], user[2])
    elif user[0] == 'change':
        dict_phone[user[1]] = user[2]
    elif user[0] == 'phone':
        print(dict_phone.get(user[1]))
    elif user[0] == 'hello':
        print('"How can I help you?')
    elif user[0] == 'show' and user[1] == 'all':
        print(dict_phone)
    else:
        print('Not enough param')
    

while True:
    input_user = input('>>>')
    if input_user == 'exit':
        print('Good bye')
        break
    main(*input_user.split())