first_list = [1, 2, 3, 4, 5]
second_list = [4, 5, 6, 7, 8]


def deduplicate_lists(lst1, lst2, reverse=False):
    new_list = sorted((lst1 + lst2), reverse=reverse)
    for item in new_list:
        if new_list.count(item) > 1:
            new_list.remove(item)
    return new_list


# above is my approach (which is wrong cause im not using fp style)
# the provided solution code is this:
# return sorted(set(lst1 + lst2), reverse=reverse)


print(deduplicate_lists(first_list, second_list, True))
