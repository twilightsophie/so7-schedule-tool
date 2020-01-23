import argparse
import fileinput
import cmd, sys
import readline


# "-e","--error"

# if args.error:
# with open featureRace as :
#    readlastline()
#    removeLastentry()
# with open database:
#    removeLastLine()
# with open schedule as:
#    readlastline()
#    removeLastentry()

# def removeLastEntry():
#    read lines into set
#    len item in set
#    remove last x in set


# class LoadFromFile (argparse.Action):
#     def __call__(self, parser, namespace, values, option_string=None):
#         with values as f:
#             parser.parse_args(f.read().split(), namespace)
# read file and add arguments to list then call them based on their place in the list?


def convert_arg_line_to_args(arg_line):
    for arg in arg_line.split():
        if not arg.strip():
            continue
        yield arg


def main():
    parser = argparse.ArgumentParser(
        fromfile_prefix_chars='@',
        prog='scratchpad'
    )
    parser.add_argument("-t", "--test",
                        type=str
                        )
    parser.add_argument("-x", "--exam",
                        type=str
                        )
    parser.add_argument("--files", "-f"
                        )
    # parser.convert_arg_line_to_args = convert_arg_line_to_args
    args = parser.parse_args()

    args.files = str(args.files)

    with open(args.files, 'r') as f:
        lines = f.readlines()
        for line in lines:
            args = parser.parse_args(line.split())
            if args.exam == "lovebug":
                print(f"Test = {args.test}")
            else:
                print(f"Exam = {args.exam}")
            continue


if __name__ == "__main__":
    main()
