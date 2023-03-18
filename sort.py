def extract_age(item):
    return item[1][1]


def sort_dictionary(dictionary):
    sorted_dict = sorted(dictionary.items(), key=extract_age)
    result = [(name, phone) for name, (phone, age) in sorted_dict]
    return result


example_input = {'Tom': (5464512, 24), 'Sara': (
    5446987, 32), 'Mary': (1557896, 20)}
result = sort_dictionary(example_input)
print(result)
