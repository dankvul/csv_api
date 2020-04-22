from .exceptions import ArgumentsError
from .utils import get_info_from_csv, get_target_column, convert

possible_datatypes = ['int', 'float', 'datetime', 'date', 'string']


def get_max(column: int, datatype: str) -> str:
    if datatype not in possible_datatypes:
        raise ArgumentsError
    target_column: list = get_target_column(column)
    for i in range(len(target_column)):
        target_column[i] = convert(target_column[i], datatype)
    ans = max(target_column)
    if datatype == 'datetime':
        ans = ans.strftime('%d-%m-%Y (%H:%M:%S)')
    elif datatype == 'date':
        ans = ans.strftime('%d-%m-%Y')
    else:
        ans = str(ans)
    return ans


def get_min(column: int, datatype: str) -> str:
    if datatype not in possible_datatypes:
        raise ArgumentsError
    target_column: list = get_target_column(column)
    for i in range(len(target_column)):
        target_column[i] = convert(target_column[i], datatype)
    ans = min(target_column)
    if datatype == 'datetime':
        ans = ans.strftime('%d-%m-%Y (%H:%M:%S)')
    elif datatype == 'date':
        ans = ans.strftime('%d-%m-%Y')
    else:
        ans = str(ans)
    return ans


def get_sorted_data(column: int, datatype: str) -> dict:
    if datatype not in possible_datatypes:
        raise ArgumentsError
    data_from_csv: dict = get_info_from_csv()
    if column > len(data_from_csv['ColumnName']):
        raise ArgumentsError
    for i in range(len(data_from_csv['body'])):
        data_from_csv['body'][i][column - 1] = convert(data_from_csv['body'][i][column - 1], datatype)

    data_from_csv['body'].sort(key=lambda el: el[column - 1], reverse=True)

    for i in range(len(data_from_csv['body'])):
        if datatype == 'datetime':
            data_from_csv['body'][i][column - 1] = data_from_csv['body'][i][column - 1].strftime('%d-%m-%Y (%H:%M:%S)')
        elif datatype == 'date':
            data_from_csv['body'][i][column - 1] = data_from_csv['body'][i][column - 1].strftime('%d-%m-%Y')
        else:
            data_from_csv['body'][i][column - 1] = str(data_from_csv['body'][i][column - 1])
    return data_from_csv
