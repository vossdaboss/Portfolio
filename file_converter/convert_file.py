import argparse
import json
import pandas as pd

# Define the command line arguments
parser = argparse.ArgumentParser(description='Convert file format.')
parser.add_argument('input_path', type=str, help='Path to input file')
parser.add_argument('output_path', type=str, help='Path to output file')
parser.add_argument('input_format', type=str, help='Input file format')
parser.add_argument('output_format', type=str, help='Output file format')

# Parse the command line arguments
args = parser.parse_args()

# Read the input file
if args.input_format == 'csv':
    df = pd.read_csv(args.input_path)
elif args.input_format == 'json':
    with open(args.input_path, 'r') as f:
        data = json.load(f)
    df = pd.DataFrame(data)

# Convert the data to the output format
if args.output_format == 'csv':
    df.to_csv(args.output_path, index=False)
elif args.output_format == 'json':
    with open(args.output_path, 'w') as f:
        data = df.to_dict(orient='records')
        json.dump(data, f, indent=4)
