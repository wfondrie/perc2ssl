# perc2ssl
Convert crux percolator results to .ssl format for BiblioSpec


[Crux percolator](http://crux.ms/commands/percolator.html) currently doesn't
report a format that is compatible with spectral library generation via
[BiblioSpec](https://skyline.ms/project/home/software/BiblioSpec/begin.view). As
a temporary solution, this package provides a command line tool to convert crux
percolator results to the BiblioSpec-compatible .ssl file format.

## Installation  
This package requires Python 3.5+. Although I currently don't plan to release it
on PyPI, it can be easily installed with:

```bash
pip install git+https://github.com/wfondrie/perc2ssl.git
```

## Usage  
perc2ssl is easy to use. Once installed, the documentation can be displayed by
running `perc2ssl` with no arguments, or by using the `-h` and `--help`
arguments.

```
usage: perc2ssl [-h] [--data_dir DATA_DIR] target_file

Convert crux percolator results to .ssl format for BiblioSpec. Given the log
and tab-delimited files from a crux percolator run, this program will
aggregate the necessary information into an .ssl file. This can be used for
input into BiblioSpec for generating spectral libraries. An .ssl file with the
same file root as the input files will be created.

positional arguments:
  target_file           A tab-delimited result file from crux percolator.
                        These end with
                        'percolator.target.[psms|peptides].txt'. The root of
                        this file will be used to find the corresponding log
                        file within the same directory.

optional arguments:
  -h, --help            show this help message and exit
  --data_dir DATA_DIR, -d DATA_DIR
                        Path to the MS data files.
```
