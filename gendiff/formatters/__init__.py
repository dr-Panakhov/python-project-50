from gendiff.formatters.plain import render_plain
from gendiff.formatters.stylish import render_stylish


def format_diff(diff_tree, format_name):
    if format_name == 'stylish':
        return render_stylish(diff_tree)
    if format_name == 'plain':
        return render_plain(diff_tree)
    raise ValueError(f"Unknown format: {format_name}")
