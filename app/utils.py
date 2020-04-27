import csv
from config import Config
from .exceptions import ArgumentsError, WrongDataError
from datetime import date, datetime
from typing import Union
import dateutil.parser


def convert(var: str, datatype: str) -> Union[int, float, datetime, date]:
    if datatype == 'int':
        try:
            var = int(var)
        except ValueError:
            raise WrongDataError
    if datatype == 'float':
        try:
            var = float(var)
        except ValueError:
            raise WrongDataError
    if datatype == 'datetime' or datatype == 'date':
        try:
            var = dateutil.parser.parse(var)
        except ValueError:
            raise WrongDataError
    return var


def get_column_name(column: int) -> str:
    column_name = ''
    with open(Config.DATAFILE_PATH) as data_file:
        reader = csv.reader(data_file, delimiter=',')
        for row in reader:
            if column > len(row) or column <= 0:
                raise ArgumentsError
            column_name = row[column - 1]
            break
    return column_name


def get_target_column(column: int) -> list:
    target_column = list()
    with open(Config.DATAFILE_PATH) as data_file:
        reader = csv.reader(data_file, delimiter=',')
        current_line = 0
        for row in reader:
            if current_line == 0:
                current_line += 1
            else:
                if column > len(row) or column <= 0:
                    raise ArgumentsError
                target_column.append(row[column - 1])
    return target_column


def get_info_from_csv() -> dict:
    dataset = {'ColumnName': [], 'body': []}
    with open(Config.DATAFILE_PATH) as data_file:
        reader = csv.reader(data_file, delimiter=',')
        current_line = 0
        for row in reader:
            if current_line == 0:
                for i in row:
                    dataset['ColumnName'].append(i)
                current_line += 1
            else:
                dataset['body'].append(row)
                current_line += 1
    return dataset
