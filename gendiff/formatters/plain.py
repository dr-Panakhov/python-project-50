def to_str(value):
    if isinstance(value, dict):
        return "[complex value]"
    if isinstance(value, bool):
        return str(value).lower()
    if value is None:
        return "null"
    if isinstance(value, int):
        return str(value)
    return f"'{value}'"


def render_plain(diff, path=""):
    lines = []

    for node in diff:
        property_path = f"{path}{node['key']}"
        type_ = node['type']
        if type_ == 'nested':
            lines.append(render_plain(node['children'], f"{property_path}."))
        elif type_ == 'added':
            val = to_str(node['value'])
            res = f"Property '{property_path}' was added with value: {val}"
            lines.append(res)
        elif type_ == 'deleted':
            res = f"Property '{property_path}' was removed"
            lines.append(res)
        elif type_ == 'changed':
            old_val = to_str(node['old_value'])
            new_val = to_str(node['new_value'])
            res = (f"Property '{property_path}' was updated. "
                   f"From {old_val} to {new_val}")
            lines.append(res)

    return "\n".join(lines)
