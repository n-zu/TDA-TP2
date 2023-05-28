import time
import argparse
from items.static_items import load_items
from packing import FUNCTIONS

parser = argparse.ArgumentParser(description='Solution for the packing problem')
parser.add_argument('function', metavar='function', type=str, nargs=1, help='function to use: ' + str(FUNCTIONS.keys()), choices=FUNCTIONS.keys())
parser.add_argument('data', metavar='data', type=str, nargs=1, help='data file')

args  = parser.parse_args()

function = FUNCTIONS[args.function[0]]
data = args.data[0]

items = load_items(data)

print(f"Processing items")
print(f"{items}")

start_time = time.time()
packages = function(items)
duration = time.time() - start_time

print(f"Time: {duration}")
print(f"#Packages: {len(packages)}")
print(f"{packages}")
                    
