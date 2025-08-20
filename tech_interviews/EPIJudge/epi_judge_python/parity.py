from test_framework import generic_test


def parity(x: int) -> int:

    # input: integer, not binary 
    # output: 1 or 0

    # set count = 0
    # use loop 
        # check the binary of x 
        # if the rightmost bit is 1 
            # count+=1
    # if count is odd, return 1 
    # else, return 0

    count = 0
    while x:
        if (x & 1 == 1): 
            count += 1
            x >>= 1
        x >>= 1
    if (count % 2 == 1): 
        return 1
    return 0

if __name__ == '__main__':
    exit(generic_test.generic_test_main('parity.py', 'parity.tsv', parity))
