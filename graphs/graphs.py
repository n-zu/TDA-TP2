import json

def load_stats( file_name ):
    stats = {}
    with open(file_name) as f:
        for line in f:
            data = json.loads(line)
            for name, value in data.items():
                if name not in stats:
                    stats[name] = []
                stats[name].append(value)
    return stats

def graph(stats, key, y_label, logscale = False, output_file_name = None):
    import matplotlib.pyplot as plt

    plt.figure(figsize=(10,10))
    
    for name, data in stats.items():
        if name == "items":
            continue
        plt.errorbar(stats["items"], [x[key]["avg"] for x in data], yerr=[x[key]["dev"] for x in data], label=name)
    
    plt.xlabel("Number of items")
    plt.ylabel(y_label)

    if logscale:
        plt.yscale("log")

    plt.legend()

    if output_file_name is not None:
        plt.savefig(output_file_name)
    else:
        plt.show()


if __name__ == "__main__":
    stats = load_stats("data/stats.json")
    
    graph(stats, "result", "number of bins", False, "graphs/number_of_bins.png")
    graph(stats, "duration", "duration (s)", True, "graphs/duration.png")

    

