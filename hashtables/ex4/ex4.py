def has_negatives(a):
    """
    YOUR CODE HERE
    """
    # Your code here

    cache = {}
    result = []
    for i in a:
        if abs(i) not in cache:
            cache[abs(i)] = 1
        else:
            cache[abs(i)] += 1

    for pair in cache:
        if cache[pair] > 1:
            result.append(pair)

    return result


if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
