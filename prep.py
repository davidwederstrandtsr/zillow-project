import numpy as np
import pandas as pd

def clean_df(df):
    '''
    Returns a cleaned Zillow dataframe:
    
        - missing bathroom and bedroom counts filled with the mean
          of the df for each column.
          
        - blanks are replaced by NaN and those columns are dropped.
        
        - tax_rate is calculated for each property, the mean for each 
          county will be calculated later.
          
        - fips column values coverted to int.
    '''
    print('Cleaning data ...\n')
    bathcount = round(df.bathroom_count.mean())
    bedcount = round(df.bedroom_count.mean())
    df.bathroom_count.replace(0, bathcount, inplace=True)
    df.bedroom_count.replace(0, bedcount, inplace=True)
    print("- bathroom and bedroom 0 counts corrected by the df.mean() for each.")
    df = df.replace(r'^\s*$', np.nan, regex=True)
    df = df.dropna(how='any')
    print("- dropped all rows containing a null")
    df['tax_rate'] = (df.tax_amount / df.tax_property_value).astype(float)
    print("- created tax_rate column")
    df = df.drop(columns=['fips'])
    print('\nZillow_df cleaned and ready for exploration')
    return df

def get_county_tax_property_value_mean(df):
    '''
    Returns the mean property tax value for each county
    
        - group by county.
    '''
    county_tax_property_value_mean = df.groupby(df.county).tax_property_value.mean()
    return county_tax_property_value_mean


def get_county_tax_rate_mean(df, county_tax_property_value_mean):
    '''
    Return the mean tax rate for each county
    '''
    county_tax_rate_mean = df.groupby(df.county).tax_rate.mean()
    county_tax_rate_mean = pd.DataFrame(county_tax_rate_mean)
    county_tax_rate_mean['county_tax_property_value_mean'] = county_tax_property_value_mean
    county_tax_rate_mean.reset_index(inplace=True)
    return county_tax_rate_mean

# def get_orange(df):
#     return pd.DataFrame((df.county == 'Orange').tax_rate)
