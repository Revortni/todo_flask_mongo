
def fib_gen(limit):
    mapper = [0, 1]
    count = len(mapper)

    while (mapper[count-1] < limit):
        mapper.append(mapper[count-1]+mapper[count-2])
        count = count+1
        yield mapper[count-2]


result = [val for val in fib_gen(100)]
