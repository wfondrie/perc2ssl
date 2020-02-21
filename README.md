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
