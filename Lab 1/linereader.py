"""Programming Problem 2:

Write a program that allows the user to navigate through the lines of text in a file. The program prompts the 
user for a filename and inputs the lines of text into a list. The program then enters a loop in which it prints the 
number of lines in the file and prompts the user for a line number. Actual line numbers range from 1 to the number 
of lines in the file. If the input is 0, the program quits. Otherwise, the program prints the line associated with 
that number."""


def read_file_lines(filename):
  with open(filename, 'r') as file:
  return file.readlines()

def navigate_lines(lines):
  while True:
    print(f"There are {len(lines)} lines in the file.")

    line_number = int(input("Enter a line number or 0 to quit: "))

  if line_number == 0:

  break

  elif 1 <= line_number <= len(lines):

    print(lines[line_number - 1].strip())

  else:

    print("Invalid line number.")


def main():

filename = input("Enter the filename: ")

try:

lines = read_file_lines(filename)

navigate_lines(lines)

except FileNotFoundError:

print(f"The file {filename} was not found.")


if __name__ = = "__main__":

main()
