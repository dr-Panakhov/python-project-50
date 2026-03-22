import json
import os

import pytest

from gendiff import generate_diff


def get_fixture_path(file_name):
    current_dir = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(current_dir, 'test_data', file_name)


def read_file(file_path):
    with open(file_path, 'r') as f:
        return f.read()


@pytest.mark.parametrize("file1, file2, expected_file", [
    ('file1.json', 'file2.json', 'expected.txt'),
    ('file1.yml', 'file2.yml', 'expected.txt'),
    ('file1_nested.json', 'file2_nested.json', 'expected_nested.txt'),
    ('file1_nested.yml', 'file2_nested.yml', 'expected_nested.txt')
])
def test_generate_diff(file1, file2, expected_file):
    path1 = get_fixture_path(file1)
    path2 = get_fixture_path(file2)
    expected = read_file(get_fixture_path(expected_file)).strip()
    
    assert generate_diff(path1, path2).strip() == expected


def test_plain_format():
    path1 = get_fixture_path('file1_nested.json')
    path2 = get_fixture_path('file2_nested.json')
    expected = read_file(get_fixture_path('expected_plain.txt')).strip()
    
    assert generate_diff(path1, path2, 'plain').strip() == expected


def test_json_format():
    path1 = get_fixture_path('file1_nested.json')
    path2 = get_fixture_path('file2_nested.json')
    result = generate_diff(path1, path2, 'json')
    
    assert json.loads(result)
