import json

def generate_diff(file_path1, file_path2):
    data1 = json.load(open(file_path1))
    data2 = json.load(open(file_path2))
    
    print(data1)
    print(data2)
    
    return "Diff will be here soon!"
