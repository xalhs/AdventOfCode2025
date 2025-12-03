# Advent of Code 2025
These are my scripts for the puzzles at https://adventofcode.com/2025 . Same as the previous years, I will be uploading all days that I solve with a short commentary on thought process/description. All the puzzles (so far) have been solved without looking up any hint related to the event. Note that my naming process for the input texts is input + the date. So for the first day it was input1.txt, the second day input2.txt... etc.

## Day 1
Again, the first days are generally easy, so I didn't expect much. Part 1 was about keeping track of a position, using a little modular arithmetic. Part 2 just needed to calculate the number of turns as well after each command, with some caution for edge cases to not double count or miscount

## Day 2
Day 2 was fairly easy too. In fact I misread the prompt and did wrote the code for part 2 before I finished part 1. Part 1 was basically about splitting the words in half and seeing if those halves match. In part 2, I reinvented the wheel and wrote a function to find the divisors of numbers instead of grabbing a ready made one. Then checked the "sub-strings" of length corresponding to divisors of the length of the full string to see if the full string is made out of copies of those sub-strings. Small note for edge cases where the full string was of length "1". 

## Day 3
Day 3 didn't have anything special either. For part 1, you needed to find the largest concatenation of 2 digits inside a multi digit string. You just had to realize that you need to search the entire string minus the last character to find the first digit, and then from the first digit to the end to find the second digit. For part 2, you had to find the largest concatenation of 12 digits this time. The logic was the same though, you search the entire string minus the last 11 characters for the first digit, then from the first digit up until 10 characters before the end for the second digit, and so on...
