import pandas as pd

def preprocess(df,df_region):
    #filtering for summer olympics
    df =df[df['Season']=='Summer']
    #merge with df_region
    df=df.merge(df_region,on='NOC',how='left')
    #dropping duplicates
    df.drop_duplicates(inplace=True)
    #one hot encoding medals
    df= pd.concat([df,pd.get_dummies(df['Medal'])],axis=1)
    return df
    
    
    
    
    
    
    