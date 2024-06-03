def longest_name(file):
    """
    Prints the longest name from the given file.

    :param file: The path to the file containing names
    :type file: str
    """
    print(max((line.strip() for line in open(file, 'r')), key=len))
    # In case you have more than one name in the same line you can do the following
    # print(max((name for line in open(file, 'r') for name in line.split()), key=len))


def total_len(file):
    """
    Prints the total length of all names in the given file.

    :param file: The path to the file containing names
    :type file: str
    """
    print(sum(len(name) for line in open(file, 'r') for name in line.split()))


def shortest_name(file):
    """
    Prints the shortest name(s) from the given file.

    :param file: The path to the file containing names
    :type file: str
    """
    names = [line.strip() for line in open(file, 'r')]
    min_len = min(map(len, names))
    print('\n'.join(name for name in names if len(name) == min_len))
    # You can also do it shorter in 2 lines
    # names = [line.strip() for line in open(file, 'r')]
    # print('\n'.join(name for name in names if len(name) == min(map(len, names))))


def write_len(in_filename, out_filename):
    """
    Writes the length of each name from the input file to the output file.

    :param in_filename: The path to the input file containing names
    :type in_filename: str
    :param out_filename: The path to the output file to write the lengths of the names
    :type out_filename: str
    """
    with open(out_filename, 'w') as f:
        f.writelines((f'{len(line.strip())}\n' for line in open(in_filename, 'r')))


def find_name_by_length(file, length):
    """
    Prints all names from the given file that have the specified length.

    :param file: The path to the file containing names
    :type file: str
    :param length: The length of the names to find
    :type length: int
    """
    print('\n'.join(line.strip() for line in open(file, 'r') if len(line.strip()) == length))


if __name__ == '__main__':
    in_filename = "names.txt"
    out_filename = "name_length.txt"

    longest_name(in_filename)
    total_len(in_filename)
    shortest_name(in_filename)
    write_len(in_filename, out_filename)
    find_name_by_length(in_filename, 4)