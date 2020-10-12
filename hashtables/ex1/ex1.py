def get_indices_of_item_weights(weights, length, limit):
    """
    Given a package with a weight limit `limit` and a list `weights` of item
    weights, implement a function `get_indices_of_item_weights` that finds
    two items whose sum of weights equals the weight limit `limit`. Your
    function will return a tuple of integers that has the following form:

    ```
    (zero, one)
    ```

    where each element represents the item weights of the two packages.
    _**The higher valued index should be placed in the `zeroth` index and
    the smaller index should be placed in the `first` index.**_ If such a
    pair doesn’t exist for the given inputs, your function should return
    `None`.

    Your solution should run in linear time.

    Example:
    ```
    input: weights = [ 4, 6, 10, 15, 16 ], length = 5, limit = 21
    output: [ 3, 1 ]  # since these are the indices of weights 15 and 6 whose sum equals 21
    ```
    YOUR CODE HERE
    """
    # Your code here
    # fine two items with sum of weighs equal weight limit
    
    # * What if we store each weight in the input list as keys? What would be
    # a useful thing to store as the value for each key? 
    cache = {}

    # each element represents items weights
    for i in range(length):
        cache[weights[i]] = i

    for j in range(length):
        """
         If we store each weight's list index as its value, we can then check
        to see if the hash table contains an entry for `limit - weight`. If it
        does, then we've found the two items whose weights sum up to the
        """
        value = limit - weights[j]

        if value in cache:
            return(max(j, cache[value]), min(j, cache[value]))


    return None
