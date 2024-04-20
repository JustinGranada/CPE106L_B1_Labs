"""Programming Problem 1:

Statisticians would like to have a set of functions to compute the median and mode of a list of numbers. The median is the number that would appear at the 
midpoint of a list if it were sorted. The mode is the number that appears most frequently in the list. Define these functions in a module named stats.py. 
Also include a function named mean, which computes the average of a set of numbers. Each function expects a list of numbers as an argument and returns a 
single number."""


# stats.py

def mean(numbers):
  return sum(numbers) / len(numbers)

def median(numbers):
  sorted_numbers = sorted(numbers)

  n = len(sorted_numbers)

  middle = n // 2

  if n % 2 == 0:

    return (sorted_numbers[middle - 1] + sorted_numbers[middle]) / 2

  else:

    return sorted_numbers[middle]

def mode(numbers):
  frequency = {}

  for number in numbers:

    frequency[number] = frequency.get(number, 0) + 1

  max_frequency = max(frequency.values())

  modes = [number for number, freq in frequency.items() if freq == max_frequency]

  return modes[0] if len(modes) == 1 else modes

if __name__ == "__main__":

  numbers = [1, 3, 3, 4, 5, 5, 5, 7, 9]

  print(f"Mean: {mean(numbers)}")

  print(f"Median: {median(numbers)}")

  print(f"Mode: {mode(numbers)}")
