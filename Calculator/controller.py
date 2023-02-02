from model import Model
from view import View
from logg import logging


class Controller:
    """
    Связываем логику и визуал тут
    """

    def __init__(self):
        self.view = View(self)
        self.model = Model()

    def main(self):
        self.view.main()
        self.view.choose_operation()

    def main_select(self, selected_operation):
        match selected_operation:
            case "1":
                logging.info("Chosen simple numbers")
                self.view.operations(selected_operation)

            case "2":
                logging.info("Chosen complex numbers")
                self.view.operations(selected_operation)
            case "0":
                logging.info("Close program")
                exit()
            case _:
                logging.warning("Enter something wrong")
                print("Error")

    def simple_number(self, selected_operation):
        match selected_operation:
            case "0":
                self.view.choose_operation()
            case _:
                return self.view.answer(self.model.simple_operations(self.view.input_numbers(), selected_operation))

    def complex_number(self, selected_operation):
        match selected_operation:
            case "0":
                self.view.choose_operation()
            case _:
                return self.view.answer(self.model.complex_opertions(self.view.input_numbers(), selected_operation))
