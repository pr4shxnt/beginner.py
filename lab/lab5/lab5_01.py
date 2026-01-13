def create_list():
    return ['PlayStation', 'Xbox', 'Steam', 'iOS', 'Google Play']

def get_info(my_list):
    new_list = [my_list[0], my_list[-1], len(my_list)]
    return tuple(new_list)

def get_partial(my_list):
    return my_list[1:5]

def get_last_three(my_list):
    return my_list[-3:]

def double_list(my_list):
    return my_list * 2

def amend(my_list):
    my_list[1] = 'None'
    my_list.append('Bye')
    return my_list


if __name__ == "__main__":
    test_list = create_list()
    print(get_info(test_list))
    print(get_partial(test_list))
    print(get_last_three(test_list))
    print(double_list(test_list))
    print(amend(test_list))