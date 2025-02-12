# Facebook, Google, and TikTok Ads Statistical Analysis
# Arianna Langton
##  About

For this project, I received data from a paid digital media specialist who ran ads across Facebook, Google, and TikTok. I will conduct separate analyses for each 
platform, as well as an overall comparison to determine which platform was the most successful based on several key metrics. For each individual analysis, I will 
create Tableau dashboards to visualize the data and utilize Python for detailed analysis, including statistical methods like confidence intervals, 
hypothesis tests, and regression analysis. This folder all dashboards and code created for the project, as well as any executive summaries created. Each platform is orgnaized into its own folder.
## Table of Contents    
- [TikTok Statisical Analysis](https://github.com/ariannalangton/Portfolio/blob/main/ad_campaign_comparison/tiktok/README.md)
  - [Jupyter Notebook](https://github.com/ariannalangton/Portfolio/blob/main/ad_campaign_comparison/tiktok/tiktok_analysis.ipynb)
  - Tableau Dashboards
    - [Demographic Dashboard](https://public.tableau.com/app/profile/arianna.langton5684/viz/TikTokDemographicDataDashboards/Metrics)
    - [Metrics Dashboard](https://public.tableau.com/app/profile/arianna.langton5684/viz/TiktokAdMetricsDashboards/Story1)   
- [Facebook Statistical Analysis](https://github.com/ariannalangton/Portfolio/blob/main/ad_campaign_comparison/facebook/README.md)
  - [Jupyter Notebook](https://github.com/ariannalangton/Portfolio/blob/main/ad_campaign_comparison/facebook/Facebook_Ad_Statistical_Analysis.ipynb)
  - [Tableau Dashboards](https://public.tableau.com/app/profile/arianna.langton5684/viz/FacebookAdCampaignReachAnalysis/Story1)
  - [Executive Summary](https://github.com/ariannalangton/Portfolio/blob/main/ad_campaign_comparison/facebook/Facebook%20Ads%20Executive%20Summary.pdf)
- [Google Statistical Analysis](https://github.com/ariannalangton/Portfolio/tree/main/ad_campaign_comparison/google)
  - [Jupyter Notebook](https://github.com/ariannalangton/Portfolio/blob/main/ad_campaign_comparison/google/google_analysis.ipynb)
  - [Tableau Dashboards](https://public.tableau.com/app/profile/arianna.langton5684/viz/GoogleAdCampaignAnalysis/Story1)
- [Overall Platform Comparison](https://github.com/ariannalangton/Portfolio/blob/main/ad_campgaign_comparison/README.md#Overall)
  - [Tableau Dashboards](https://public.tableau.com/app/profile/arianna.langton5684/viz/AdPlatformComparison/Dashboard1#1)

**Results:** An overview of the results for each platform is below.
- Facebook
  - Males viewed the ad significantly more than females, in terms of reach and impressions, which was confirmed through statistical testing. There was some indication that the reach-to-impression ratio between genders may differ, the p-value of 0.08 suggests that further investigation is needed to draw firm conclusions.
  - The age group 55-64 stood out as the most frequent viewers, with a significant 99% difference from the lowest group, indicating a strong preference for this demographic.
  - The ad was most frequently seen during early morning hours, lunch breaks, and late afternoon, aligning with typical routines of the older demographic. However, due to the minor differences in impressions during the top viewing hours, more data is required to determine the most effective time for ad placements.
  - It performed well in terms of conversion and click-through rates, surpassing industry averages. The 30% conversion rate is particularly notable, but the relatively low impression-to-conversion rate (1.4%).
- Tiktok
  -  Using a two-sample z-test it was found women had significantly more impressions than men, however there was no significant difference in conversion rate (CVR) or click rate (CTR) by gender.
  -  Using a one way ANOVA test it was revealed that age had no effect on CVR or CTR. Using a post-hoc tukey test it was revealed that the age group with the most conversions was the 55+ group, with 18-25 having the least. .
  -  Two-way ANOVA test for age and gender revealed the females in the 18-25 group had the lowest conversions and men in the 55+ age group had the most. This indicates older people, men specifically, are more likely to convert, and younger people, women specifically, are less likely to convert.
  -  An ANOVA test was used to analyze what days of the week recieved the most impressions, showing that Sunday had the most, follwoed by Saturday, and that this is signigicantly different than the rest.
  -  A one way ANOVA test revealed that the times that recieved the most views were 8PM, 10PM, 9PM, 7PM, 6PM, all occurring during the evening when people are generally more available after work and school.
- Google
  - Women viewed the ad significantly more than males in terms of impressions, confirmed through a two-sample z-test
  - There is a moderate difference in the amount of impressions by age, with the age group recieiving the most being 25-35 and the least being 65+. Found using ANOVA test with a p-value < 0.05 for significance and < 0.1 for moderate significance.
  - There is no difference in amount of impressions by hour or by weekday, found using an ANOVA test. However, the day with the most impressions was Tuesday and Friday. The times with the most were in the evening or during lunch (7PM, 8PM, 1PM, 2PM, 11AM), both times when people tend to have free time in their day.
  - There is no difference in the amount of clicks recieved by keyword search, however the ones that did recieve clicks suggests the target demographic should be families / those with kids or couples / those with a partner, as top keywords contained words like 'kids' or 'couples'.

**Overall** 
  - TikTok had the largest reach as well as clicks, but the lowest conversion rate (1.13%) and second lowest click through rate (3.45%). Facebook had the seconed highest reach and clicks, with the best conversion rate by a land slide (30.96%), and the best click through rate (4.6%). Google performed the worst, with the lowest amount of impressions and clicks, as well as lowest click through rate (1.14%) and second lowest conversion rate (3.1%).
  - TikTok had the lowest cost per click (0.22$) with the highest total cost (120$), facebook had the second highest cost per click (0.42$) and the second highest total cost (100.4$), lastly Google having the highest CPC (0.53$) but lowest total cost (56.19$). 
  - TikTok recieved the most views, but it had the lowest conversion rate and second lowest click through rate. Therefore, Facebook out performned TikTok and can be selected as the best performing platform for these metrics.
  - While google had the lowest total cost, it had the lowest amount of clicks, which resulted in the low cost irregardless of it having the highest cost per click. Additionally, it had the worst click through and second lowest conversion rate. TikTok had the highest total cost, but it also had the most views resutling in the high cost despite it having the lowest cost per click. Facebook had the second lowest total cost and cost per click, as well as the second highest reach. Taking only cost and reach into account, TikTok would be the superior choice. However, taking all metrics into account, Facebook is the best choice.
  - Using facebook, the target demographic should be men and older age groups, as they were most likely to convert. If the time of day is going to be manually selected, the times should be either early mornings or lunch hours as that is when people in older age groups are more likely to be on social media and view the ad. Additionally, the ad should be catered to target families or couples, as revealed in the Google keyword search results.
