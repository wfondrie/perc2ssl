"""
Parse the required files
"""
import os
import re
from typing import Dict

import pandas as pd

def get_fileroot(perc_file: str) -> str:
    """
    Get the root of the Percolator result file.

    Parameters
    ----------
    perc_file
        The result file to obtain the fileroot from.

    Returns
    -------
    The file root, including the path and "percolator".
    """
    return ".".join(perc_file.split(".")[:-3])


def find_log(perc_file: str) -> str:
    """
    Find the crux percolator log file.

    Parameters
    ----------
    perc_file
        The result file to obtain the fileroot from.

    Returns
    -------
    The path to the crux percolator log file.
    """
    log_file = get_fileroot(perc_file) + ".log.txt"

    if not os.path.isfile(log_file):
        raise FileNotFoundError("{} could not be found.".format(log_file))

    return log_file


def parse_log(log_file: str, data_dir) -> Dict:
    """
    Parse the log file to find the file indices.

    Parameters
    ----------
    log_file
        The log file from crux percolator.

    Returns
    -------
    A dictionary mapping the file indices to file names.
    """
    idx_regex = re.compile(r"Assigning index (\d+) to (.+).")
    file_map = {}
    with open(log_file, "r") as log:
        for line in log:
            if "Assigning index" in line:
                idx, fname = idx_regex.search(line).groups()
                fname = os.path.join(data_dir, fname)

                if not os.path.isfile(os.path.expanduser(fname)):
                    raise FileNotFoundError("{} could not be found".format(fname))

                file_map[idx] = fname

    return file_map


def parse_results(perc_file: str, file_map: Dict) -> pd.DataFrame:
    """
    Parse the crux percolator results file
    """
    res = pd.read_csv(perc_file, sep="\t")
    res["file"] = [file_map[str(i)] for i in res["file_idx"]]
    res["score-type"] = "PERCOLATOR QVALUE"
    res = res.rename(columns={"percolator q-value": "score"})

    ssl_cols = ("file", "scan", "charge", "sequence", "score-type", "score")
    return res.loc[:, ssl_cols]
