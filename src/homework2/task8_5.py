#   7 kyu
# Highest and Lowest

# In this little assignment you are given a string of
# space separated numbers, and have to return the highest and lowest number.
# Example:
# high_and_low("1 2 3 4 5")  # return "5 1"
# high_and_low("1 2 -3 4 5") # return "5 -3"
# high_and_low("1 9 3 4 -5") # return "9 -5"
# Notes:
# All numbers are valid Int32, no need to validate them.
# There will always be at least one number in the input string.
# Output string must be two numbers separated by a single space, and highest number is first.


def high_and_low(numbers):
    len_num = len(numbers)
    num_new = []
    i = 0
    while i < len_num:
        num_int = ''
        a = numbers[i]
        while '0' <= a <= '9':
            num_int += a
            i += 1
            if i < len_num:
                a = numbers[i]
            else:
                break
        i += 1
        if num_int != '':
            num_new.append(int(num_int))
    numbers = str(max(num_new)) + " " + str(min(num_new))
    return numbers


print(high_and_low("1 2 3 4 5"))
