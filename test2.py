import os
import csv
from more_itertools import chunked


def file_conversion(input_file, output_file_pattern, chunksize):
    output_filenames = []
    with open(input_file) as fin:
        reader = csv.reader(fin, delimiter=',')
        for i, chunk in enumerate(chunked(reader, chunksize)):
            output_filename = output_file_pattern.format(i)
            with open(output_filename, 'w', newline='') as fout:
                output_filenames.append(output_filename)
                writer = csv.writer(fout, reader, delimiter='|')

                writer.writerows(chunk)
                # print("Successfully converted into", output_file)
    return output_filenames

script_dir = os.path.dirname(os.path.abspath(__file__))
dest_dir = os.path.join(script_dir, 'temp')
try:
     os.makedirs(dest_dir)
except OSError:
     pass
path = os.path.join(dest_dir,'out{:03}.csv' )

paths = file_conversion('IPROD_current.csv', path, 10000)
x = paths[0]
print(type(x))
# base_names = [os.path.basename(path) for path in paths]
# # for x in range(len(base_names)):
# #     print (base_names[x])
# base_name = base_names[0]
# print(base_name)