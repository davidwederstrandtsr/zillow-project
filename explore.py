import pandas as pd
import numpy as np
import seaborn as sns
from scipy import stats
from pandas_profiling import ProfileReport
from pydataset import data
import matplotlib.pyplot as plt


def plot_variable_pairs(df, hue=None):
    g = sns.pairplot(df, hue=hue, kind="reg", corner=True, diag_kind="kde",
        plot_kws=({'line_kws':{'color':'red'}, 'scatter_kws':{'alpha':0.7}}))
    g.fig.suptitle("Scattlerplot with Regression for Continuous Variables")
    plt.show()

def plot_categroical_and_continous_vars(categorical_var, continuous_var, df):
    sns.catplot(y=categorical_var, x=continuous_var, data=df)
    sns.catplot(x=continuous_var, kind="count", palette="ch:.25", data=df)
    sns.catplot(y=categorical_var, x=continuous_var, kind="box", data=df)
    sns.catplot(y=categorical_var, x=continuous_var, kind="violin", bw=.15, cut=0, data=df)

def get_pearsonr(x, y):
    return stats.pearsonr(x, y)

def t_test_county(df, county):
    c = df[df.county == '{county}']
    μ = df.tax_property_value.mean()
    xbar = c.tax_property_value.mean()
    s = c.tax_property_value.std()
    n = c.shape[0]
    degf = n - 1
    standard_error = s / sqrt(n)
    t = (xbar - μ) / (s / sqrt(n))
    p = stats.t(degf).sf(t) * 2 
    return t, p