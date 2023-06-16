import time
import json
import logging
from packing import APROXIMATIONS
from items.generate_items import generate_items_for_bins


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

def generate_iteration_stats( functions, number_of_bins, repetitions ):

    logging.info(f"Bins [{number_of_bins}]: ")

    iteration_stats = { "items": [] }
    for name in functions.keys():
        iteration_stats[name] = []

    for i in range(repetitions):
        logging.debug(f"  It:{i+1}")
        start_time = time.time()
        items = generate_items_for_bins(number_of_bins)
        iteration_stats["items"].append({ "len": len(items)})

        for name, function in functions.items():
            logging.debug(f"    {name}")
            iteration_stats[name].append( run_stats(function, items) )
        logging.debug(f"  {i+1} - {time.time()-start_time}")
    
    for name, data in iteration_stats.items():
        iteration_stats[name] = aggregate(data)

    logging.debug(iteration_stats)
    return iteration_stats

def generate_stats( functions = APROXIMATIONS, start=100, stop=1000, step=100, repetitions=10, fs=None ):

    stats={
        "bins": [],
        "items": []
    }
    for name in functions.keys():
        stats[name] = []

    for number_of_bins in range(start, stop+1, step):
        stats["bins"].append(number_of_bins)

        iteration_stats = generate_iteration_stats(functions, number_of_bins, repetitions)

        for name, data in iteration_stats.items():
            stats[name].append(data)

        if fs is not None:
            iteration_stats["bins"] = number_of_bins
            fs.write(json.dumps(iteration_stats))
            fs.write("\n")

    return stats   


if __name__ == "__main__":

    logging.addLevelName(
        logging.DEBUG, "\033[1;32m%s\033[1;0m" % logging.getLevelName(logging.DEBUG))
    logging.addLevelName(
        logging.INFO, "\033[1;34m%s\033[1;0m" % logging.getLevelName(logging.INFO))

    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s',
                        datefmt='%H:%M:%S')
    with open("data/stats2.json", "w") as f:
        generate_stats(fs=f)