## TikTok Ad Campaign Analysis

To get an overview of the entire project, please go to the [README](https://github.com/ariannalangton/Portfolio/blob/main/ad_campaign_comparison/README.md) file in the ad campaign comparison folder. In this folder there are three files; an [executive summary] of the project,  screenshots of the two dashboards I created on Tableau ([Demographics Dashbaord](https://public.tableau.com/app/profile/arianna.langton5684/viz/TikTokDemographicDataDashboards/Metrics) | [Metrics Dashboard](https://public.tableau.com/app/profile/arianna.langton5684/viz/TiktokAdMetricsDashboards/Story1)) and the [python notebook]() I created using google colab to analyze the data. For this part of the project, I analyzed the data provided by a digital media specialist who ran an ad through TikTok's ad platform. I analyzed the statistical significance of the demographic data, focusing on age and gender. Additionally, I examined the times of day when the ads receive the most views. I also calculated the expected conversion rate and click through rate.

The following is a summary of the methods used and results

## Demographics

In this analysis, I explored the relationship between user demographics (gender and age) and key performance indicators (KPIs) such as impressions, clicks, and conversions. The goal was to understand if there were statistically significant differences between men and women in terms of these metrics and if age had any impact on conversion and click-through rates (CTR).

To achieve this, I applied a series of hypothesis tests and analysis of variance (ANOVA) techniques, including:

1. **Hypothesis Test for Gender Differences**: I performed a hypothesis test to determine whether women had more impressions, clicks, and conversions than men. Using the resultant p-value and an alpha of 0.05, women have a statisitically different amount of impressions and clicks. However, there is no difference in conversions between men and women.
  
2. **2-Way Z-Test for Conversion (CVR) and Click Rates (CTR)**: A two-way z-test was used to investigate conversion and click rates by gender. Using an alpha of 0.05 again, it was found that there is no significant difference between CVR or CTR for men and women. Even though women were the majority of impressions and clicks, they both had the same overall CVR and CTR.
  
3. **One-Way ANOVA for Age Effect**: I conducted a one-way ANOVA to assess whether age influenced conversion rates, as it was revealed gender does not. The test revealed that age had no significant effect on CVR.

4. **One-Way ANOVA for Gender and KPIs**: A one-way ANOVA was also performed to see if gender had an effect on conversion rates. The test revealed that gender had no significant effect on CVR, which can be seen in the z-test as well.

5. **Two-Way ANOVA with Post-Hoc Tukey Test**: To refine the analysis, a two-way ANOVA with a post-hoc Tukey test was applied to assess the effect of both age and gender on conversion rates. Using a 0.05 value for alpha, there was no significant difference between any of the categories. However, upon further analysis in the post-hoc tukey test, it was found that the following pairs had a p value of less than 0.1, which is also a valid alpha choice.
  - Age groups 18-25 and 55+
  - Women in the age group 18-25 and men in the age group 55+

 This suggests that older age groups, and older men specifically, are more likely to convert than the younger age groups, young women specifically. This makes sense, as older age groups are more likely to have money to spend on entertainment than the younger age groups.

This series of analyses provides valuable insights into how user demographics may affect conversion behaviors and helps identify actionable trends for improving performance across different user groups.

## Time Analysis

 For this analysis, I examined data from an advertising campaign that was run over the course of two different weeks.

 **Week 1**, I performed a one-way ANOVA test to determine if there were significant differences in impressions, clicks, and conversions across different days of the week. The results revealed a significant difference, with Sunday leading in all three metrics, followed by Saturday. To further explore the differences between the days, I used a post-hoc Tukey test, which compared all the days in pairs.

**Week 2**, I found that the data was insufficient to run an ANOVA test, so I evaluated the trends manually. I observed that Wednesday and Tuesday outperformed the other days in impressions, clicks, and conversions. Monday lagged behind in impressions and clicks but was relatively consistent with other days in terms of conversions. Thursday and Friday consistently had low performance across all metrics.

Lastly, I conducted an ANOVA test for impressions by hour of the day for week 1. The results showed no significant variance between hours, even with a p-value < 0.1. However, I did identify that the top 5 times for impressions were consistently around 300 impressions, with the peak time being over 500 impressions. The top 5 times, in order, were: 8 PM, 10 PM, 9 PM, 7 PM, and 6 PM—all occurring during the evening when people are generally more available after work and school.
