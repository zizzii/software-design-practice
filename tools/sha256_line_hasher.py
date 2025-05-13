from hashlib import sha256
import matplotlib.pyplot as plt

# Calculates SHA-256 hash code of each unique line of a text file 
def hash_unique_lines(file_path):
    seen_lines = set()
    hash_lines = []
    
    with open(file_path, "r", encoding='utf-8') as f:
        for line in f:
            line = line.strip()
            if line and line not in seen_lines:
                seen_lines.add(line)
                h = sha256(line.encode('utf-8')).hexdigest()
                hash_lines.append(int(h, 16) / (2**256)) # Turn the hash code into numerical values and normalize the hash value

    return hash_lines

if __name__=="__main__":
    hashes = hash_unique_lines("tests/data/large_sample.txt")
    plt.hist(hashes, bins=20, color='skyblue', edgecolor='black')
    plt.show()