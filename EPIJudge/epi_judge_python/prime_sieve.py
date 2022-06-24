from typing import List

from test_framework import generic_test


# Given n, return all primes up to and including n.
def generate_primes(n: int) -> List[int]:
    # TODO - you fill in here.
    if n <= 1:
        return []

    result = []
    
    comp = n
    for m in reversed(range(1,n)):
        print(m)
        if comp % m != 0:
            result.append(m)
            comp = m

    print(result)
    return result

generate_primes(18)



if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('prime_sieve.py', 'prime_sieve.tsv',
                                       generate_primes))
