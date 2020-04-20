# Data Science Pipeline
## Project Planning
Goal: leave this section with (at least the outline of) a plan for the project in the form of a README.md file.

Brainstorming ideas, hypotheses, related to how variables might impact or relate to each other, both within independent variables and between the independent variables and dependent variable, and also related to any ideas for new features you may have while first looking at the existing variables and challenge ahead of you.

Have a detailed README.md file for anyone who wants to check out your project. In this file should be a description of what the project is, and any instructions necessary for someone else to clone your project and run the code on their own laptop.

During project planning, think about what things in your project are nice to have, versus which things are need to have. For example, you might document that you will only worry about trying to scale your features after creating and evaluating a baseline model.

## Acquire
Goal: leave this section with a dataframe ready to prepare.

**write python script to:**
- test for zillow.csv existence
- import into zillow dataframe, data from SQL
- import into fips dataframe, data from fips.txt
- merge zillow and fips dataframes on fips
- create zillow.csv
 
**acquire.py**
- csv_exist()
- get_zillow_sql()
- get_zillow_url()
- get_zillow_data()
- get_zillow_csv()
- get_fips()
- merge_dfs(zdf, fips_df)
- generate_csv()
- acquire_data()


## Prep
Goal: leave this section with a dataset that is split into train and test ready to be analyzed. Data types are appropriate, missing values have been addressed, as have any data integrity issues.

**write python script to:**
- fill in missing bedroom and bathroom values
- create county_tax_property_value_mean
- create county_tax_rate_mean

**prep.py**
- clean_df(df)
- get_county_tax_property_value_mean(df)
- get_county_tax_rate_mean(df, county_tax_property_value_mean)


## Data Exploration
Goal: Address each of the questions you posed in your planning and brainstorming and any others you have come up with along the way through visual or statistical analysis.

- write hypothesis


Run at least 1 t-test and 1 correlation test (but as many as you need!)
Visualize all combinations of variables in some way(s).
What independent variables are correlated with the dependent?
Which independent variables are correlated with other independent variables?
Make sure to summarize your takeaways and conclusions. That is, the data science zillow team doesn't want to see just a bunch of dataframes/numbers/charts without any explanation, you should explain in the notebook what these dataframes/numbers/charts mean.


## Modeling
Goal: develop a regression model that performs better than a baseline.

You must evaluate a baseline model, and show how the model you end up with performs better than that.

Your notebook will contain various algorithms and/or hyperparameters tried, along with the evaluation code and results, before settling on the final algorithm.

Be sure and evaluate your model using the standard techniques: plotting the residuals, computing the evaluation metric (SSE, RMSE, and/or MSE), comparing to baseline, plotting y by ^y.

model.py: will have the functions to fit, predict and evaluate the final model on the test data set.

- For some additional options see sklearn's linear models and sklearn's page on supervised learning.

- After developing a baseline model, you can do some feature engineering and answer questions like:

- Which features should be included in your model?
- Are there new features you could create based on existing features that might be helpful?
- Are there any features that aren't adding much value?
- Here you could also use automated feature selection techniques to determine which features to put into your model.

- Be sure that any transformation that you apply to your training dataframe are reproducible, that is, the same transformations can be applied to your test dataset.


