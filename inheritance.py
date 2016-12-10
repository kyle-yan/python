class Parent():

    def print_last_name(self):
        print('Yan')


class Child():

    def print_first_name(self):
        print('Kai')


class Name(Parent, Child):
    pass

    # def print_last_name(self):
    #     print('Chen')

kai = Name()
kai.print_first_name()
kai.print_last_name()
