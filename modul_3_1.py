# счетчик вызовов
calls = 0
def count_calls():
    def strig_info(string):
        global calls
        calls = calls + 1
        a = len(string)
        b = string.upper()
        c = string.lower()
        return (a, b, c)

    print(strig_info(string ='bananas'))
    print(strig_info(string='Capybara'))

    def is_contains(string, list_to_search):
        global calls
        calls = calls + 1
        new_list = [a.lower() for a in list_to_search]
        if string.lower() in new_list:
            return True
        else:
            return False

    print(is_contains(string='Urban', list_to_search=['banan', 'urban', 'ban']))
    print(is_contains(string='Arba', list_to_search=['banan', 'urban', 'ban']))
    return calls


print(count_calls())
