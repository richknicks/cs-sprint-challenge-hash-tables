def get_indices_of_item_weights(weights, length, limit):
    """
    YOUR CODE HERE
    """
    # Your code here

    cache = {}
    for i in range(length):
        if weights[i] not in cache:
            cache[weights[i]] = [i]
        else:
            cache[weights[i]].append(i)

    for weight in weights:
        pair = limit - weight
        if pair not in cache:
            continue
        elif pair == weight:
            return [cache[weight][1], cache[weight][0]]
        else:
            if cache[weight] > cache[pair]:
                return [cache[weight][0], cache[pair][0]]
            else:
                return [cache[pair][0], cache[weight][0]]
    return None

