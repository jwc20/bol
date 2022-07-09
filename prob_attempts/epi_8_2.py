from typing import List


def evalulate(rpn: str) -> int:
    intermediate_results: List[int] = []
    delimiter = ","

    operators = {
        "+": lambda y, x: x + y,
        "-": lambda y, x: x - y,
        "*": lambda y, x: x * y,
        "/": lambda y, x: x // y,
    }

    for token in rpn.split(delimiter):
        if token in operators:
            intermediate_results.append(
                operators[token](intermediate_results.pop(), intermediate_results.pop())
            )
            print(intermediate_results)
            print(type(intermediate_results[-1]))
        else:
            intermediate_results.append(int(token))

    return intermediate_results[-1]


print(evalulate("3,4,+,2,*,1,+"))
