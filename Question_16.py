# Q16: Read a file and count number of lines, words, and characters

# Function to count lines, words, and characters
def analyze_file(filename):
    lines = 0
    words = 0
    characters = 0

    # Open file in read mode
    with open(filename, 'r') as file:
        for line in file:
            lines += 1                          # Count lines
            words += len(line.split())          # Count words
            characters += len(line)             # Count characters (including spaces)

    return lines, words, characters


# ---- Main Execution ----
filename = "sample.txt"   # make sure this file exists in same folder

lines, words, chars = analyze_file(filename)

print("Number of lines:", lines)
print("Number of words:", words)
print("Number of characters:", chars)