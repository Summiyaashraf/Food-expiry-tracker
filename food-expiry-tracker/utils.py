from datetime import datetime

def format_date(date):
    return date.strftime("%Y-%m-%d")

def parse_date(date_str):
    return datetime.strptime(date_str, "%Y-%m-%d")