from functools import cmp_to_key

def comparator(a, b):
    """
    sort comparator.
    for asending sort, return:-
        1, 0, -1 for a>b, a = b, a<b respectively
    for descending sort, return:-
        -1, 0, 1 for a>b, a = b, a<b respectively
    """
    if a[0] == b[0]:
        if a[1] > b[1]:
            return 1
        else:
            return -1
    else:
        return b[0] - a[0]


def reconstructor_fn(queue):
    queue = sorted(queue, key = cmp_to_key(comparator))
    new_queue = []
    for i in range(0, len(queue)):
        new_queue.insert(queue[i][1], queue[i])
    return new_queue


# driver code
if __name__=="__main__":
    input_queue = [[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]]
    output_queue = reconstructor_fn(input_queue)
    print(output_queue)