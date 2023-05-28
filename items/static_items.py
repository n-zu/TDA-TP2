def parse_item(line):
    try:
        return float(line)
    except:
        return None

def load_items(file_name):
    items = []
    with open(file_name) as f:
        #skip first 2 lines
        f.readline()
        f.readline()

        for line in f:
            item = parse_item(line)
            if item is not None:
                items.append(item)
    return items

def save_items(file_name, items):

    output = f'{len(items)}\n'
    for item in items:
        output += f'\n{item}'

    with open(file_name, "w") as f:
        f.write(output)
