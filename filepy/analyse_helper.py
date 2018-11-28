from filepy.dto import DTO


def classify_attribute(attribute: str) -> str:
    try:
        float(attribute)
    except ValueError:
        return "string"
    return "numeric"


def create_attributes_to_save(dto: DTO) -> str:
    attributes = ""
    first_data_line = dto.data[0]
    for column, data in zip(dto.columns, first_data_line):
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
