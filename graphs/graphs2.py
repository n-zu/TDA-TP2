import json
import matplotlib.pyplot as plt


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

def grap_results(stats, key, y_label, logscale = False, output_file_name = None):
  pass

def graph(stats, key, y_label, logscale = False, output_file_name = None):
    plt.figure(figsize=(10,10))
    
    for name, data in stats.items():
        if name == "items" or name == "bins":
            continue
        plt.errorbar(stats["bins"], [x[key]["avg"] for x in data], yerr=[x[key]["dev"] for x in data], label=name)
    
    if key == "result":
      plt.errorbar(stats["bins"], stats["bins"], label="bins",linestyle="dashed")
    
    plt.xlabel("Number of bins")
    plt.ylabel(y_label)

    if logscale:
        plt.yscale("log")

    plt.legend()

    if output_file_name is not None:
        plt.savefig(output_file_name)
    else:
        plt.show()


if __name__ == "__main__":
    stats = load_stats("data/stats2.1.json")
    graph(stats, "result", "number of bins", False, "graphs/number_of_bins_2.1.png")
    graph(stats, "duration", "duration (s)", False, "graphs/duration_2.1.png")
    
    stats = load_stats("data/stats2.2.json")
    graph(stats, "result", "number of bins", False, "graphs/number_of_bins_2.2.png")
    graph(stats, "duration", "duration (s)", False, "graphs/duration_2.2.png")

    

