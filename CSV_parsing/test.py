import re

pattern_text = r'[\w\s.,\"\'!?а-яА-Я]+'
pattern = r'^[\w\s.,\"\'!?а-яА-Я]+:\s\d{4}-\d{2}-\d{2},[\w\s.,\"\'!?а-яА-Я]+'
pattern_city_timestamp = r'^[\w\s.,!?а-яА-Я]+?\d{4}-\d{2}-\d{2} \d{2}:\d{2}$'

# string_text = 'Something happen. Right no4w 4 we don\'t understands what exactly. But something absolutely happen'
string = "Actual until: 2023-03-29, 7 days left"
string_timestamp = 'Krakow 22-3-2023 19:41'
string_text = 'News_text1'

if re.match(pattern_text, string_text):
    print("Строка соответствует заданному шаблону")
else:
    print("Строка не соответствует заданному шаблону")

