def generate_items(number_of_items, min=0, max=1, file_name=None):
    import random

    items = [random.uniform(min, max) for _ in range(number_of_items)]

    if file_name is not None:
        from static_items import save_items
        save_items(file_name, items)

    return items
    