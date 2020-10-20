"""Jack Reser
This program implements pythons version of switch case
10/19/20"""


def switch_average(my_key):
    switch_case_dict = {'A': 'You entered an A!',
                        'B': 'You entered a B!',
                        'C': 'You entered a C!',
                        'D': 'You entered a D!',
                        'F': 'You entered an F!'}

    result = switch_case_dict.get(my_key, "This is not a valid Grade")
    return result


if __name__ == '__main__':
    print(switch_average('A'))
