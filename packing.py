def greedy_packing( items, pckg_size = 1 ):
  _items = items[:]
  packages = [[]]
  current_size = 0

  while len(_items) > 0:

    next_idx = None
    for (idx,item) in enumerate(_items):
      if item + current_size <= pckg_size:
        next_idx = idx
        break
    
    if next_idx is not None:
      packages[-1].append(_items[next_idx])
      current_size += _items[next_idx]
      _items.pop(next_idx)
    else:
      packages.append([])
      current_size = 0

  return packages


def dumb_packing( items, pckg_size = 1):
  packages = [[]]
  current_size = 0

  for item in items:
    if current_size + item <= pckg_size:
        packages[-1].append(item)
        current_size += item
    else:
        packages.append([item])
        current_size = item

  return packages



def brute_packing(items, pckg_size=1, packages=[[]], current_size=0, best_size=None, best=None):
  
  if best_size is not None and len(packages) >= best_size:
    return best

  if len(items) == 0:
    return packages

  def add_item(idx):
    item = items[idx]
    if item + current_size <= pckg_size:
      new_packages = [x[:] for x in packages]
      new_packages[-1].append(item)
      new_items = items[:]
      new_items.pop(idx)
      new_size = current_size + item
      return (new_packages, new_items, new_size)
    else:
      new_packages = [x[:] for x in packages]
      new_packages.append([item])
      new_items = items[:]
      new_items.pop(idx)
      new_size = item
      return (new_packages, new_items, new_size)

  for (idx, item) in enumerate(items):
    new_packages, new_items, new_size = add_item(idx)
    new_best = brute_packing(new_items, pckg_size, new_packages, new_size, best_size, best)
    if best is None or len(new_best) < len(best):
      best = new_best
      best_size = len(best)
    
  return best
