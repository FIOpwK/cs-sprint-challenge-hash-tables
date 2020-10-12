def intersection(arrays):
    """
    YOUR CODE HERE
    """
    # Your code here
    cache = {}
    result = []

    length_of_lists = len(arrays)

    for list_of_integers in arrays:
        for integer in list_of_integers:
            if integer in cache:
                cache[integer] += 1
            else:
                cache[integer] = 1

            if cache[integer] == length_of_lists:
                result.append(integer)

    return resul


if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection(arrays))
