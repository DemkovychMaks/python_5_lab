import re
from pprint import pprint


def main():
    log_file = "/Users/maksdemkovych/Desktop/python_5_lab/log.txt"
    count = 0

    with open(log_file, mode="r") as file:
        text = file.read()
        result1 = re.findall(r'\[\d\d/\w*/\d\d\d\d:10:[0-5]\d:[0-5]\d \+0100] "POST /\w*/\w*\.\w* \w*/\d\.\d" [4\d\d\-5\d\d]', text)
        result2 = re.findall(r'\[\d\d/\w*/\d\d\d\d:10:[0-5]\d:[0-5]\d \+0100] "POST \w*://\w*\.\w*\.\w*/\w*-\w*/\w*\.\w* \w*/\d\.\d" [4\d\d\-5\d\d]', text)

    result = []
    result.extend(result1)
    result.extend(result2)


    for item in result:
        count += 1
        result.sort()

    print(f"Unaccomplished POST requests: {count}")
    pprint(result)


if __name__ == '__main__':
    main()
