import csv
import re

reg_with_dop = r'(?:\+7|8)(\d{3})(\d{3})(\d{2})(\d{2})доб\.(\d{4})'
tmp_with_dop = r'+7(\1)\2-\3-\4 доб.\5'

reg_without_dop = r'(?:\+7|8)(\d{3})(\d{3})(\d{2})(\d{2})'
tmp_without_dop = r'+7(\1)\2-\3-\4'

with open('phonebook_raw.csv', encoding='utf-8') as file:
    reader = csv.DictReader(file).reader
    fields = next(reader)
    for line in reader:
        line = ' '.join(line[:3]).split() + line[3:]
        number = line[5].replace(
            ' ',''
        ).replace(")",'').replace('(','').replace('-','')
        if len(number.split('доб.')) == 2:
            line[5] = re.sub(reg_with_dop, tmp_with_dop, number)
        else:
            line[5] = re.sub(reg_without_dop, tmp_without_dop, number)
        print(line)

def remove_duplicates(reader):
    result_dict = {}
    for row in correct_data(reader):
        key = ' '.join(row[:2])
        data_dict = {'surname': row[2], 'organization': row[3], 'position': row[4], 'phone': row[5], 'email': row[6]}
        if result_dict.get(key):
            for value in result_dict.get(key):
                if row[2] in value.get('surname'):
                    value.update({key: data_dict.get(key) for key in value if not value.get(key)})
                else:
                    result_dict.get(key).append(data_dict)
        else:
            result_dict[key] = [data_dict]
    return result_dict


