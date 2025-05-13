# File: tests/generate_test_files.py

import os
import random
import string

# Ensure the data directory exists
os.makedirs("tests/data", exist_ok=True)

# Define fixed test cases: filename → content
fixed_test_cases = {
    "a1.txt": "hello",
    "a2.txt": "hello",
    "a3.txt": "hello",
    "b1.txt": "world",
    "b2.txt": "world",
    "c1.txt": "python",
}

# Write fixed test files
for filename, content in fixed_test_cases.items():
    path = os.path.join("tests/data", filename)
    with open(path, "w") as f:
        f.write(content)

# Generate a large sample file with 10,000 random lines
large_sample_path = "tests/data/large_sample.txt"
with open(large_sample_path, "w", encoding="utf-8") as f:
    for _ in range(10000):
        word_length = random.randint(5, 15)
        word = ''.join(random.choices(string.ascii_lowercase, k=word_length))
        f.write(word + "\n")

print("Test files (fixed + large sample) created in 'tests/data/' directory.")