from flask import Blueprint, request, jsonify
from .operations import get_max, get_min, get_sorted_data
from .exceptions import ArgumentsError, WrongDataError
from .utils import get_column_name, get_info_from_csv

api = Blueprint('api', __name__)


@api.route('/', methods=['GET', 'POST'])
def gateway():
    operation_type = request.args.get('type')
    column = request.args.get('column')
    datatype = request.args.get('datatype')
    if operation_type is None and column is None and datatype is None:
        raw_data = get_info_from_csv()
        return jsonify(raw_data)
    try:
        column = int(column)
    except ValueError:
        return '<h1>Bad request</h1>', 400

    if operation_type == 'max':
        try:
            max_from_column = get_max(column, datatype)
            column_name = get_column_name(column)
        except ArgumentsError and WrongDataError:
            return '<h1>Bad request</h1>', 400
        return jsonify({column_name: max_from_column})

    if operation_type == 'min':
        try:
            min_from_column = get_min(column, datatype)
            column_name = get_column_name(column)
        except ArgumentsError and WrongDataError:
            return '<h1>Bad request</h1>', 400
        return jsonify({column_name: min_from_column})

    if operation_type == 'sort':
        try:
            sorted_data = get_sorted_data(column, datatype)
        except ArgumentsError and WrongDataError:
            return '<h1>Bad request</h1>', 400
        return jsonify(sorted_data)
    else:
        return '<h1>Bad request</h1>', 400
