#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    index = 0
    div_result = 0
    result = []
    while (index < list_length):
        try:
            num1 = convert_to_int_or_float(my_list_1[index])
            num2 = convert_to_int_or_float(my_list_2[index])
            div_result = num1 / num2
        except IndexError:
            print("out of range")
        except ValueError:
            print("wrong type")
        except ZeroDivisionError:
            print("division by zero")
        except BaseException:
            print("wrong type")
        finally:
            result.append(div_result)
            div_result = 0
            index += 1
    return result


def convert_to_int_or_float(input_str):
    if (isinstance(input_str, int)):
        return int(input_str)
    elif (isinstance(input_str, float)):
        return float(input_str)
    raise ValueError
