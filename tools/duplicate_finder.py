import sys
from hashlib import sha256

# find duplicates (literally the function name, duh)
def find_duplicates(filenames):
    matches = []
    for i_left in range(len(filenames)):
        left = filenames[i_left]
        for i_right in range(i_left):
            right = filenames[i_right]
            if same_byte(left,right):
                matches.append((left,right))
    return matches

# read two file and compare them byte by byte
def same_byte(left,right):
    left_bytes = open(left, "rb").read()
    right_bytes = open(right, "rb").read()
    return left_bytes == right_bytes


# Naive implementation of hash function
def naive_hash(data):
    return sum(data) % 13

# Build a dictionary that has hash codes as key and set of filenames as values
def find_groups1(filenames):
    groups = {}
    for fn in filenames:
        data = open(fn, "rb").read()
        hash_code = naive_hash(data)
        if hash_code not in groups:
            groups[hash_code] = set()
        groups[hash_code].add(fn)
    return groups

# Build a dictionary that has sha256 hash codes as key and set of filenames as values
def find_groups(filenames):
    groups = {}
    for fn in filenames:
        data = open(fn, "rb").read()
        hash_code = sha256(data).hexdigest()
        if hash_code not in groups:
            groups[hash_code] = set()
        groups[hash_code].add(fn)
    return groups


if __name__=="__main__":
    groups = find_groups(sys.argv[1:])
    for filename in groups.values():
        print(",".join(sorted(filename)))