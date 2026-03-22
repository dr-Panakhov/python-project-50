def to_str(value, depth):
    if isinstance(value, bool):
        return str(value).lower()
    if value is None:
        return "null"
    if isinstance(value, dict):
        indent_size = depth * 4
        current_indent = " " * indent_size
        end_indent = " " * ((depth - 1) * 4)
        lines = []
        for k, v in value.items():
            lines.append(f"{current_indent}{k}: {to_str(v, depth + 1)}")
        result = "\n".join(lines)
        return f"{{\n{result}\n{end_indent}}}"
        
    return str(value)


def render_stylish(diff, depth=1):
    indent_size = depth * 4
    current_indent = " " * (indent_size - 2)
    end_indent = " " * ((depth - 1) * 4)

    lines = []
    for node in diff:
        key = node['key']
        type_ = node['type']

        if type_ == 'nested':
            children_str = render_stylish(node['children'], depth + 1)
            lines.append(f"{current_indent}  {key}: {children_str}")
        elif type_ == 'added':
            val = to_str(node['value'], depth + 1)
            lines.append(f"{current_indent}+ {key}: {val}")
        elif type_ == 'deleted':
            val = to_str(node['value'], depth + 1)
            lines.append(f"{current_indent}- {key}: {val}")
        elif type_ == 'unchanged':
            val = to_str(node['value'], depth + 1)
            lines.append(f"{current_indent}  {key}: {val}")
        elif type_ == 'changed':
            old_val = to_str(node['old_value'], depth + 1)
            new_val = to_str(node['new_value'], depth + 1)
            lines.append(f"{current_indent}- {key}: {old_val}")
            lines.append(f"{current_indent}+ {key}: {new_val}")

    result = "\n".join(lines)
    return f"{{\n{result}\n{end_indent}}}"
