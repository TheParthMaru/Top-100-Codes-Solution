## Leap year

**Problem Statement**

- Take an integer input as year and check if it is a leap year or not.

**Test Cases**

```
Input: 2016
Output: Leap year

Input: 2022
Output: Not a leap year

Input: 1998
Output: Not a leap year
```

**Code**

```py
year = int(input())

if (year % 4 == 0) and (year % 100 != 0) or (year % 400 == 0):
    print("Leap year")
else:
    print("Not a leap year")
```