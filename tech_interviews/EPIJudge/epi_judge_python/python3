from test_framework import generic_test
from pprint import pprint


def ss_decode_col_id(col: str) -> int:

    # solution from leetcode 171
    res = 0 
    val = [i for i in range(1, 27)]
    letters = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    d = dict(zip(letters, val))
    pprint(d)
    for char in col:
        res = res * 26 + d[char]
    return res

print(ss_decode_col_id("ABC"))


'''
if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('spreadsheet_encoding.py',
                                       'spreadsheet_encoding.tsv',
                                       ss_decode_col_id))
        '''
