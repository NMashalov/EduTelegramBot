from itertools import chain
def return_tup(i):
    return (i,i+1)

print(list(chain.from_iterable(return_tup(i) for i in range(10))))