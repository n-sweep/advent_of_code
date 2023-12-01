NUMS = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']

with open('input.txt', 'r') as f:
    lines = f.read().strip().split('\n')


def find_digit(string, nums):
    ind = len(string)
    result = ''

    for n in nums:
        if n in string:
            i = string.index(n)
            if i < ind:
                ind = i
                result = str(nums.index(n) + 1)

    for char in string:
        if char.isdigit():
            i = string.index(char)
            if i < ind:
                ind = i
                result = char
            break

    return result


def main():
    calibration_values = []
    for line in lines:
        a = find_digit(line, NUMS)
        b = find_digit(line[::-1], [n[::-1] for n in NUMS])
        calibration_values.append(int(a + b))

    s = sum(calibration_values)
    print(s)


if __name__ == '__main__':
    main()
