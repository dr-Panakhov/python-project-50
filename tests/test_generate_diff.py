import os

from gendiff import generate_diff


def get_fixture_path(file_name):
    current_dir = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(current_dir, 'test_data', file_name)


def read_file(file_path):
    with open(file_path, 'r') as f:
        return f.read()


def test_generate_diff():
    file1 = get_fixture_path('file1.json')
    file2 = get_fixture_path('file2.json')
    expected_path = get_fixture_path('expected.txt')
    expected = read_file(expected_path).strip()
    assert generate_diff(file1, file2).strip() == expected
