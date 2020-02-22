"""
This is the main module of perc2ssl and the command line entry point.
"""
import os
import sys
import logging
import argparse
import time

import perc2ssl.parse as parse

DESC = """
Convert crux percolator results to .ssl format for BiblioSpec.

Given the log and tab-delimited files from a crux percolator run, this
program will aggregate the necessary information into an .ssl file. This
can be used for input into BiblioSpec for generating spectral libraries.

An .ssl file with the same file root as the input files will be created.
"""

def main():
    """Run perc2ssl"""
    start = time.time()
    parser = argparse.ArgumentParser(description=DESC)
    parser.add_argument("target_file",
                        help=("A tab-delimited result file from crux "
                              "percolator. These end with 'percolator.target"
                              ".[psms|peptides].txt'. The root of "
                              "this file will be used to find the "
                              "corresponding log file "
                              "within the same directory."))

    parser.add_argument("--data_dir", "-d",
                        default=(".."),
                        help=("Path to the MS data files."))

    # print help if no arguments
    if len(sys.argv) == 1:
        parser.print_help(sys.stderr)
        quit()

    # logging
    logging.basicConfig(format="{levelname}: {message}",
                        style="{",
                        level=logging.INFO)

    # Run perc2ssl
    args = parser.parse_args()

    if not os.path.isfile(args.target_file):
        raise FileNotFoundError(f"{args.target_file} could not be found.")

    out_file = os.path.splitext(args.target_file)[0] + ".ssl"
    log_file = parse.find_log(args.target_file)
    logging.info("Parsing log file, %s...", log_file)
    file_map = parse.parse_log(log_file, args.data_dir)
    logging.info("Mapped file indices:")
    for idx, fname in file_map.items():
        logging.info("\t %s -> %s", idx, fname)

    logging.info("Parsing result file, %s...", args.target_file)
    ssl = parse.parse_results(args.target_file, file_map)
    logging.info("Writing to %s...", out_file)
    ssl.to_csv(out_file, sep="\t")
    fin = time.time()
    logging.info("Completed in %.2f seconds.", fin-start)
    logging.info("DONE!")


if __name__ == "__main__":
    main()
