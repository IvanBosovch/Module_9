def input_error(func):
    def inner(*user):
        try:
            return func(*user)
        except IndexError:
            return "Give me name and phone please" 
    return inner

dict_phone = {}

@input_error
def main(*user):
    if user[0] == 'add':
        dict_phone.setdefault(user[1], user[2])
    elif user[0] == 'change':
        dict_phone[user[1]] = user[2]
    elif user[0] == 'phone':
        if user[1] in dict_phone:
            return dict_phone.get(user[1])
        else:
            return 'Not user'
    elif user[0] == 'hello':
        return '"How can I help you?'
    elif user[0] == 'show' and user[1] == 'all':
        return dict_phone
    else:
        return "There is no such request"
    
while True:
    input_user = input('>>>').lower()
    if input_user == 'exit':
        print('Good bye')
        break
    print(main(*input_user.split()))