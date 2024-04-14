def is_leap(yr):
    return yr % 4 == 0 and (yr % 100 != 0 or yr % 400 == 0)
# Example
yr = 2020
if is_leap(yr):
    print("The year {} is a leap year".format(yr))
else:
    print("The year {} is not a leap year".format(yr))