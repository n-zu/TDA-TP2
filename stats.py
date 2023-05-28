import time
import json
import logging
from packing import greedy_packing, dumb_packing, brute_packing
from items.generate_items import generate_items

FUNCTIONS = {
    'greedy': greedy_packing,
    'dumb': dumb_packing,
    'brute': brute_packing
}


def aggregate( iterable ):
    """
    Receives a list of objects,
    Converts into an object with the same keys,
    with values being the average and deviation of the values in the list
    """
    result = {}
    for key in iterable[0].keys():
        values = [x[key] for x in iterable]
        result[key] = {
            "avg": sum(values)/len(values),
            "dev": sum([(x - sum(values)/len(values))**2 for x in values])/len(values)
        }
    return result

def run_stats( function, items ):
    start = time.time()
    result=len(function(items))
    duration = time.time() - start

    return {
        "result": result,
        "duration": duration
    }

def generate_iteration_stats( functions, number_of_items, repetitions ):

    logging.info(f"Iteration [{number_of_items}]: ")

    iteration_stats = {}
    for name in functions.keys():
        iteration_stats[name] = []

    for i in range(repetitions):
        start_time = time.time()
        items = generate_items(number_of_items)
        for name, function in functions.items():
            iteration_stats[name].append( run_stats(function, items) )
        logging.debug(f"  {i+1} - {time.time()-start_time}")
    
    for name, data in iteration_stats.items():
        iteration_stats[name] = aggregate(data)

    logging.debug(iteration_stats)
    return iteration_stats

def generate_stats( functions = FUNCTIONS, start=3, stop=12, step=3, repetitions=10, fs=None ):

    stats={
        "items": [],
    }
    for name in functions.keys():
        stats[name] = []

    for number_of_items in range(start, stop+1, step):
        stats["items"].append(number_of_items)

        iteration_stats = generate_iteration_stats(functions, number_of_items, repetitions)

        for name, data in iteration_stats.items():
            stats[name].append(data)

        if fs is not None:
            iteration_stats["items"] = number_of_items
            fs.write(json.dumps(iteration_stats))
            fs.write("\n")

    return stats   


if __name__ == "__main__":

    logging.addLevelName(
        logging.DEBUG, "\033[1;32m%s\033[1;0m" % logging.getLevelName(logging.DEBUG))
    logging.addLevelName(
        logging.INFO, "\033[1;34m%s\033[1;0m" % logging.getLevelName(logging.INFO))

    logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s',
                        datefmt='%H:%M:%S')
    with open("data/stats.json", "w") as f:
        generate_stats(fs=f)