def skip_elements(elements):
    result = []
    for index,number in enumerate(elements):
        if index % 2 == 0:
            result.append(number)
    return result


print(skip_elements(["a", "b", "c", "d", "e", "f", "g"]))
