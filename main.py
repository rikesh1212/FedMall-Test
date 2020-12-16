import os
import csv
from more_itertools import chunked
import pandas as pd





# declare fed_headers for output files

fed_headers = ['Item Master Primary Spec/Item Status Information/Archive',
               'Item Master Primary Spec/Common Information/Commercial and Government Entity Code',
               'Item Master Primary Spec/Common Information/Contract Number',
               'Item Master Primary Spec/Common Information/Part Number',
               'Item Master Primary Spec/Common Information/Part Name',
               'Item Master Primary Spec/Common Information/Federal Supply Class',
               'Item Master Primary Spec/Pricing/Original Unit Price',
               'Item Master Primary Spec/Pricing/Original Unit of Issue',
               'Item Master Primary Spec/Pricing/Quantity Per Unit Pack',
               'Item Master Primary Spec/Common Information/Original Equipment Manufacturer Part Number',
               'Item Master Primary Spec/Common Information/Original Equipment Manufacturer CAGE Code',
               'Item Master Primary Spec/Common Information/Original Equipment Manufacturer Name',
               'Item Master Primary Spec/Short Description',
               'Item Master Primary Spec/Common Information/Days After Receipt of Order',
               'Item Master Primary Spec/Long Description',
               'Item Master Primary Spec/Common Information/Universal Product Code',
               'Item Master Primary Spec/Commercial Information/Environmental Information/Hazardous Material Flag',
               'Item Master Primary Spec/Sale Pricing/Sale Start Date',
               'Item Master Primary Spec/Sale Pricing/Sale End Date',
               'Item Master Primary Spec/Sale Pricing/Sale Price',
               'Item Master Primary Spec/Commercial Information/Shipping Information/Shipment Level of Service/Standard Shipment Price',
               'Item Master Primary Spec/Commercial Information/Shipping Information/Shipment Level of Service/Expedited Shipment Price',
               'Item Master Primary Spec/Commercial Information/Shipping Information/Shipment Level of Service/Next Day Shipment Price',
               'Item Master Primary Spec/Special Properties/Environmentally Preferred/Environmentally Preferred Indicator',
               'Item Master Primary Spec/Special Properties/Environmentally Preferred/Justifying Comment',
               'Item Master Primary Spec/Special Properties/Energy Star/Energy Star Indicator',
               'Item Master Primary Spec/Special Properties/Energy Star/Justifying Comment',
               'Item Master Primary Spec/Special Properties/Made in the USA/Made in the USA Indicator',
               'Item Master Primary Spec/Special Properties/Made in the USA/Justifying Comment',
               'Item Master Primary Spec/Characteristic Information' ]
# input compulsory arguments
cc = input("Enter Cage Code \t")
cn = input("Enter Contract Number \t")
input_file = input("Enter input file \t")
act = input("Enter Action (Update- N/Delete -Y) \t")
# output_file = input("Enter Output file")

# print Cage Code and Contract Number
print("Cage Code:",cc)
print("Contract Number:",cn)


df = pd.read_csv(input_file, delimiter = ',')
final_df = df.iloc[:,[0,1,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28]]
final_df.to_csv(cc+'.csv',index = False)

path0 = cc+'.csv'

# file conversion from input file to output file

#
# def file_conversion(input_file, output_file):
#     with open(input_file) as fin:
#         with open(output_file, 'w', newline='') as fout:
#             reader = csv.DictReader(fin, delimiter=',')
#             writer = csv.DictWriter(fout, reader.fieldnames, delimiter='|')
#             writer.writeheader()
#             writer.writerows(reader)
#             print("Successfully converted into", output_file)


# def file_conversion(input_file, output_file_pattern, chunksize):
#     with open(input_file) as fin:
#         reader = csv.DictReader(fin, delimiter=',')
#
#         for i, chunk in enumerate(chunked(reader, chunksize)):
#             with open(output_file_pattern.format(i), 'w', newline='') as fout:
#                 writer = csv.DictWriter(fout,fieldnames=fed_headers,extrasaction='ignore',delimiter='^')
#                 writer.writeheader()
#                 writer.writerows(chunk)
#                 print("Successfully converted into", output_file_pattern)

def add_column_in_csv(input_file, output_file, transform_row,transform_row1):
    with open(input_file, 'r') as read_obj, \
            open(output_file, 'w', newline='') as write_obj:
        reader = csv.reader(read_obj,delimiter=',')
        writer = csv.writer(write_obj)
        for row in reader:

            transform_row(row,reader.line_num)
            transform_row1(row,reader.line_num)
            writer.writerow(row)
        # writer.writerows([map,(operator.itemgetter(0,1,2,3,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30),reader)])
script_dir1 = os.path.dirname(os.path.abspath(__file__))
dest = os.path.join(script_dir1, 'excess')
try:
    os.makedirs(dest)
except OSError:
    pass
path1 = os.path.join(dest,cn+'.csv' )
add_column_in_csv(path0,path1, lambda row, line_num: row.insert(0, act),lambda row, line_num: row.insert(1,cc))
# add_column_in_csv(input_file,cn+'{:06}.csv', lambda row, line_num: row.insert(1, cc))
# add_column_in_csv(input_file,cn+'{:06}.csv', lambda row, line_num: row.insert(2, cn))
#
#
#
#
#
def file_conversion(input_file, output_file_pattern, chunksize, act,cc,cn):

    with open(input_file,"r+") as fin:
        # ignore headers of input files
        for i in range(1):
            fin.__next__()
        reader = csv.reader(fin, delimiter=',')

        for i, chunk in enumerate(chunked(reader, chunksize)):
            with open(output_file_pattern.format(i), 'w', newline='') as fout:
                writer = csv.writer(fout,reader,delimiter='^')

                writer.writerow(fed_headers)
                # for node, row in enumerate(reader,1):
                #     row['invalid keyword'] = act^cc^cn
                #     writer.writerows(row)



                writer.writerows(chunk)
                print("Successfully converted into", output_file_pattern)

# count total number of lines
#
#
def total_lines(input_file):
    with open(input_file) as f:
        return sum(1 for line in f)

script_dir = os.path.dirname(os.path.abspath(__file__))
dest_dir = os.path.join(script_dir, 'temp')
try:
    os.makedirs(dest_dir)
except OSError:
    pass
path = os.path.join(dest_dir,cn+'{:06}.csv' )

print("Total Number of lines:",total_lines(input_file))
file_conversion(path1,path,10000,act,cc,cn)

#
#
