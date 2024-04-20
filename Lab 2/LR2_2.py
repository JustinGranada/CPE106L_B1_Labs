def read_file_lines(filename):

  try:
    with open(filename, 'r') as file:
      lines = file.readlines()
    return lines
  except FileNotFoundError:
    print(f"Error: File '{filename}' not found.")
    return []

def print_file_contents(lines):
  num_lines = len(lines)
  print(f"Number of lines in the file: {num_lines}")

  while True:
    try:
      line_number = int(input("Enter a line number (1 to {0}, or 0 to quit): ".format(num_lines)))
      if line_number == 0:

        print("Exiting the program.")

        break
      elif 1 <= line_number <= num_lines:

        print(f"Line {line_number}: {lines[line_number - 1]}")

      else:

        print(f"Invalid line number. Please enter a number between 1 and {num_lines}.")

    except ValueError:

      print("Invalid input. Please enter a valid line number or 0 to quit.")


def main():
  filename = input("Enter the filename: ")
  lines = read_file_lines(filename)

  if lines:
    print_file_contents(lines)

if __name__ == "__main__":
  main()
