from math import sqrt
from logg import logging


class Model:
    """
    Вся логика тут
    """

    def __init__(self):
        pass

    def simple_operations(self, numbers, selected_operation):
        num_1, num_2 = numbers
        try:
            float(num_1)
            float(num_2)
        except ValueError:
            logging.error("ValueError")
            exit(ValueError)
        else:
            num_1 = float(num_1)
            num_2 = float(num_2)
        match selected_operation:
            case "1":
                return num_1 + num_2
            case "2":
                return num_1 - num_2
            case "3":
                return num_1 * num_2
            case "4":
                try:
                    num_1 / num_2
                except ZeroDivisionError:
                    logging.error("ZeroDivisionError")
                else:
                    return num_1 / num_2
            case "5":
                return pow(num_1, int(num_2))
            case "6":
                return sqrt(num_1), sqrt(num_2)
            case _:
                print("Error")

    def complex_opertions(self, numbers, selected_operation):
        (num_1, num_2) = numbers
        match selected_operation:
            case "1":
                return complex(num_1) + complex(num_2)
            case "2":
                return complex(num_1) - complex(num_2)
            case "3":
                return complex(num_1) * complex(num_2)
            case "4":
                try:
                    complex(num_1) / complex(num_2)
                except ZeroDivisionError:
                    logging.error("ZeroDivisionError")
                else:
                    return complex(num_1) / complex(num_2)
            case "5":
                print("Can't take action")
                return
            case "6":
                print("Can't take action")
                return
            case _:
                print("Error")
