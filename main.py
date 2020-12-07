import csv
# input compulsory arguments
cc = input("Enter Cage Code")
cn = input("Enter Contract Number")
input_file = input("Enter input file")
output_file = input("Enter Output file")

# print Cage Code and Contract Number
print("Cage Code:",cc)
print("Contract Number:",cn)

# file conversion from input file to output file


def file_conversion(input_file, output_file):
    with open(input_file) as fin:
        with open(output_file, 'w', newline='') as fout:
            reader = csv.DictReader(fin, delimiter=',')
            writer = csv.DictWriter(fout, reader.fieldnames, delimiter='|')
            writer.writeheader()
            writer.writerows(reader)
            print("Successfully converted into", output_file)

# count total number of lines


def total_lines(input_file):
    with open(input_file) as f:
        return sum(1 for line in f)


print("Total Number of lines:",total_lines(input_file))
file_conversion(input_file,output_file)



