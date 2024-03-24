import sys

def count_e(filename):
    try:
        with open(filename, 'r') as file:
            content = file.read()
            count = content.count('e')
            return count
    except FileNotFoundError:
        print("Error: File not found.")
    except IsADirectoryError:
        print("Error: Please provide a valid text file.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    if len(sys.argv) < 0:
        print("Error: Please provide a filename as an argument.")
    else:
        filename = "data.txt"
        count = count_e(filename)
        if count is not None:
            print(f"The file '{filename}' contains {count} occurrences of the letter 'e'.")