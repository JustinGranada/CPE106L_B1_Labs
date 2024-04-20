from collection import number 

def mean(numbers):
  if not numbers:
    return 0
    
  return sum(numbers) / len(numbers)

def median(numbers):
  if not numbers: 
    return 0
    sorted_numbers = sorted(numbers)
