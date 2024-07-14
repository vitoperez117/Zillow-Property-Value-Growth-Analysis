# Python US Home Values
The objective is to find neighborhoods with the fastest rising home values in order to assist potential real estate investors start their search. Realistically, real estate investment involves more than home value growth. However, this research provides a useful starting point.

### Understanding the Data
Zillow ZHVI time-series [dataset](https://drive.google.com/file/d/1SeR8qDqmhj0YHPOMiBU1zEbyaIjmAnga/view?usp=sharing) from January 1989 to May 2024 containing home values of single-family residences in 23,917 US neighborhoods across 296 months. Values smoothed, seasonally adjusted, and calculated by taking a trimmed mean of Zillow's own estimates while accounting for [repeat sales index](https://www.investopedia.com/terms/r/repeatsales-method.asp) - [more here](https://www.zillow.com/research/methodology-neural-zhvi-32128/). 

### Data Cleaning
1. Null values
There are 1,356,132 null values in the original dataset; that's **19.5%** (nearly 1/5) of total data. Some neighborhoods only have data for the past few months. For example, Silver Lake neighborhood in Blairstown Nownship, New Jersey only has data from December 2023 to May 2024. Filling them in with adjacent data (**pandas.bfill()**) significantly increased growth rates; doing this method caused some neighborhoods to show inaccurate growth rates like 40,000% in some.
Null values were ultimately dropped. 

2. Dropping columns
Dropped the following columns with unrelated data: "RegionID", "SizeRank", "StateName" (state initials column was kept), "Metro".

### Method
Rate of change formula used:
((Current Value - Previous Value)/Previous Value) * 100

First, we look at the total set of neighborhoods. Then, we take the 50 neighborhoods with the fastest growth and observe their distribution around the median.. Scatterplots are used here to observe the distribution across percentiles.

### Findings

#### All Neighborhoods

<img width="800" src="https://github.com/vitoperez117/Python_US_Home_Values/blob/main/Output%20Plots/All%20Neighborhoods%205%20year%20ROC.png">

*Note: The names of the 23,917 neighborhoods do not fit underneath the x-axis. For viewability, they have been removed.

- The mean growth rate is 52.16%
- The maximum growth rate is 211.88%
- The minimum growth rate is -44.22%

- 75th percentile: 5,482 neighborhoods with growth rates above 64.71%.
- 50th percentile: 10,964 neighborhoods with growth rates between 64.71% and 39.5%.
- 25th percentile: 5,481 neighborhoods with growth rates less than 39.5%
- Red data points: growth rate below 0%.

#### Top 50 Neighborhoods

<img width="500" src="https://github.com/vitoperez117/Python_US_Home_Values/blob/main/Output%20Plots/Top%2050%20Neighborhoods%20scatterplot.png">

- The mean growth rate is 152.27%.
- The top 50 neighborhoods saw home values grow more than double in 5 years.
- Median was used as a guideline to avoid skew from the high-performing outliers.

### Limitations
1. Null values accounted for nearly 1/5 of the data set.
2. Findings rely on Zillow's value estimates.

### Next Steps
1. Identify neighborhoods within each percentile.
2. Find datasets with significantly less null values.
3. Consider different methods of estimating home values from other real estate companies or public agencies.
4. Zoom in on highest performing neighborhoods as well as neighborhoods with a negative growth rate.
5. Add tooltips so that each point shows more information when the cursor is hovering over it.
