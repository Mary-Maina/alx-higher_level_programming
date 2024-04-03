#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    result = []
    count = 0
    try:
        for i in range(list_length):
            if i < len(my_list_1) and i < len(my_list_2):
                x = my_list_1[i]
                y = my_list_2[i]
                if isinstance(x, (int, float)) and isinstance(y, (int, float)):
                    if y != 0:
                        count = x / y
                        result.append(count)
                    else:
                        result.append(0)
                        print("division by 0")
                else:
                    print("wrong type")
                    count = 0
                    result.append(count)
            else:
                print("out of range")
                count = 0
                result.append(count)
    except ZeroDivisionError:
        print("division by 0")
    finally:
        return result
