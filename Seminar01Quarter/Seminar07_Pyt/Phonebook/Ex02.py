import csv

name='Jeck'
surname="Kolins"
phone_number='358798948203970'

def init(im,sern,phone):
    global name
    global surname
    global phone_number
    name=im
    surname=sern
    phone_number=phone

with open('names.csv', 'w', newline='') as csvfile:
    fieldnames = ['first_name', 'last_name','phone_number']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writerow({'first_name': name, 'last_name': surname,'phone_number': phone_number})
