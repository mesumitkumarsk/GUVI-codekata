import re

def extract_dates(text):
    pattern = r'\b\d{2}/\d{2}/\d{4}\b'
    dates = re.findall(pattern, text)
    return dates

text = input()
dates = extract_dates(text)
print(", ".join(dates))