import itertools
import json


def stringify(value, replacer=' ', spaces_count=1):

    def iter_(current_value, depth):
        if not isinstance(current_value, dict):
            return str(current_value)

        deep_indent_size = depth + spaces_count
        deep_indent = replacer * deep_indent_size
        current_indent = replacer * depth
        lines = []
        for key, val in current_value.items():
            lines.append(f'{deep_indent}{key}: {iter_(val, deep_indent_size)}')
        result = itertools.chain(lines, current_indent, '\n')
        return ''.join(result)

    return iter_(value, 0)


def json_to_dict(path: str) -> dict:
    with open(path) as fp:
        result = json.load(fp)

    # decoding from python to json: true, false и null
    for key, value in result.items():
        if type(value) is bool:
            result[key] = str(value).lower()
        elif value is None:
            result[key] = 'null'

    return result


def generate_diff(file_path1: str, file_path2: str) -> str:
    file1 = json_to_dict(file_path1)
    file2 = json_to_dict(file_path2)
    result = ''
    keys = file1.keys() | file2.keys()

    for key in sorted(keys):
        if key not in file1:
            result += stringify({key: file2[key]}, '  + ')
        elif key not in file2:
            result += stringify({key: file1[key]}, '  - ')
        elif file1[key] == file2[key]:
            result += stringify({key: file1[key]}, '    ')
        else:
            result += stringify({key: file1[key]}, '  - ')
            result += stringify({key: file2[key]}, '  + ')

    return '{\n' + result + '}'