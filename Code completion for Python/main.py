import argparse
import os


def find_literals(line: str) -> list[str]:
    literals = []
    i = 0
    while i < len(line):
        if line[i] == "'":
            left_border = i
            i += 1
            while line[i] != "'":
                i += 1
                if i < len(line) - 1 and line[i:i + 2] == r"\'":
                    i += 2
            right_border = i
            literals.append(line[left_border + 1: right_border])
        if line[i] == '"':
            left_border = i
            i += 1
            while line[i] != '"':
                i += 1
                if i < len(line) - 1 and line[i:i + 2] == r"\"":
                    i += 2
            right_border = i
            literals.append(line[left_border + 1: right_border])
        i += 1
    return literals


def get_arg() -> str:
    parser = argparse.ArgumentParser()
    parser.add_argument("file_path", help="")
    args = parser.parse_args()
    return args.file_path


def main():
    file_path = get_arg()
    literal_and_line_indexes = {}
    if not os.path.isfile(file_path):
        print(f"Error: no such file: '{file_path}'")
    else:
        with open(file_path, 'r') as f:
            for line_number, line in enumerate(f.readlines()):
                line_literals = find_literals(line)

                for literal in line_literals:
                    if literal in literal_and_line_indexes:
                        literal_and_line_indexes[literal].append(line_number)
                    else:
                        literal_and_line_indexes[literal] = [line_number]

        for literal, lines in literal_and_line_indexes.items():
            if len(lines) > 1:
                print(f"Lines with '{literal}': {', '.join(map(str, set(lines)))}")


if __name__ == "__main__":
    main()
