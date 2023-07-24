import pandas as pd



def preprocessor(df,region_df):
    #filtring the summer olympics
    df = df[df['Season'] == 'Summer']
    # merge with region_df
    df =  df.merge(region_df, on='NOC', how='left')
    df.drop_duplicates(inplace=True)
    # one hot encoding medals
    df = pd.concat([df,pd.get_dummies(df['Medal']).astype(int)], axis=1)
    return df