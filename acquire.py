import os.path
import pandas as pd
import numpy as np 
import env

def csv_exist():
    return os.path.isfile('zillow.csv')


def get_zillow_sql():
     return '''
        select 
            bathroomcnt as bedroom_count,
            bedroomcnt as bathroom_count,
            calculatedfinishedsquarefeet as total_sqft,
            taxvaluedollarcnt as tax_property_value,
            taxamount as tax_amount,
            fips
        from `properties_2017`
        join `predictions_2017`using(`parcelid`)
        where propertylandusetypeid = 261 and `transactiondate` >= '2017-05-01' and `transactiondate` <= '2017-06-30'
    '''
    
def get_zillow_url():
    return f'mysql+pymysql://{env.user}:{env.password}@{env.host}/zillow'

    
def get_zillow_data():
    zdf = pd.read_sql(get_zillow_sql(), get_zillow_url())
    print('- CodeUp_db successfully accessed ...')
    print('- Zillow SQL query successful ...')
    
    return zdf


def get_zillow_csv():
    df = pd.read_table('zillow.csv')
    df.drop(columns=['Unnamed: 0'], inplace=True)
    return df


def get_fips():
    fips_df = pd.read_table('FIPS.txt')
    print('- fips_df dataframe successfully created.')
    return fips_df
    

def merge_dfs(zdf, fips_df):
    print('- merging zillow_df and fips_df ...')
    mdf = pd.merge(left=zdf, right=fips_df, left_on='fips', right_on='fips')
    mdf.rename(columns={'name':'county', 'state':'state'}, inplace=True)
    return mdf


def generate_csv():
    if csv_exist():
        print('- csv already exist')
    else:
        df = merge_dfs(get_zillow_data(), get_fips())
        print('- merge successful, creating zillow.csv')
        df.to_csv('zillow.csv')
        print('- zillow.csv successfully created')
              
              
def acquire_data():
    print('Acquiring data ...\n')
    generate_csv()
    print('\nData has been acquired')
    df = pd.read_csv('zillow.csv')
    df.drop(columns=['Unnamed: 0'], inplace=True)
    return df
    