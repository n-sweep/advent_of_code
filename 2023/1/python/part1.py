
with open('../data/input.txt', 'r') as f:
    lines = f.read().strip().split('\n')


def get_digits(string):
    for char in string:
        if char.isdigit():
            return char


def main():
    calibration_values = []
    for line in lines:
        first = get_digits(line)
        last = get_digits(line[::-1])

        calibration_values.append(int(first + last))

    print(sum(calibration_values))

if __name__ == '__main__':
    main()
