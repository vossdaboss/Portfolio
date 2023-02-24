import argparse
import sqlite3
import pandas as pd
import os

# Define the command line arguments
parser = argparse.ArgumentParser(description='Convert file format.')
parser.add_argument('input_path_full', type=str, help='Path to input file')
parser.add_argument('output_path_full', type=str, help='Path to output file')
parser.add_argument('input_format', type=str, help='Input file format')
parser.add_argument('output_format', type=str, help='Output file format')

# Parse the command line arguments
args = parser.parse_args()

# Read the input file
if args.input_format == 'csv':
    df = pd.read_csv(args.input_path_full)
elif args.input_format == 'json':
    df = pd.read_json(args.input_path_full)
elif args.input_format == 'xml':
    df = pd.read_xml(args.input_path_full)
elif args.input_format == 'SQL':
    conn = sqlite3.connect(args.input_path_full)
    df = pd.read_sql('SELECT * FROM data', conn)


# Convert the data to the output format
if args.output_format == 'csv':
    # Write output to output file
    output_dir = 'output'
    output_path_full = os.path.join(output_dir, args.output_path_full)
    df.to_csv(output_path_full, index=False)
elif args.output_format == 'json':
    output_dir = 'output'
    output_path_full = os.path.join(output_dir, args.output_path_full)
    df.to_json(output_path_full, orient='records')
elif args.output_format == 'xml':
    output_dir = 'output'
    output_path_full = os.path.join(output_dir, args.output_path_full)
    df.to_xml(output_path_full)
elif args.output_format == 'SQL':
    output_dir = 'output'
    output_path_full = os.path.join(output_dir, args.output_path_full)
    conn = sqlite3.connect(output_path_full)
    df.to_sql('data', conn, if_exists='replace', index=False)