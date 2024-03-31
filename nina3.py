class Test():
    def public_func(self):
        print ('публичный метод')

    # Создаем защищённый метод (одно нижнее подчёркивание):
    def _protected_func(self):
        print ('защищенный метод')

    # Создаем приватный метод. Он будет работать только если его вызывать внутри данного класса, то есть работать он в других функциях, но только внутри данного класса.
    def __private_func(self):
        print ('приватный метод')

    def test_private(self):
        self.__private_func()

test = Test()

test.public_func()

test._protected_func()

test.test_private()