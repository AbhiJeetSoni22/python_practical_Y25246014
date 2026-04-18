# Q17: Copy contents of one file to another after removing digits

# Function to remove digits and copy content
def copy_without_digits(source_file, destination_file):
    # Open source file in read mode
    with open(source_file, 'r') as src:
        content = src.read()

    # Remove digits from content
    filtered_content = ""
    for ch in content:
        if not ch.isdigit():  # keep only non-digit characters
            filtered_content += ch

    # Write filtered content to destination file
    with open(destination_file, 'w') as dest:
        dest.write(filtered_content)


# ---- Main Execution ----
source = "sample.txt"
destination = "output.txt"

copy_without_digits(source, destination)

print("File copied successfully without digits!")