from PytestLearn.UnitClass.test_unit import Unit


class Login:
    def login_test(self):
        S = Unit().fun_x(2)
        print(S)

if __name__ == '__main__':

    Login().login_test()