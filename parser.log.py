import re
from collections import Counter
import csv


def reader(filename):
    regexp = r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}'
    with open(filename) as f:
        log = f.read()
        ips_list = re.findall(regexp, log)
    return ips_list


def count(ips_list):
    counter = Counter(ips_list)
    # print(counter)
    return counter


def write_csv(counter):
    with open('output.csv', 'w') as csv_file:
        writer = csv.writer(csv_file)

        header = ['IP', 'Frequency']
        writer.writerow(header)
        for item in counter:
            writer.writerow((item, counter[item]))


if __name__ == '__main__':
    write_csv(count(reader('app.log')))
