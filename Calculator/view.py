class View:
    """
    Весь визуал тут
    """

    def __init__(self, controller):
        self.controller = controller

    def main(self):
        print("Welcome to calculator\n\n")

    def choose_operation(self):
        user_input = input("Working with:\n1 - rational\n2 - complex\n0 - exit\n\n~: ")
        match user_input:
            case "1":
                return self.controller.main_select(user_input)
            case "2":
                return self.controller.main_select(user_input)
            case "0":
                return self.controller.main_select(user_input)
            case _:
                print("Error")

    def operations(self, selected_operation):
        user_input = input(
            "Opertions:\n"
            "1 - sum\n"
            "2 - sub\n"
            "3 - mul\n"
            "4 - div\n"
            "5 - pow - only for simple\n"
            "6 - sqrt - only for simple\n"
            "0 - previous menu\n\n"
            "~: ")
        match selected_operation:
            case "1":
                return self.controller.simple_number(user_input)
            case "2":
                return self.controller.complex_number(user_input)

    def input_numbers(self):
        num_1 = input("Enter First Number: ")
        num_2 = input("Enter Second Number: ")
        return num_1, num_2

    def answer(self, answer: tuple):
        return print(answer)
