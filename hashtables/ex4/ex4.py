def has_negatives(a):
    """
    YOUR CODE HERE
    """
    # Your code here
    cache = {}
    result = []

    for n in a:
        if cache.get(abs(n)) is not None:
            result.append(abs(n))
        else:
            cache[abs(n)] = abs(n)

    return result


if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
