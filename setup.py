"""
Setup the perc2ssl package.
"""
import setuptools

with open("README.md", "r") as readme:
    LONG_DESC = readme.read()

DESC = ("Convert crux percolator results to .ssl format for BiblioSpec")

CATAGORIES = ["Programming Language :: Python :: 3",
              "License :: OSI Approved :: Apache Software License",
              "Operating System :: OS Independent",
              "Topic :: Scientific/Engineering :: Bio-Informatics"]

setuptools.setup(
    name="perc2ssl",
    version="0.0.1",
    author="William E. Fondrie",
    author_email="fondriew@gmail.com",
    description=DESC,
    long_description=LONG_DESC,
    long_description_content_type="text/markdown",
    url="https://github.com/wfondrie/perc2ssl",
    packages=setuptools.find_packages(),
    license="Apache 2.0",
    entry_points={"console_scripts": ["perc2ssl = perc2ssl.perc2ssl:main"]},
    classifiers=CATAGORIES,
    install_requires=["numpy", "pandas"],
    use_scm_version=True,
    setup_requires=["setuptools_scm"]
)
