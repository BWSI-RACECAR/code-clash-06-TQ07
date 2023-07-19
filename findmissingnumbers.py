"""
Copyright MIT BWSI Autonomous RACECAR Course
MIT License
Summer 2023

Code Clash #6 - WHERE ARE MY NUMBERS!? (findmissingnumbers.py)


Author: Ali Qattan

Difficulty Level: 6/10

Prompt: The Grand Prix was about to begin. The track was set, 
the cars were revved up, and the anticipation filled the air. 
As the race officials prepared for the event, they encountered a
problem that needed to be solved. The challenge was to analyze a list 
of numbers that represented checkpoints along the race track. 

These numbers were supposed to be in a specific sequence, but it 
seemed that some were missing. The officials needed to identify those
missing numbers before the race could commence.
Given a list of numbers that are in sequence, find the numbers missing in 
the sequence and output those numbers. You may assume the following:

1. The number sequence will NOT contain negatives.
2. The number sequence will NOT always start with the 
lowest value of the sequence and the last number in the sequence will
NOT always be the highest value in the sequence.
3. The numbers missing will always be in between the lowest value
and the highest values.
4. It matters not if numbers repeat or if they are scrambled, 
your duty is to find the numbers missing in betwixt the lowest and the highest
denary values. There may be floats.
5. If list is empty, output “Invalid input”
6. If list has only one number, output “None missing”

Test Cases: 
Input: [1, 2, 3, 5, 6]  Output: [4]

Input: [3, 4, 2, 1, 6, 7, 5, 9, 10] Output:[8]

Input: [3, 3, 3, 3, 4, 7] Output: [5, 6]

"""
"""
Copyright MIT BWSI Autonomous RACECAR Course
MIT License
Summer 2023

Code Clash #6 - WHERE ARE MY NUMBERS!? (findmissingnumbers.py)


Author: Ali Qattan

Difficulty Level: 6/10

Prompt: The Grand Prix was about to begin. The track was set, 
the cars were revved up, and the anticipation filled the air. 
As the race officials prepared for the event, they encountered a
problem that needed to be solved. The challenge was to analyze a list 
of numbers that represented checkpoints along the race track. 

These numbers were supposed to be in a specific sequence, but it 
seemed that some were missing. The officials needed to identify those
missing numbers before the race could commence.
Given a list of numbers that are in sequence, find the numbers missing in 
the sequence and output those numbers. You may assume the following:

1. The number sequence will NOT contain negatives.
2. The number sequence will NOT always start with the 
lowest value of the sequence and the last number in the sequence will
NOT always be the highest value in the sequence.
3. The numbers missing will always be in between the lowest value
and the highest values.
4. It matters not if numbers repeat or if they are scrambled, 
your duty is to find the numbers missing in betwixt the lowest and the highest
denary values. There may be floats.
5. If list is empty, output “Invalid input”
6. If list has only one number, output “None missing”

Test Cases: 
Input: [1, 2, 3, 5, 6]  Output: [4]

Input: [3, 4, 2, 1, 6, 7, 5, 9, 10] Output:[8]

Input: [3, 3, 3, 3, 4, 7] Output: [5, 6]

"""
class Solution:
    def findMissingNumbers(self, numbers):
        # type numbers: list of float
        # return type: list of int

        # Check for invalid input
        if not numbers:
            return "Invalid input"
        if len(numbers) == 1:
            return "None missing"

        # Find the minimum and maximum values in the list
        min_val = min(numbers)
        max_val = max(numbers)

        # Create a set of all the numbers in the sequence
        all_numbers = set(range(int(min_val), int(max_val) + 1))

        # Find the missing numbers by subtracting the set of given numbers from the set of all numbers
        missing_numbers = list(all_numbers - set(map(int, numbers)))

        return missing_numbers
    



def main():
    array = input().split(" ")
    for x in range (0, len(array)):
        array[x] = float(array[x])

    tc1 = Solution()
    ans = tc1.findMissingNumbers(array)
    print(ans)

if __name__ == "__main__":
    main()
    
#listOfNumbers = [0, 3, 3, 3, 4, 7, 3]  # STEP 1: get the in input
#print(findMissingNumbers(listOfNumbers)) # Step 2: Call a function to handle the input
    
#listOfNumbers = [0, 3, 3, 3, 4, 7, 3]  # STEP 1: get the in input
#print(findMissingNumbers(listOfNumbers)) # Step 2: Call a function to handle the input
