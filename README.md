# Climate Analysis for Business Profitability

## Overview and purpose
The purpose of this analysis was to find weather data for the city of Oahu to see if starting a surf board & ice cream business would be profitable. I conducted an analysis of the temperature and the precipitation from a set of weather data.

## Results
Here are some of the findings:
- **June**
  - June had 1,700 temperature observations across the entire dataset
  - the average temperature was 74.94F
  - the max was 85F

![June Summary Stats](/Resources/jun_desc.png)

- **December**
  - December only had 1,517 days worth of temperature observations across the entire dataset
  - the average temperature was 71.04F
  - the min was 56F

![Decemebr Summary Stats](/Resources/dec_desc.png)
  
## Summary
The results of this analysis are mixed. While at first glance there is not much discrepancy between the temperature observations for the two months, there is a discrepancy between the counts of observations. There are 1,517 counts of observations for December vs 1,700 for June. While this is as accurate as the data can get, it may have been beneficial for there to have been data where there is not for the days in December.

The average temperatures are very similar, showing that the weather is going to be nearly the same all year round. It may occasionally get too cold for ice cream in December, as the lowest recorded temperature from the summary is 56F. June will be a popular month for both ice cream and surfing as it can get hot, up to 85F.

I ran two additional queries on the dataset, also grabbing the precipitation data for the months of June and December. 

![June Extra Query](/Resources/jun_extra.png)![December Extra Query](/Resources/dec_extra.png)

Here is what I found:
- **June**
  - 1,574 precipitation observations across the entire dataset
  - the average precipitation was 0.14 in
  - the min was 0 in

![June Extra Summary Stats](/Resources/jun_extra_desc.png)


- **December**
  - 1,405 precipitation observations across the entire dataset
  - the average precipitation was 0.22 in
  - the max was 6.42 in

![December Extra Summary Stats](/Resources/dec_extra_desc.png)
  
This info tells me that while the temperature remains nearly the same all year round, on average, there tends to be more precipitation in December than in June. Couple that with the minimum temperature for June also being relatively low, then business may not be as profitable at that time compared to in June.
