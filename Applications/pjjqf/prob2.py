
from collections import Counter

def find_unique_numbers(numbers):
    freq = Counter(numbers)
    #ix_list = np.bincount(numbers)
    #return [numbers[x] for x in ix_list if x ==1]
    #return set(numbers)

if __name__ == "__main__":
    print(find_unique_numbers([1, 2, 1, 3]))