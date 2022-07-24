import argparse


def parse():
    parser = argparse.ArgumentParser(
        description='Compares two configuration files and shows a difference.'
    )

    parser.add_argument('first_file', type=str)
    parser.add_argument('second_file', type=str)

    parser.add_argument(
        '-f', '--format',
        metavar='FORMAT',
        help='set format of output',
        choices=['stylish', 'plain', 'json'],
        default='stylish'
    )

    args = parser.parse_args()

    return args