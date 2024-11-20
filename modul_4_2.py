
def test_functio():
    def inner_function():
        print('Я в области видимости функции test_function')
    print(inner_function())
print(test_functio())
print(inner_function())