def mean(list):
    """Takes a list of integers and returns mean."""
    return sum(list) / len(list)

def standard_deviation(list):
    """Takes a list of integers and returns standard deviation."""
    m = mean(list)
    a = []
    for num in list:
        a.append((num-m)**2)

    return sum(a) / (len(list)-1)

def median(list):
    """Takes a list of integers and returns median."""
    list.sort()
    if len(list) % 2 == 0:
        mid = len(list) / 2
        s = list[mid-1] + list[mid]
        return s / 2
    else:
        mid = int(len(list) / 2)
        return list[mid] / 2

def mode(list):
    """Takes a list of integers and returns mode."""
    list.sort()
    c = 0
    mod = 0
    for num in list:
        if c < list.count(num):
            c = list.count(num)
            mod = num
    if c > 1:
        return mod
    else:
        return "No mode"