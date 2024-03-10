test_list = [1, 5, 3, 6, 3, 5, 6, 1]
unique_list = list(set(test_list))
print("The list after removing duplicates:", unique_list)


test_list = [1, 5, 3, 6, 3, 5, 6, 1]
res = [i for n, i in enumerate(test_list) if i not in test_list[:n]]
print("The list after removing duplicates:", res)


from collections import OrderedDict
test_list = [1, 5, 3, 6, 3, 5, 6, 1]
res = list(OrderedDict.fromkeys(test_list))
print("The list after removing duplicates:", res)

