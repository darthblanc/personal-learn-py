from inheritance_test_parent import Parent


class Child(Parent):
    pass


if __name__ == '__main__':
    x = Child("Bruv")
    x.print_name()
