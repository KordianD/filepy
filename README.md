[![Build Status](https://travis-ci.com/KordianD/filepy.svg?branch=master)](https://travis-ci.com/KordianD/filepy)
[![PyPI version](https://badge.fury.io/py/filepy.svg)](https://badge.fury.io/py/filepy)
 
# Goal
This is a package which converts files to different types.

# Supported extensions 
- CSV
- ARFF

# Installation
``pip install filepy --upgrade`` 

# Usage

This library is mainly divided into 2 ideas, namely writers and readers.
Readers will read your files, writer will write in appropriate format.

# Available classes:
- CsvReader
- CsvWriter
- ArffReader
- ArffWriter


Suppose that you have a csv file: `example1.csv`.

You want to convert this file to an arff format for instance `converted.arff`

    from filepy.csv_reader import CsvReader
    from filepy.arff_writer import ArffWriter
    from filepy.file_converter import convert

    csv_reader = CsvReader('example1.csv', delimiter=';')
    arff_writer = ArffWriter('converted.arff', delimiter=',')

    convert(input_reader=csv_reader, output_writer=arff_writer)
    
# Additional options

Each writer and reader has additional options to use.

# CsvReader
CsvReader(path_to_file, delimiter = ',', first_line_column_names = True, skip_first_column = False)
    
    delimiter - how data is separated, can be regex
    first_line_column_names - uses first line to read columns
    skip_first_column - skips first column of data 

After creating object you can get data from it.

    csv_reader = CsvReader('your/path/to/file')
    data = csv_reader.dto.data
    column_names = csv_reader.dto.columns

# CsvWriter    
CsvWriter(path_to_file, delimiter = ',', skip_writing_columns = False)

    delimiter - how data will be separated in generated file
    skip_writing_column - whether first line in generated file should have columns names
   
# ArffReader
ArffReader(path_to_file, delimiter = ',')

    delimiter - how data is separated, can be regex
    
After creating object you can get data from it.
    
    csv_reader = CsvReader('your/path/to/file')
    data = csv_reader.dto.data
    column_names = csv_reader.dto.columns
    
# ArffWriter
ArffWriter(path_to_file, delimiter= ',')

    delimiter - how data will be separated in generated file
    