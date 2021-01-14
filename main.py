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


data = pd.read_csv(input_file, delimiter = ',')

# final_df = df.reindex(['CONTNUM','MFGPART','PRODNAME','PSC_CODE','GSAPRICE','ISSCODE','QTY_UNIT','VENDPART','OEM_CAGE','MFGNAME','PRODDESC','P_DELIV','PRODDESC','UPC','HAZMAT','TPRSTART','TPRSTOP','TEMPRICE','SHIPPING_STANDARD','SHIPPING_EXPEDITED','SHIPPING_NEXTDAY','EPI','EPJC','ESI','ESJC','USAI','USJC','CI'],axis=1)
def mapping(df):
    for column_name, column in df.transpose().iterrows():
        df = df.rename(columns={'PART_NUMBER': 'VENDPART', 'PART_NAME':'PRODNAME', 'PSC':'PSC_CODE',
                           'Contract Price with IFF': 'GSAPRICE','UNIT_OF_ISSUE':'ISSCODE','ITEMS_PER_UOI':'QTY_UNIT',
                           'OEM_NUMBER':'MFGPART','OEM_CAGE':'OEM_CAGE','OEM_NAME':'MFGNAME','DESCRIPTION':'PRODDESC',
                           'DAYS_ARO':'P_DELIV','LONG_DESCRIPTION':'LONG_DESCRIPTION','UPC':'UPC','HAZMAT':'HAZMAT','TPRSTART':'TPRSTART','TPRSTOP':'TPRSTOP',
                           'TEMPRICE':'TEMPRICE', 'SHIPPING_STANDARD':'SHIPPING','SHIPPING_EXPEDITED':'SHIPPING_EXPEDITED',
                           'SHIPPING_NEXTDAY':'SHIPPING_NEXTDAY',
                           'Environmentally Preferred Indicator': 'Environmentally Preferred Indicator',
                           'Environmentally Preferred Justifying Comment':'Environmentally Preferred Justifying Comment',
                           'Energy Star Indicator': 'Energy Star Indicator',
                           'Energy Star Justifying Comment':'Energy Star Justifying Comment',
                           'Made in the USA Indicator':'Made in the USA Indicator',
                           'Made in the USA Justifying Comment':'Made in the USA Justifying Comment',
                           'Characteristic Information':'Characteristic Information'})
        df = df.rename(columns={'VENDPART': 'VENDPART', 'PRODNAME': 'PRODNAME', 'PSC_CODE': 'PSC_CODE',
                           'Contract  Price with IFF': 'GSAPRICE', 'UNIT OF ISSUE': 'ISSCODE',
                           'Quantity per Unit of Issue': 'QTY_UNIT',
                           'MFGPART': 'MFGPART', 'OEM_CAGE': 'OEM_CAGE', 'OEM NAME': 'MFGNAME',
                           'PRODESC': 'PRODDESC',
                           'ARO': 'P_DELIV', 'LONG_DESCRIPTION':'LONG_DESCRIPTION','UPC': 'UPC', 'HAZMAT': 'HAZMAT', 'TPRSTART': 'TPRSTART',
                           'TPRSTOP': 'TPRSTOP',
                           'TEMPRICE': 'TEMPRICE', 'SHIPPING_STANDARD': 'SHIPPING',
                           'SHIPPING_EXPEDITED': 'SHIPPING_EXPEDITED',
                           'SHIPPING_NEXTDAY': 'SHIPPING_NEXTDAY',
                           'Environmentally Preferred Indicator': 'Environmentally Preferred Indicator',
                           'Environmentally Preferred Justifying Comment': 'Environmentally Preferred Justifying Comment',
                           'Energy Star Indicator': 'Energy Star Indicator',
                           'Energy Star Justifying Comment': 'Energy Star Justifying Comment',
                           'Made in the USA Indicator': 'Made in the USA Indicator',
                           'Made in the USA Justifying Comment': 'Made in the USA Justifying Comment',
                           'Characteristic Information': 'Characteristic Information'})
        df = df.rename(columns={'Contractor PN': 'VENDPART', 'PRODUCT_NAME': 'PRODNAME', 'PSC_CODE': 'PSC_CODE',
                           'CONTRACT PRICE WITH IFF': 'GSAPRICE', 'Unit of Issue': 'ISSCODE',
                           'Quantity per Unit of Issue': 'QTY_UNIT',
                           'OEM NUMBER': 'MFGPART', 'OEM_CAGE': 'OEM_CAGE', 'OEM NAME': 'MFGNAME',
                           'Product Description': 'PRODDESC',
                           'LEAD TIME DAYS': 'P_DELIV', 'LONG_DESCRIPTION':'LONG_DESCRIPTION','UPC': 'UPC', 'HAZMAT': 'HAZMAT', 'TPRSTART': 'TPRSTART',
                           'TPRSTOP': 'TPRSTOP',
                           'TEMPRICE': 'TEMPRICE', 'SHIPPING_STANDARD': 'SHIPPING',
                           'SHIPPING_EXPEDITED': 'SHIPPING_EXPEDITED',
                           'SHIPPING_NEXTDAY': 'SHIPPING_NEXTDAY',
                           'Environmentally Preferred Indicator': 'Environmentally Preferred Indicator',
                           'Environmentally Preferred Justifying Comment': 'Environmentally Preferred Justifying Comment',
                           'Energy Star Indicator': 'Energy Star Indicator',
                           'Energy Star Justifying Comment': 'Energy Star Justifying Comment',
                           'Made in the USA Indicator': 'Made in the USA Indicator',
                           'Made in the USA Justifying Comment': 'Made in the USA Justifying Comment',
                           'Characteristic Information': 'Characteristic Information'})
        df = df.rename(columns={'Contractor Part Number': 'VENDPART', 'Product Name': 'PRODNAME', 'PSC': 'PSC_CODE',
                           'PRICE': 'GSAPRICE', 'ISSCODE': 'ISSCODE',
                           'QTY_UNIT': 'QTY_UNIT',
                           'MANUFACTURER PART NUMBER': 'MFGPART', 'OEM_CAGE': 'OEM_CAGE', 'MANUFACTURER': 'MFGNAME',
                           'PRODUCT DESCRIPTION': 'PRODDESC',
                           'P_DELIV': 'P_DELIV', 'LONG_DESCRIPTION':'LONG_DESCRIPTION','UPC': 'UPC', 'HAZMAT': 'HAZMAT', 'TPRSTART': 'TPRSTART',
                           'TPRSTOP': 'TPRSTOP',
                           'TEMPRICE': 'TEMPRICE', 'SHIPPING_STANDARD': 'SHIPPING',
                           'SHIPPING_EXPEDITED': 'SHIPPING_EXPEDITED',
                           'SHIPPING_NEXTDAY': 'SHIPPING_NEXTDAY',
                           'Environmentally Preferred Indicator': 'Environmentally Preferred Indicator',
                           'Environmentally Preferred Justifying Comment': 'Environmentally Preferred Justifying Comment',
                           'Energy Star Indicator': 'Energy Star Indicator',
                           'Energy Star Justifying Comment': 'Energy Star Justifying Comment',
                           'Made in the USA Indicator': 'Made in the USA Indicator',
                           'Made in the USA Justifying Comment': 'Made in the USA Justifying Comment',
                           'Characteristic Information': 'Characteristic Information'})
        df = df.rename(columns={'VENDPART': 'VENDPART', 'PRODUCT NAME/DESCRIPTION': 'PRODNAME', 'PSC_CODE': 'PSC_CODE',
                           'Price': 'GSAPRICE', 'UOM': 'ISSCODE',
                           'QTY_UNIT': 'QTY_UNIT',
                           'Manufacturer Part #': 'MFGPART', 'OEM_CAGE': 'OEM_CAGE', 'MANUFACTURER NAME': 'MFGNAME',
                           'PRODDESC': 'PRODDESC',
                           'Lead Time Days': 'P_DELIV', 'LONG_DESCRIPTION':'LONG_DESCRIPTION','UPC': 'UPC', 'HAZMAT': 'HAZMAT', 'TPRSTART': 'TPRSTART',
                           'TPRSTOP': 'TPRSTOP',
                           'TEMPRICE': 'TEMPRICE', 'SHIPPING': 'SHIPPING',
                           'SHIPPING_EXPEDITED': 'SHIPPING_EXPEDITED',
                           'SHIPPING_NEXTDAY': 'SHIPPING_NEXTDAY',
                           'Environmentally Preferred Indicator': 'Environmentally Preferred Indicator',
                           'Environmentally Preferred Justifying Comment': 'Environmentally Preferred Justifying Comment',
                           'Energy Star Indicator': 'Energy Star Indicator',
                           'Energy Star Justifying Comment': 'Energy Star Justifying Comment',
                           'Made in the USA Indicator': 'Made in the USA Indicator',
                           'Made in the USA Justifying Comment': 'Made in the USA Justifying Comment',
                           'Characteristic Information': 'Characteristic Information'})
        df = df.rename(columns={'VENDPART': 'VENDPART', 'PRODNAME': 'PRODNAME', 'PSC_CODE': 'PSC_CODE',
                           'GSAPRICE': 'GSAPRICE', 'ISSCODE': 'ISSCODE',
                           'QTY_UNIT': 'QTY_UNIT',
                           'MFGPART': 'MFGPART', 'OEM_CAGE': 'OEM_CAGE', 'Manufacturer Name': 'MFGNAME',
                           'PRODDESC': 'PRODDESC',
                           'Lead Time Days': 'P_DELIV', 'LONG_DESCRIPTION':'LONG_DESCRIPTION','UPC': 'UPC', 'HAZMAT': 'HAZMAT', 'TPRSTART': 'TPRSTART',
                           'TPRSTOP': 'TPRSTOP',
                           'TEMPRICE': 'TEMPRICE', 'SHIPPING': 'SHIPPING',
                           'SHIPPING_EXPEDITED': 'SHIPPING_EXPEDITED',
                           'SHIPPING_NEXTDAY': 'SHIPPING_NEXTDAY',
                           'Environmentally Preferred Indicator': 'Environmentally Preferred Indicator',
                           'Environmentally Preferred Justifying Comment': 'Environmentally Preferred Justifying Comment',
                           'Energy Star Indicator': 'Energy Star Indicator',
                           'Energy Star Justifying Comment': 'Energy Star Justifying Comment',
                           'Made in the USA Indicator': 'Made in the USA Indicator',
                           'Made in the USA Justifying Comment': 'Made in the USA Justifying Comment',
                           'Characteristic Information': 'Characteristic Information'})
        df = df.rename(columns={'VENDPART': 'VENDPART', 'PRODNAME': 'PRODNAME', 'PSC_CODE': 'PSC_CODE',
                           'Contract Price': 'GSAPRICE', 'ISSCODE': 'ISSCODE',
                           'QTY_UNIT': 'QTY_UNIT',
                           'MFGPART': 'MFGPART', 'OEM_CAGE': 'OEM_CAGE', 'MANUFACTURER OR BRAND NAME': 'MFGNAME',
                           'PRODDESC': 'PRODDESC',
                           'Lead Time Days': 'P_DELIV', 'LONG_DESCRIPTION':'LONG_DESCRIPTION','UPC': 'UPC', 'HAZMAT': 'HAZMAT', 'TPRSTART': 'TPRSTART',
                           'TPRSTOP': 'TPRSTOP',
                           'TEMPRICE': 'TEMPRICE', 'SHIPPING': 'SHIPPING',
                           'SHIPPING_EXPEDITED': 'SHIPPING_EXPEDITED',
                           'SHIPPING_NEXTDAY': 'SHIPPING_NEXTDAY',
                           'Environmentally Preferred Indicator': 'Environmentally Preferred Indicator',
                           'Environmentally Preferred Justifying Comment': 'Environmentally Preferred Justifying Comment',
                           'Energy Star Indicator': 'Energy Star Indicator',
                           'Energy Star Justifying Comment': 'Energy Star Justifying Comment',
                           'Made in the USA Indicator': 'Made in the USA Indicator',
                           'Made in the USA Justifying Comment': 'Made in the USA Justifying Comment',
                           'Characteristic Information': 'Characteristic Information'})
        df = df.rename(columns={'VENDPART': 'VENDPART', 'PRODUCT NAME': 'PRODNAME', 'PSC_CODE': 'PSC_CODE',
                           'CONTRACT PRICE': 'GSAPRICE', 'ISSCODE': 'ISSCODE',
                           'QTY_UNIT': 'QTY_UNIT',
                           'MFGPART': 'MFGPART', 'OEM_CAGE': 'OEM_CAGE', 'MANUFACTURER OR BRAND NAME': 'MFGNAME',
                           'PRODDESC': 'PRODDESC',
                           'Lead Time Days': 'P_DELIV', 'LONG_DESCRIPTION':'LONG_DESCRIPTION','UPC': 'UPC', 'HAZMAT': 'HAZMAT', 'TPRSTART': 'TPRSTART',
                           'TPRSTOP': 'TPRSTOP',
                           'TEMPRICE': 'TEMPRICE', 'SHIPPING': 'SHIPPING',
                           'SHIPPING_EXPEDITED': 'SHIPPING_EXPEDITED',
                           'SHIPPING_NEXTDAY': 'SHIPPING_NEXTDAY',
                           'Environmentally Preferred Indicator': 'Environmentally Preferred Indicator',
                           'Environmentally Preferred Justifying Comment': 'Environmentally Preferred Justifying Comment',
                           'Energy Star Indicator': 'Energy Star Indicator',
                           'Energy Star Justifying Comment': 'Energy Star Justifying Comment',
                           'Made in the USA Indicator': 'Made in the USA Indicator',
                           'Made in the USA Justifying Comment': 'Made in the USA Justifying Comment',
                           'Characteristic Information': 'Characteristic Information'})
    return df





        # df.rename(columns={'alias': 'FNAME', 'contact': 'EMAIL'}, inplace=True)
        # df.rename(columns={'initial name': 'FNAME', 'emailid': 'EMAIL'}, inplace=True)
first_df= mapping(data)
initial_df = first_df.reindex(['SIN','VENDPART','PRODNAME','PSC_CODE','GSAPRICE','ISSCODE','QTY_UNIT','MFGPART','OEM_CAGE','MFGNAME','PRODDESC','P_DELIV','LONG_DESCRIPTION','UPC','HAZMAT','TPRSTART','TPRSTOP','TEMPRICE','SHIPPING_STANDARD','SHIPPING_EXPEDITED','SHIPPING_NEXTDAY','Environmentally Preferred Indicator','Environmentally Preferred Justifying Comment','Energy Star Indicator','Energy Star Justifying Comment','Made in the USA Indicator','Made in the USA Justifying Comment','Characteristic Information'],axis=1)

final_df = initial_df.reindex(['VENDPART','PRODNAME','PSC_CODE','GSAPRICE','ISSCODE','QTY_UNIT','MFGPART','OEM_CAGE','MFGNAME','PRODDESC','P_DELIV','LONG_DESCRIPTION','UPC','HAZMAT','TPRSTART','TPRSTOP','TEMPRICE','SHIPPING_STANDARD','SHIPPING_EXPEDITED','SHIPPING_NEXTDAY','Environmentally Preferred Indicator','Environmentally Preferred Justifying Comment','Energy Star Indicator','Energy Star Justifying Comment','Made in the USA Indicator','Made in the USA Justifying Comment','Characteristic Information'],axis=1)

df2 = pd.read_csv('sin_psc_table.csv',delimiter=',')
initial_df['SIN'] = initial_df['SIN'].astype(str)
initial_df['SIN'] = initial_df['SIN'].str.replace(' ','')
df2dict = df2.set_index(['SIN'])['PSC_CODE'].squeeze().to_dict()
final_df['PSC_CODE'] = final_df['PSC_CODE'].fillna(initial_df['SIN'].map(df2dict))

final_df['P_DELIV'] = final_df['P_DELIV'].fillna('5')
final_df['ISSCODE'] = final_df['ISSCODE'].fillna('EA')
final_df.loc[final_df['UPC'].astype(str).str.len() >12, 'UPC']= ''
final_df.loc[final_df['TEMPRICE'] == 0,'TEMPRICE']=''
final_df['QTY_UNIT'] = final_df['QTY_UNIT'].fillna('0')
final_df['QTY_UNIT'] = final_df['QTY_UNIT'].astype(int)
final_df['VENDPART'] = final_df['VENDPART'].astype(str).str.replace('+','-PLUS')
final_df['VENDPART'] = final_df['VENDPART'].astype(str).str.replace('/','-SLASH-')
final_df['VENDPART'] = final_df['VENDPART'].astype(str).str.replace('\\','-SLASH-')
final_df['VENDPART'] = final_df['VENDPART'].astype(str).str.replace(' ','-')
final_df['VENDPART'] = final_df['VENDPART'].astype(str).str.replace('_','-')
final_df['VENDPART'] = final_df['VENDPART'].astype(str).str.replace('.','-')
final_df['VENDPART'] = final_df['VENDPART'].astype(str).str.replace('"','')
final_df['VENDPART'] = final_df['VENDPART'].astype(str).str.replace('(','')
final_df['VENDPART'] = final_df['VENDPART'].astype(str).str.replace(')','')
final_df['VENDPART'] = final_df['VENDPART'].astype(str).str.replace('%','-')
final_df['GSAPRICE'] = final_df['GSAPRICE'].round(2)
final_df['GSAPRICE'] = final_df['GSAPRICE'].astype(str).str.replace('$','')
final_df['GSAPRICE'] = final_df['GSAPRICE'].astype(str).str.replace(',','')

final_df['VENDPART'] = final_df['VENDPART'].fillna(final_df['MFGPART'])
final_df['MFGPART'] = final_df['MFGPART'].fillna(final_df['VENDPART'])
final_df['PRODDESC'] = final_df['PRODDESC'].astype(str).str.replace('   ',' ')
final_df['PRODDESC'] = final_df['PRODDESC'].astype(str).str.replace('  ',' ')
final_df['LONG_DESCRIPTION'] = final_df['PRODDESC'].fillna('')
final_df['LONG_DESCRIPTION'] = final_df['LONG_DESCRIPTION'].astype(str).str.replace('   ',' ')
final_df['PRODDESC'] = final_df['PRODDESC'].astype(str).str.replace('#','-')
final_df['PRODDESC'] = final_df['PRODDESC'].astype(str).str.replace('[','-')
final_df['PRODDESC'] = final_df['PRODDESC'].astype(str).str.replace(']','-')
final_df['PRODDESC'] = final_df['PRODDESC'].astype(str).str.replace('[','-')
final_df['PRODDESC'] = final_df['PRODDESC'].astype(str).str.replace('ï¿½','-')
final_df['LONG_DESCRIPTION'] = final_df['LONG_DESCRIPTION'].astype(str).str.replace('#','-')
final_df['LONG_DESCRIPTION'] = final_df['LONG_DESCRIPTION'].astype(str).str.replace('[','-')
final_df['LONG_DESCRIPTION'] = final_df['LONG_DESCRIPTION'].astype(str).str.replace(']','-')
final_df['LONG_DESCRIPTION'] = final_df['LONG_DESCRIPTION'].astype(str).str.replace('[','-')
final_df['LONG_DESCRIPTION'] = final_df['LONG_DESCRIPTION'].astype(str).str.replace('ï¿½','-')
log1_df = initial_df.reindex(['PART_NAME','OEM_NAME','OEM_NUMBER','NEW_OEM_NUMBER','PART_NUMBER','NEW_PART_NUMBER'],axis= 1)

log1_df['PART_NAME'] = final_df['PRODNAME']
log1_df['OEM_NAME'] = final_df['MFGNAME']
log1_df['OEM_NUMBER'] = initial_df['MFGPART']
log1_df['NEW_OEM_NUMBER'] = final_df['MFGPART']
log1_df['PART_NUMBER'] = initial_df['VENDPART']
log1_df['NEW_PART_NUMBER'] = final_df['VENDPART']

log2_df = initial_df.loc[initial_df['UPC'].astype(str).str.len() >12 ]
log2_df = initial_df.reindex(['PART_NAME','OEM_NAME','OEM_NUMBER','NEW_OEM_NUMBER','PART_NUMBER','NEW_PART_NUMBER','UPC','COMMENT'],axis= 1)
log2_df['PART_NAME'] = final_df['PRODNAME']
log2_df['OEM_NAME'] = final_df['MFGNAME']
log2_df['OEM_NUMBER'] = initial_df['MFGPART']
log2_df['NEW_OEM_NUMBER'] = final_df['MFGPART']
log2_df['PART_NUMBER'] = initial_df['VENDPART']
log2_df['NEW_PART_NUMBER'] = final_df['VENDPART']
log2_df['COMMENT'] = log2_df['COMMENT'].fillna('toolong')

log3_df = initial_df.reindex(['PART_NUMBER','PART_NAME','OEM_NAME','ORIGINAL_PRICE','DISCOUNT_PRICE'], axis=1)
log3_df['PART_NUMBER'] = final_df['VENDPART']
log3_df['PART_NAME'] = final_df['PRODNAME']
log3_df['OEM_NAME']= final_df['MFGNAME']
log3_df['ORIGINAL_PRICE'] = final_df['GSAPRICE']
log3_df['DISCOUNT_PRICE'] = final_df['GSAPRICE']

log4_df = final_df.set_axis(fed_headers[0:27],axis=1)
log4_df = log4_df.loc[initial_df['PSC_CODE']=='']


log5_df = final_df.set_axis(fed_headers[0:27],axis=1)
log5_df = log5_df.loc[initial_df['SIN']=='']




#
# # final_df = df.iloc[:,[0,1,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28]]
#
script_dir0 = os.path.dirname(os.path.abspath(__file__))
dest0 = os.path.join(script_dir0, 'excess')
try:
    os.makedirs(dest0)
except OSError:
    pass
path0 = os.path.join(dest0,cc+'.csv' )
final_df.to_csv(path0,index = False)
log1_df.to_csv('logschanged1.csv',index = False)
log2_df.to_csv('logschanged2.csv',index = False)
log3_df.to_csv('logschanged3.csv',index = False)
log4_df.to_csv('logschanged4.csv',index = False)
log5_df.to_csv('logschanged5.csv',index = False)
# path0 = cc+'.csv'

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

def add_column_in_csv(input_file, output_file, transform_row,transform_row1,transform_row2):
    with open(input_file, 'r') as read_obj, \
            open(output_file, 'w', newline='') as write_obj:
        reader = csv.reader(read_obj,delimiter=',')
        writer = csv.writer(write_obj)
        for row in reader:

            transform_row(row,reader.line_num)
            transform_row1(row,reader.line_num)
            transform_row2(row,reader.line_num)
            writer.writerow(row)
        # writer.writerows([map,(operator.itemgetter(0,1,2,3,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30),reader)])
script_dir1 = os.path.dirname(os.path.abspath(__file__))
dest = os.path.join(script_dir1, 'excess')
try:
    os.makedirs(dest)
except OSError:
    pass
path1 = os.path.join(dest,cn+'.csv' )
add_column_in_csv(path0,path1, lambda row, line_num: row.insert(0, act),lambda row, line_num: row.insert(1,cc),lambda row, line_num: row.insert(2,cn))
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
# def total_lines(input_file):
#     with open(input_file) as f:
#         return sum(1 for line in f)

script_dir = os.path.dirname(os.path.abspath(__file__))
dest_dir = os.path.join(script_dir, 'temp')
try:
    os.makedirs(dest_dir)
except OSError:
    pass
path = os.path.join(dest_dir,cn+'{:06}.csv' )

# pyth
file_conversion(path1,path,10000,act,cc,cn)



