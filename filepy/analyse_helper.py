import re

from filepy.dto import DTO


def classify_attribute(attribute: str) -> str:
    try:
        float(attribute)
    except ValueError:
        return "string"
    return "numeric"


def create_attributes_to_save(dto: DTO) -> str:
    attributes: str = ""
    first_data_line: list = dto.data[0]
    columns: list = []
    if dto.columns:
        columns = dto.columns
    else:
        for index in range(len(first_data_line)):
            columns.append('col{index}'.format(index=index))
    for column, data in zip(columns, first_data_line):
        attributes += "@attribute {} {}\n".format(
            column, classify_attribute(data))
    return attributes


def extract_filename_from_path_to_file(path_to_file: str) -> str:
    index_of_starting_filename = path_to_file.rfind('/')
    if index_of_starting_filename == -1:
        return path_to_file
    return path_to_file[index_of_starting_filename + 1:]


def is_line_containing_declaration(line: str, declaration: str) -> bool:
    return bool(line.strip() and line.split()[0].lower() == '@' + declaration)


def split_attributes(line: str) -> tuple:
    groups = []
    for match in re.finditer(r'\s+(?![^{]*})', line.strip()):
        groups.append(match.span())

    first_part = line[groups[0][1]:groups[1][0]]
    second_part = line[groups[1][1]:]
    return first_part.strip(), second_part.strip()
