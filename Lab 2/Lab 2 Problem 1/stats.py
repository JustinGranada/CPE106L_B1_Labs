
def mode(numbers):
    if not numbers:
        return 0
    
    words = [str(number).upper() for number in numbers]
    theDictionary = {}
    for word in words:
        number = theDictionary.get(word, None)
        if number == None:
            theDictionary[word] = 1
        else:
            theDictionary[word] = number + 1

    theMaximum = max(theDictionary.values())
    modes = [key for key in theDictionary if theDictionary[key] == theMaximum]
    return modes[0] if len(modes) == 1 else "No unique mode"

def median(numbers):
    if not numbers:
        return 0
    
    numbers.sort()
    midpoint = len(numbers) // 2
    if len(numbers) % 2 == 1:
        return numbers[midpoint]
    else:
        return (numbers[midpoint] + numbers[midpoint - 1]) / 2

def mean(numbers):
    if not numbers:
        return 0
    
    return sum(numbers) / len(numbers)

def main():
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print(f"List: {numbers}")
    print(f"Mean: {mean(numbers)}")
    print(f"Median: {median(numbers)}")
    print(f"Mode: {mode(numbers)}")

if __name__ == "__main__":
    main()
