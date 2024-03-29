import os
import pathlib

separator = '------------------------------\n'      # separator for records
title_length = 30                                   # default length of record title
all_news_file_path = os.path.join(pathlib.Path.cwd(), 'news_feed.txt')      # defaulf file path to write
default_file_to_read_news = os.path.join(pathlib.Path.cwd(), 'FilesToRead/news_to_read.txt')  # default file path to read
default_file_path_to_csv_file = 'CSV_files'  # default file path to csv files
default_file_path_to_json_file = 'JSON/text.json'    # default file path to json files
default_file_path_to_xml_file = 'XML/text.xml'  # default file path to json files
default_file_path_to_db = 'test.db'     # default file path to db file
pattern_city_timestamp = r'^[\w\s.,!?а-яА-Я]+?\d{4}-\d{2}-\d{2} \d{2}:\d{2}$'
pattern_text = r'[\w\s.,\"\'!?а-яА-Я]+'
pattern_ad_exp_date = r'^[\w\s.,\"\'!?а-яА-Я]+:\s\d{4}-\d{2}-\d{2},[\w\s.,\"\'!?а-яА-Я]+'
