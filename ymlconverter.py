#!/usr/bin/env python
import json
import yaml
import argparse


def write_data(data, out_file):
    with open(out_file, 'a') as f:
        f.write(data)

def json2yml(in_file, out_file):
    with open(in_file) as f:
        write_data(data=yaml.safe_dump(json.load(f), default_flow_style=False, indent=4), out_file=out_file)

def yml2json(in_file, out_file):
    with open(in_file) as f:
        write_data(data=json.dumps(yaml.safe_load(f), indent=4), out_file=out_file)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--infile', help='input file json or yaml extension', required=True)
    parser.add_argument('--outfile', help='output file name', required=True)
    args = parser.parse_args()

    if "json" in args.infile:
        json2yml(args.infile, args.outfile)
    elif "yml" in args.infile or "yaml" in args.infile:
        yml2json(args.infile, args.outfile)
