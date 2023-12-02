fn load_data(filepath: String) raises -> String:
    var input_file = open(filepath, 'r')
    let data = input_file.read()

    input_file.close()

    return data

fn split(s: String, char: String = '\n') -> object:
    let lines  = object([])
    var j = 0
    for i in range(len(s)):
        if s[i] == char:
            object(s[j:i])
            lines.append(out)
            j = i

    return lines

fn main() raises:
    let fp = '../data/test_1.txt'
    let s = load_data(fp)
    print(split(s))
