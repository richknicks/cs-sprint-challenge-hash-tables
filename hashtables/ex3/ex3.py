def intersection(arrays):
    """
    YOUR CODE HERE
    """
    # Your code here

    cache = {}

    total = len(arrays)
    result = []

    i = 0
    for array in arrays:
        for item in array:
            if item not in cache:
                if i == 0:
                    cache[item] = 1
                else:
                    continue
            else:
                cache[item] += 1
        i += 1

    for pair in cache:
        if cache[pair] == total:
            result.append(pair)

    return result


if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection(arrays))
