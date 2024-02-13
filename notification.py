import openpyxl
from datetime import datetime, date
import requests

workbook = openpyxl.load_workbook('NAME OF THE EXCEL FILE ONLY -> example: data.xlsx') 
sheet = workbook.active
date_column = sheet['C']
assg_column = sheet['A']

today_date = date.today()
today_date_formatted = today_date.strftime('%d/%m/%Y')

for cell, cell_assignment_name in zip(date_column, assg_column):
    try:
        if isinstance(cell.value, (datetime, date)):
            cell_date = cell.value.date()
        elif isinstance(cell.value, str):
            cell_date = datetime.strptime(cell.value, '%d/%m/%Y')
            cell_date_formatted = cell_date.strftime('%d/%m/%Y')
        else:
            continue

        if cell_date_formatted == today_date_formatted:
            requests.post('https://api.mynotifier.app', {
            "apiKey":  '********-****-****-****-************', # Add your own apiKey here
            "description": "Hello! Your assignment {0} is due today ({1}). Don't forget to send it!".format(cell_assignment_name.value, cell_date_formatted),
            "message": "Assignment due today!",
            "type": "info"
            })
            
            # To test it without sending the notification:
            # print(f"Hello! Your assignment {cell_assignment_name.value} is due today ({cell_date_formatted}). Don't forget to send it!")

    except ValueError:
        print(f"Skipping row {cell.row} - Invalid date format: {cell.value}")
