import random

def generate_items(number_of_items, min=0, max=1, file_name=None):

    items = [random.uniform(min, max) for _ in range(number_of_items)]

    if file_name is not None:
        from static_items import save_items
        save_items(file_name, items)

    return items

def generate_items_for_bins(bins, bin_size = 1):
    
    # generate a list of items that filss the bins completely

    items = []

    for _ in range(bins):
      free_space = bin_size
      while True:
        item = round(random.uniform(0, free_space), 3)

        if item == 0:
          continue

        if item >= free_space-0.001:
          break

        items.append(item)
        free_space -= item

      items.append(free_space-0.001)

    random.shuffle(items)

    return items
    