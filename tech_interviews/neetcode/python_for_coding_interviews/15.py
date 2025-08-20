"""
List clone
"""

import copy

original_list = [[1, 2], [3, 4]]
shallow_cloned_list = list(original_list)
deep_cloned_list = copy.deepcopy(original_list)


original_list[0][1] = 3

print("shallow: ", shallow_cloned_list)
print("deep: ", deep_cloned_list)
