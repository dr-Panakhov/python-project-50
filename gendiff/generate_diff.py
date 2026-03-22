import os

from gendiff.builder import build_diff
from gendiff.formatters.stylish import render_stylish
from gendiff.parser import parse


def get_file_data(file_path):
    with open(file_path, 'r') as file:
        data = file.read()
    
    _, extension = os.path.splitext(file_path)
    format_name = extension[1:].lower()
    
    return parse(data, format_name)


def generate_diff(file_path1, file_path2, format_name='stylish'):
    data1 = get_file_data(file_path1)
    data2 = get_file_data(file_path2)
    
    diff_tree = build_diff(data1, data2)
    
    if format_name == 'stylish':
        return render_stylish(diff_tree)
