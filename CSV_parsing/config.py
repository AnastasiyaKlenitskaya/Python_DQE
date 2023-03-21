import os
import pathlib

separator = '------------------------------\n'      # separator for records
title_length = 30                                   # default length of record title
all_news_file_path = os.path.join(pathlib.Path.cwd(), 'news_feed.txt')      # defaulf file path to write
default_file_to_read_news = os.path.join(pathlib.Path.cwd(), 'FilesToRead/news_to_read.txt')  # default file path to read
default_file_path_to_csv_file = 'CSVFiles'  # default file path to csv files

