import csv

input_file = 'security_incidents.csv'
output_file = 'output.csv'


with open(input_file, mode='r') as infile:
    reader = csv.reader(infile)
    data = list(reader)


header = data[0]
if 'Status' not in header:
    header.append('Status')

    rows = [row + ['Pending'] for row in data[1:]]
else:
    rows = data[1:]

with open(output_file, mode='w', newline='') as outfile:
    writer = csv.writer(outfile)
    writer.writerow(header)
    writer.writerows(rows)

print(f"Modified data saved to '{output_file}'")