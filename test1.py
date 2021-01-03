import pandas as pd

sample1 = pd.read_csv('sample1.csv')

def mapping(df):
    for column_name, column in df.transpose().iterrows():
        df = df.rename(columns ={'first name' : 'FNAME', 'email address': 'EMAIL'})
        df = df.rename(columns ={'alias' : 'FNAME', 'contact': 'EMAIL'})
        df = df.rename(columns ={'initial name' : 'FNAME', 'emailid': 'EMAIL'})
    return df

t = mapping(sample1)
print(t)
