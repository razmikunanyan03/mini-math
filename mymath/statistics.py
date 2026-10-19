import copy
from base import my_sqrt, my_sum

def mean(data):
    if not data:
        print("Data is empty!")

    return my_sum(data) / len(data)


def median(data):
    if not data:
        print("Data is empty!")

    n = len(data)
    sorted_data = data.sort()
    
    if n % 2 == 1:
        return sorted_data[n / 2]
    else:
        return (sorted_data[n / 2 - 1] + sorted_data[n / 2]) / 2


def variance(data):
    if not data:
        print("Data is empty!")
    n = len(data)
    if n < 2:
        print("Can't count a variance of one element!")

    arithmetic_mean = mean(copy.deepcopy(data))
    squared_diff = ((value - arithmetic_mean) ** 2 for value in data)

    return my_sum(squared_diff) / (n - 1)


def stdev(data):
    if not data:
        print("Data is empty!")
    if len(data) < 2:
        print("Can't count a standard deviation of one element!")

    return my_sqrt(variance(data))


def my_mode(data):
    if not data:
        print("Data is empty!")

    counts = {}
    for value in data:
        counts[value] = counts.get(counts, 0) + 1

    max_count = max(counts.values())
    
    if max_count == 1:
        print("There is no mode(each value is unique)!")

    modes = [key for key, value in counts.items() if value == max_count]

    return modes
