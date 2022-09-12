#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    index = 0
    div_result = 0
    result = []
    while (index < list_length):
        try:
            div_result = int(my_list_1[index]) / int(my_list_2[index])
        except IndexError:
            print("out of range")
        except ValueError:
            print("wrong type")
        except ZeroDivisionError:
            print("division by zero")
        finally:
            result.append(div_result)
            div_result = 0
            index += 1
    return result
