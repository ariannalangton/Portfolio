## Google Ad Campaign Analysis

To get an overview of the entire project, please go to the [README](https://github.com/ariannalangton/Portfolio/blob/main/ad_campaign_comparison/README.md) file in the ad campaign comparison folder. In this folder there are multiple files; screenshots of the dashboard I created on Tableau [(Google Dashbaord)](https://public.tableau.com/app/profile/arianna.langton5684/viz/GoogleAdCampaignAnalysis/Story1#1) and the [python notebook](https://github.com/ariannalangton/Portfolio/blob/main/ad_campaign_comparison/google/google_analysis.ipynb) I created using google colab to analyze the data. For this part of the project, I analyzed the data provided by a digital media specialist who ran an ad through Google's ad platform. I analyzed the statistical significance of the demographic data, focusing on age and gender. Additionally, I examined the times of day when the ads receive the most views and analyzed the keyword search data, finding the CPC and most clicked keyword.

The following is a summary of the methods used and results

## **Introduction: Analyzing User Metrics and Keyword Performance**

## Demographics

In this analysis, I explored the relationship between user demographics (gender and age) and impressions. The goal was to understand if there were statistically significant differences between men and women impression amounts and if age had any impact on impressions.

To achieve this, I applied a series of hypothesis tests and analysis of variance (ANOVA) techniques, including:

1. **Hypothesis Test for Gender Differences**: I performed a hypothesis test using a two-way z-test to determine whether women had more impressions men. Using the resultant p-value and an alpha of 0.05, it was proven women have a statisitically different amount of impressions.

2. **One-Way ANOVA for Age Effect with Post-Hoc Tukey Test**: I conducted a one-way ANOVA to assess whether age influenced impressions, as it was revealed gender does. The test revealed that age has a moderate effect on the amount of impressions, with a p-value less thabn 0.1 but bigger than 0.05. This suggests further investigation should be done for age and its effect on impressions, but it could still be considered as relevant.
  - The post-hoc test found age groups 18-25 and 65+ to be the most different, with 25-25 having the most impressions and 65+ having the least.

3. **Two-Way ANOVA**: To refine the analysis, a two-way ANOVA with a post-hoc Tukey test was applied to assess the effect of both age and gender on conversion rates. Using a 0.05 value for alpha, there was no significant difference between any of the categories as the p-value for all categories was NAN. This does not actually mean there is no difference, but that there needs to be more data gathered to get a meaningful result. 
  - Since this did not turn out any results, it is hard to tell what gender and age group will get the most amount of impressions. However, it was proven that women got significantly more impressions than men, and that age group 25-35 got the most impressions, so it isn't far-fetched to say that women in the 25-35 age group will have the most impressions.

## Time Analysis

1. **Start Hour ANOVA with Post-Hoc Tukey Test** I conducted an ANOVA test for impressions by hour of the day. The results showed no significant variance between hours, even with a p-value < 0.1. However, I did identify that the top 5 times impressions were during lunch and dinner hours, with the peak time being over 100 impressions. The top 5 times, in order, were: 7 PM, 8 PM, 1 PM, 2 PM, 11 AM. These all occurr either during the evening when people are generally more available after work and school, or during a lunch break period.

2. **Weekday ANOVA Test with Post-Hoc Tukey Test** I performed a one-way ANOVA test to determine if there was a significant difference in impressions for different days of the week. The results revealed there is no significant difference when using an alpha of 0.05. Overall, Tuesday had the most impressions followed by Friday, with Thursday having the least amount of impressions. To further explore the differences between the days, I used a post-hoc Tukey test, which compared all the days in pairs. This again revealed no signifcant difference between days as none had a p-value less than 0.1.

## Keyword Analysis

**Keyword Search ANOVA Test with Post-Hoc Tukey Test** To evaulte if there was any significant differenfe between the use of keywords, I conducted an ANOVA test using the keywords and the clicks recieved. This revealed that there is no significant difference between keywords, even with a p-value < 0.1. The leading three keywords were as follows: 'things to do', 'Things to do with family', and 'Things to do with kids'. They had 54, 19, and 14 clicks in that order. The 4th keyword was 'things to do near me' but it had a steep fall off of clicks, recieving only 6, and the rest recieving under 5. From this, I gather the folliwng
 - Two of the top keywords contain family-oriented words, such as family or kids. This suggests that the link was clicked by those looking to do something fun with their children and should be considered for future target demographics.
 - Two other top keywords contained relationship-oriented words, such as date idea or couples idea. While these keywords recieved less clicks than the above, this still sugggests the link was clicked by those with a partner looking to do something fun, and should be considered for future demopgrahics as well.



