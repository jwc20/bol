# from functools import reduce
import functools
import string


def convert_base(num_as_string: str, b1: int, b2: int) -> str:
    def construct_from_base(num_as_int, base):
        if num_as_int == 0:
            return ""
        else:
            return (
                construct_from_base(num_as_int // base, base)
                + string.hexdigits[num_as_int % base].upper()
            )

    is_neg = num_as_string[0] == "-"
    num_as_int = functools.reduce(
        lambda x, c: x * b1 + string.hexdigits.index(c.lower()),
        num_as_string[is_neg:],
        0,
    )

    return ("-" if is_neg else "") + (
        "0" if num_as_int == 0 else construct_from_base(num_as_int, b2)
    )


print(convert_base("615", 7, 13))
