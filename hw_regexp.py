from pprint import pprint
import re
import csv

with open("phonebook_raw.csv", encoding='utf-8') as f:
    rows = csv.reader(f, delimiter=",")
    contacts_list = list(rows)
# pprint(contacts_list)

correct_list = []
correct_list.append(contacts_list[0])

for contact_line in contacts_list[1:]:
    names = contact_line[0]
    contacts = names.split()

    if len(contacts) == 1:
        names = contact_line[1].split()
        if len(names) == 1:
            contacts.append(names[0])
        else:
            contacts.append(names[0])
            contacts.append(names[1])

    if len(contacts) == 2:
        contacts.append(contact_line[2])
    contacts.append(contact_line[3])
    contacts.append(contact_line[4])

    phones = contact_line[5]
    pattern = r'(\+?\d)\s?\(?(\d{3})\)?[\s|\-]?(\d{3})\-?(\d{2})\-?(\d{2})\s?\(?(\w*\.?)\s?(\d*)\)?'
    sub = r'+7(\2)\3-\4-\5 \6\7'
    correct_phone = re.sub(pattern, sub, phones)
    contacts.append(correct_phone)

    contacts.append(contact_line[6])

    for duplicate in correct_list:
        if contacts[0] == duplicate[0] and contacts[1] == duplicate[1]:
            for i in range(0, len(contacts)):
                if duplicate[i] < contacts[i]:
                    duplicate[i] = contacts[i]
    correct_list.append(contacts)

for contacts in correct_list:
    for duplicate in correct_list:
        if duplicate[0] == contacts[0] and duplicate != contacts:
            correct_list.remove(duplicate)

pprint(correct_list)


with open("phonebook.csv", "w", encoding='utf-8') as f:
    datawriter = csv.writer(f, delimiter=',')
    datawriter.writerows(correct_list)
