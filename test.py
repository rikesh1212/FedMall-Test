# import pandas as pd
# import numpy as np
# df = pd.read_csv('sample1.csv',delimiter=',')
# dfn = pd.DataFrame(columns=['id', 'name', 'email'])
# for i in df:
#     cond_list = [
#         i.columns == 'id',
#         i.columns.str.contains('name|alias|first name|', na=False),
#         i.columns.str.contains('email|contact|email address', na=False)
#
#     ]
#     cols = [i.columns[cond][0] for cond in cond_list]
#     dfn = dfn.append(pd.DataFrame(i[cols].values, columns=dfn.columns))
# print(dfn)



def mapping(df):
    for column_name, column in df.transpose().iterrows():
        df.rename(columns={'PART_NUMBER': 'VENDPART', 'PART_NAME':'PRODNAME', 'PSC':'PSC_CODE',
                           'Contract Price with IFF': 'GSAPRICE','UNIT_OF_ISSUE':'ISSCODE','ITEMS_PER_UOI':'QTY_UNIT',
                           'OEM_NUMBER':'MFGPART','OEM_CAGE':'OEM_CAGE','OEM_NAME':'MFGNAME','DESCRIPTION':'PRODDESC',
                           'DAYS_ARO':'P_DELIV','UPC':'UPC','HAZMAT':'HAZMAT','TPRSTART':'TPRSTART','TPRSTOP':'TPRSTOP',
                           'TEMPRICE':'TEMPRICE', 'SHIPPING_STANDARD':'SHIPPING','SHIPPING_EXPEDITED':'SHIPPING_EXPEDITED',
                           'SHIPPING_NEXTDAY':'SHIPPING_NEXTDAY',
                           'Environmentally Preferred Indicator': 'Environmentally Preferred Indicator',
                           'Environmentally Preferred Justifying Comment':'Environmentally Preferred Justifying Comment',
                           'Energy Star Indicator': 'Energy Star Indicator',
                           'Energy Star Justifying Comment':'Energy Star Justifying Comment',
                           'Made in the USA Indicator':'Made in the USA Indicator',
                           'Made in the USA Justifying Comment':'Made in the USA Justifying Comment',
                           'Characteristic Information':'Characteristic Information'}, inplace=True)
        df.rename(columns={'VENDPART': 'VENDPART', 'PRODNAME': 'PRODNAME', 'PSC_CODE': 'PSC_CODE',
                           'Contract  Price with IFF': 'GSAPRICE', 'UNIT OF ISSUE': 'ISSCODE',
                           'Quantity per Unit of Issue': 'QTY_UNIT',
                           'MFGPART': 'MFGPART', 'OEM_CAGE': 'OEM_CAGE', 'OEM NAME': 'MFGNAME',
                           'PRODESC': 'PRODDESC',
                           'ARO': 'P_DELIV', 'UPC': 'UPC', 'HAZMAT': 'HAZMAT', 'TPRSTART': 'TPRSTART',
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
                           'Characteristic Information': 'Characteristic Information'}, inplace=True)
        df.rename(columns={'Contractor PN': 'VENDPART', 'PRODUCT_NAME': 'PRODNAME', 'PSC_CODE': 'PSC_CODE',
                           'CONTRACT PRICE WITH IFF': 'GSAPRICE', 'Unit of Issue': 'ISSCODE',
                           'Quantity per Unit of Issue': 'QTY_UNIT',
                           'OEM NUMBER': 'MFGPART', 'OEM_CAGE': 'OEM_CAGE', 'OEM NAME': 'MFGNAME',
                           'Product Description': 'PRODDESC',
                           'LEAD TIME DAYS': 'P_DELIV', 'UPC': 'UPC', 'HAZMAT': 'HAZMAT', 'TPRSTART': 'TPRSTART',
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
                           'Characteristic Information': 'Characteristic Information'}, inplace=True)
        df.rename(columns={'Contractor Part Number': 'VENDPART', 'Product Name': 'PRODNAME', 'PSC': 'PSC_CODE',
                           'PRICE': 'GSAPRICE', 'ISSCODE': 'ISSCODE',
                           'QTY_UNIT': 'QTY_UNIT',
                           'MANUFACTURER PART NUMBER': 'MFGPART', 'OEM_CAGE': 'OEM_CAGE', 'MANUFACTURER': 'MFGNAME',
                           'PRODUCT DESCRIPTION': 'PRODDESC',
                           'P_DELIV': 'P_DELIV', 'UPC': 'UPC', 'HAZMAT': 'HAZMAT', 'TPRSTART': 'TPRSTART',
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
                           'Characteristic Information': 'Characteristic Information'}, inplace=True)
        df.rename(columns={'VENDPART': 'VENDPART', 'PRODUCT NAME/DESCRIPTION': 'PRODNAME', 'PSC_CODE': 'PSC_CODE',
                           'Price': 'GSAPRICE', 'UOM': 'ISSCODE',
                           'QTY_UNIT': 'QTY_UNIT',
                           'Manufacturer Part #': 'MFGPART', 'OEM_CAGE': 'OEM_CAGE', 'MANUFACTURER NAME': 'MFGNAME',
                           'PRODDESC': 'PRODDESC',
                           'Lead Time Days': 'P_DELIV', 'UPC': 'UPC', 'HAZMAT': 'HAZMAT', 'TPRSTART': 'TPRSTART',
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
                           'Characteristic Information': 'Characteristic Information'}, inplace=True)
        df.rename(columns={'VENDPART': 'VENDPART', 'PRODNAME': 'PRODNAME', 'PSC_CODE': 'PSC_CODE',
                           'GSAPRICE': 'GSAPRICE', 'ISSCODE': 'ISSCODE',
                           'QTY_UNIT': 'QTY_UNIT',
                           'MFGPART': 'MFGPART', 'OEM_CAGE': 'OEM_CAGE', 'Manufacturer Name': 'MFGNAME',
                           'PRODDESC': 'PRODDESC',
                           'Lead Time Days': 'P_DELIV', 'UPC': 'UPC', 'HAZMAT': 'HAZMAT', 'TPRSTART': 'TPRSTART',
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
                           'Characteristic Information': 'Characteristic Information'}, inplace=True)
        df.rename(columns={'VENDPART': 'VENDPART', 'PRODNAME': 'PRODNAME', 'PSC_CODE': 'PSC_CODE',
                           'Contract Price': 'GSAPRICE', 'ISSCODE': 'ISSCODE',
                           'QTY_UNIT': 'QTY_UNIT',
                           'MFGPART': 'MFGPART', 'OEM_CAGE': 'OEM_CAGE', 'MANUFACTURER OR BRAND NAME': 'MFGNAME',
                           'PRODDESC': 'PRODDESC',
                           'Lead Time Days': 'P_DELIV', 'UPC': 'UPC', 'HAZMAT': 'HAZMAT', 'TPRSTART': 'TPRSTART',
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
                           'Characteristic Information': 'Characteristic Information'}, inplace=True)
        df.rename(columns={'VENDPART': 'VENDPART', 'PRODUCT NAME': 'PRODNAME', 'PSC_CODE': 'PSC_CODE',
                           'CONTRACT PRICE': 'GSAPRICE', 'ISSCODE': 'ISSCODE',
                           'QTY_UNIT': 'QTY_UNIT',
                           'MFGPART': 'MFGPART', 'OEM_CAGE': 'OEM_CAGE', 'MANUFACTURER OR BRAND NAME': 'MFGNAME',
                           'PRODDESC': 'PRODDESC',
                           'Lead Time Days': 'P_DELIV', 'UPC': 'UPC', 'HAZMAT': 'HAZMAT', 'TPRSTART': 'TPRSTART',
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
                           'Characteristic Information': 'Characteristic Information'}, inplace=True)






        # df.rename(columns={'alias': 'FNAME', 'contact': 'EMAIL'}, inplace=True)
        # df.rename(columns={'initial name': 'FNAME', 'emailid': 'EMAIL'}, inplace=True)
        






