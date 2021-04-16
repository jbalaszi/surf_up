# surfs_up
Perform weather analysis to gain a potential investor in new Surf Shop business.

## Overview of Statistical Analysis
The purpose of our analysis is to gather temperature statistics for June and December to gain a potential investor for a surf and ice cream venture in Hawaii. Our potential investor requested this analysis to see if our potential venture will be sustainable year round. 

To perform this analysis, the following steps were executed:
- Run two separate queries to gather temperature data
  - One query for June dates
  - One query for December dates
- Store the temperatures in a list
- Convert into a dataframe
- Summary statistics for June and December temperatures

## Results
Our analysis provided three key differences in weather between June and December

| | June Temps |
| ---- | ---- |
| Count | 1700.0000 |
| Mean | 74.9441 |
| Std. | 3.2574 |
| Min | 64.0000 |
| 25% | 73.0000 |
| 50% | 75.0000 |
| 75% | 77.0000 |
| Max | 85.0000 |

| | December Temps |
| ---- | ---- |
| Count | 1517.0000 |
| Mean | 71.0415 |
| Std. | 3.7459 |
| Min | 56.0000 |
| 25% | 69.0000 |
| 50% | 71.0000 |
| 75% | 74.0000 |
| Max | 83.0000 |

1. Overall, June has higher variables than December. June has a count of 1700 and mean of 74.94. December's count is a 183 less than June and a lower mean, 71.04.
2. December had a lower max and min compared to June. December's max (83.00) was 2 less than June's max of 85.00. December's minimum totaled to 56.00, while June had a minimum of 64.00 - an eight count difference.
3. When comparing standard deviations, there is a 0.5 difference between the two seasons. June resulted in a standard deviation (std.) of 3.257 while December possed a std. of 3.746.

## Summary 
