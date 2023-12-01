from python import Python
from sys import argv


fn get_data(filepath: StringLiteral) raises -> String:
    # avoid warning bug by creating data variable before reading file
    # https://github.com/modularml/mojo/issues/1166
    var data = String('')
    with open(filepath, 'r') as f:
        data = f.read().replace('\n', '')
    return data


fn process(text: String) raises -> Int:
    var floor = 0

    for i in range(len(text)):
        let d = text[i]
        if d == '(':
            floor +=1
        elif d == ')':
            floor -=1

    return floor


#fn test() raises:
#    print('hi mom')
#    let data = get_data()
#    let sol = process(data)
#    print(sol)


fn main() raises:
    try:
        let os = Python.import_module('os')
        let file = argv()[0]
        let dr = os.path.dirname(file)
        var fp = ''
        if dr:
            let par = os.path.join(dr, '..')
            fp = String(os.path.abspath(par))
        else:
            let par = os.path.abspath('..')
            fp = String(os.path.abspath('.'))
        print(fp)
    except:
        print('cannot import os.path')

