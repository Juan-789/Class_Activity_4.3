"""
Write a program that takes from the user a number A and B.   Print all numbers from A to B inclusively, in ascending order, if A < B, or in descending order, if A ≥ B.
"""
numA = int(input("Starting Point "))
numB = int(input("Ending point "))
if numA > numB:
  for i in range (numA, numB-1, -1):
    print(i, end = " ")
elif numA < numB:
  for i in range (numA, numB+1, 1):
    print(i, end = " ")
#the IFs decide which input is greater and starts from the greatest, and also changes the step