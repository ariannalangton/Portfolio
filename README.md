# Arianna Langton - Data Analyst Portfolio
## About
Hello, I'm Arianna! I hold a Bachelor's degree in Physics with a minor in Mathematics, providing me with a strong analytical foundation in both the physical sciences and mathematics. My passion for problem-solving and mathematics has naturally led me toward a career in data analytics. I have earned both the Google Data Analytics and Google Advanced Data Analytics Certificates and am currently working toward completing the Google Business Intelligence Certificate. This will not only build on my data analytics expertise but also deepen my understanding of the business analytics field. 

Throughout my studies, I refined my ability to analyze complex datasets and developed a keen eye for spotting patterns and trends. My experience with data management and statistical analysis has helped me develop a technical mindset that I believe will be a valuable asset in my role as a data specialist. I’m eager to apply my technical and analytical skills to the data science industry as an entry-level data specialist.

In my spare time, I enjoy exploring new data analysis tools and techniques, always seeking opportunities to further expand my knowledge and skillset. Whether collaborating on a team or working independently, I thrive on uncovering insights and solving complex problems through data. My current technical skills include SQL, Tableau, Python, and Excel, alongside deep understanding of mathematics..

This is a repository to showcase skills, share projects and track my progress in Data Analytics.
## Table of Contents
- [About](https://github.com/ariannalangton/Portfolio/blob/main/README.md#about)
- [Portfolio Projects](https://github.com/ariannalangton/Portfolio/blob/main/README.md#portfolio-projects)
  - [Python](https://github.com/ariannalangton/Portfolio/blob/main/README.md#Python)
    - [(Ad Campaign Comparison)](https://github.com/ariannalangton/Portfolio/blob/main/README.md#Analyzing-Ad-Platform-Success)   
    - [(EDA of TikTok Claim Classification)](https://github.com/ariannalangton/Portfolio/blob/main/README.md#analyzing-tiktok-video-statistics)
    - [(Marketing Platform ROI Analysis)](https://github.com/ariannalangton/Portfolio/blob/main/README.md#analyzing-marketing-campaigns-on-different-platforms)
    - [(Investment Analysis)](https://github.com/ariannalangton/Portfolio/blob/main/README.md#Analyzing-Industries-and-Countires-for-Investments)
    - [(Air Quality Analysis )](https://github.com/ariannalangton/Portfolio/blob/main/README.md#Air-Quality-Probability-Density)
    - [(Literacy Data Analysis)](https://github.com/ariannalangton/Portfolio/blob/main/README.md#Literacy-Data-Probability-Density)      
    - [(NASA Meteorite Analysis)](https://github.com/ariannalangton/Portfolio/blob/main/README.md#Analyzing-Meteroite-Landings-Recorded-by-NASA)
    - [(Chaotic Systems of Differential Equations)](https://github.com/ariannalangton/Portfolio/blob/main/README.md#Chaotic-Systems-of-Differenital-Equations)
  - [Tableau](https://github.com/ariannalangton/Portfolio/blob/main/README.md#Tableau)
    - [(My Tableau Public)](https://public.tableau.com/app/profile/arianna.langton5684/vizzes)
      - [(EDA of TikTok Claim Classification)](https://github.com/ariannalangton/Portfolio/blob/main/README.md#EDA-of-TikTok-Claim-Classification)
      - [(League of Legends V13.1 Statistics)](https://github.com/ariannalangton/Portfolio/blob/main/README.md#League-of-Legends-Statistics)
      - [(U.S Women Elected Officals dashboard)](https://github.com/ariannalangton/Portfolio/blob/main/README.md#Women-Elected-Officials)
      - [(Grocery Store KPI Dashboard)](https://github.com/ariannalangton/Portfolio/blob/main/README.md#Grocery-Store-KPI-Dashboard)
      - [(Minnesota Traffic Volume Analysis)](https://github.com/ariannalangton/Portfolio/blob/main/README.md#Minnesota-Traffic-Volume-Analysis)
  - [SQL](https://github.com/ariannalangton/Portfolio/blob/main/README.md#SQL)
  - [Excel and Sheets](https://github.com/ariannalangton/Portfolio/blob/main/README.md#Excel-and-Sheets)
      - [(Clean Data for a Gym Directory)](https://github.com/ariannalangton/Portfolio/blob/main/README.md#Cleaning-Web-Scraped-Data-for-a-Directory)

- [Education](https://github.com/ariannalangton/Portfolio/blob/main/README.md#education)  
- [Certificates](https://github.com/ariannalangton/Portfolio/blob/main/README.md#certificates)
- [Contact](https://github.com/ariannalangton/Portfolio/blob/main/README.md#contacts)
 
## Portfolio Projects
In this section I will list data analytics projects briefly describing the technology stack used to solve cases.

## Python

### Analyzing Ad Platform Success

**Overview:** [(Ad Campaign Comparison)](https://github.com/ariannalangton/Portfolio/tree/main/ad_campaign_comparison)   

**Platform Folders:** [(Facebook Ad Analysis)](https://github.com/ariannalangton/Portfolio/tree/main/ad_campaign_comparison/facebook) 

**Dashboards:** [(Facebook Ad Campaign Dashboard)](https://public.tableau.com/app/profile/arianna.langton5684/viz/FacebookAdCampaignReachAnalysis/Dashboard1#1)

**Goal:** Apply data cleaning and formatting techniques to prepare data for creating dashboards that showcase key metrics, including impressions, conversion rate, click-through rate, and demographic information across Facebook, TikTok, and Google Ads platform. Additionally, conduct statistical analysis to validate that observed trends are statistically significant and reliable for future decision-making. Finally, perform a comprehensive review to determine which platform delivered the best performance.

**Description:** For this project, I analyzed data provided by a digital media specialist who ran ads across Facebook, TikTok, and Google Ads platforms. My analysis focused on the statistical significance of demographic data, specifically age and gender. I also examined the times of day when the ads received the most views. Additionally, I calculated the expected conversion rate, click-through rate, and impressions to conversion rate using a 95% confidence interval, as well as evaluating the cost using either CPM (cost per thousand impressions) or CPC (cost per click) to identify the most effective demographics to target. Finally, I compared the overall success of the campaigns by analyzing metrics such as cost and conversion rate to determine which platform was the most successful.

**Skills:** data cleaning, data analysis, data visualization, statisical analysis, hypothesis testing.

**Technology:** Python, Pandas, Numpy, Matplotlib, scipy, tableau

**Results:**

### Analyzing TikTok Video Statistics

**Code:** 
[(TikTok Claim Analysis)](https://github.com/ariannalangton/Portfolio/blob/main/tiktok_claim_analysis/tiktok_video_stats.ipynb)
[(Claim Hypthosesis Testing)](https://github.com/ariannalangton/Portfolio/blob/main/tiktok_claim_analysis/tiktok_hypothesis_testing.ipynb)

**Dashboard:** [(EDA of TikTok Claim Classification)](https://github.com/ariannalangton/Portfolio/blob/main/tableau_dashboards/EDA_TikTok_Claim_Dashboard.pdf)

**Goal:** Use skills to clean and investigate data following EDA process. Analyze data for TikTok videos and discover trends.

**Description:** For this project I will assist the TikTok analyst team by doing some Exploratory Data Analysis (EDA) and data visualization on a dataset provided by the google data anlytics certificate. The TikTok management team asked to see a Python notebook showing data structuring and cleaning, as well as any matplotlib/seaborn visualizations plotted to help us understand the data. I will analyze claim counts to opinion counts, as well as boxplots of statistics such as “video duration,” “video like count,” “video comment count,” and “video view count” to check for outliers. In addition, I will do a breakdown of “author ban status” counts. I will then perform a hypothesis test to see if the results have any statistical significance.

**Skills:** data cleaning, data analysis, data visualization.

**Technology:** Python, Pandas, Numpy, Seaborn, Matplotlib

**Results:** I observed that TikTok videos flagged as claims receive significantly more views than those flagged as opinions, despite a similar number of videos being posted for both categories. Furthermore, the author status of the user is mainly active across both claim types. However, the proportion of active authors is greater in the opinion category. This suggests that users posting claims are more likely to have their accounts banned or under review. Additionally, all video statistics showed a right-skewed distribution, except for video duration, which exhibited a fairly uniform distribution. Overall, videos that posts claims are likely to get more views and likes than those that are opinions, but the account status is more likely to be banned or under review.

### Analyzing Marketing Campaigns on Different Platforms

**Code:** [(General Analysis)](https://github.com/ariannalangton/Portfolio/blob/main/marketing_budget_analysis/linearRegression_TVbudget_sales.ipynb)
[(Radio vs Sales Analysis)](https://github.com/ariannalangton/Portfolio/blob/main/marketing_budget_analysis/linearRegression_radioBudget_sales.ipynb)

**Goal:** Anlyze data for trends between sales and allocated budget using linear regression. Select the platform with the best relationship between budget and sales generated to recommend for further invesetment.

**Description:** For this activity, I will explore the relationship between marketing promotional budgets and sales using linear regression. The dataset provided includes information about the budget allocated for marketing campaigns across TV, radio, and social media, as well as how much revenue in sales was generated from these campaigns. I will select the platforms that have the most promising relationship between sales and budget and investigate further. After the general analysis, I will also explore the relationship between the radio promotion budget and the sales revenue. Based on this information, decisions about where to focus future marketing efforts will be made, so it is critical to have a clear understanding of the relationship between the different types of marketing and the revenue they generate. 

**Skills:** data cleaning, data analysis, data visualization, regression analysis.

**Technology:** Python, Pandas, Numpy, Seaborn, Matplotlib, statsmodels

**Results:** After analyzing the data  using linear regression and performing hypothesis tests for significance, I was able to reject the null hypothesis and state that there is a relationship between radio promotion budget and sales for companies in this data. However, of the three available promotion types (TV, radio, and social media), TV has the strongest positive linear relationship with sales. According to the model, an increase of one million dollars for the TV promotional budget will result in an estimated 3.5614 million dollars more in sales. Using statistical methods of evaluation I can say this is a very confident estimate, as the p-value for this coefficient estimate is small. Thus, the business should prioritize increasing the TV promotional budget over the radio and social media promotional budgets to increase sales.


### Analyzing Industries and Countires for Investments

**Code:** 
[(Investment Analysis)](https://github.com/ariannalangton/Portfolio/blob/main/unicorn_investment_analysis/inevstor_analysis.ipynb)
[(Unicorn Company Analysis)](https://github.com/ariannalangton/Portfolio/blob/main/unicorn_investment_analysis/unicorn_companies.ipynb)
[(Unicorn Company Trends Analysis)](https://github.com/ariannalangton/Portfolio/blob/main/unicorn_investment_analysis/time_to_unicorn_analysis.ipynb)

**Goal:** Use skills to clean and investigate data following EDA process. Analyze data for companies in different industries and countries as well as data trends, and find 'Unicorn Companies.'

**Description:** I provided insights to an imaginary investing firm. To help them decide which companies to invest in next, the firm wants insights into unicorn companies–companies that are valued at over one billion dollars. The data I used for this task provides information on over 1,000 unicorn companies, including their industry, country, year founded, and select investors. The investor wants companies in the hardware industry based in Beijing, San Francisco, and London. They also want to investigate companies in the artificial intelligence industry based in London. They requested a list of the top 20 countries sorted by company valuations in each country as well as a global valuation map of all countries except United States, China, India, and United Kingdom. In addition, I used this information to gain insights into how and when companies reach this prestigious milestone and to make recommendations for next steps to the investing firm. The investor was particularly interested in understanding the patterns and timing of when companies achieve unicorn status, so I analyzed the data across various timeframes, including years, months, weeks, and quarters.

**Skills:** data cleaning, data analysis, data visualization.

**Technology:** Python, Pandas, Numpy, Seaborn, Matplotlib

**Results:** 
The analysis identified eight companies that meet the criteria for the Hardware and Artificial Intelligence industries. These companies are: Bitmain, Global Switch, Chipone, Density, BenevolentAI, Geek+, TERMINUS Technology, and Tractable. Additionally, the top five countries ranked by valuation are Germany, Sweden, Australia, France, and Canada. A plot of the top twenty companies is available in the notebook. It is also noteworthy that Europe has a high concentration of unicorn companies in a specific region. The second analysis revealed that there are 1074 unicorn companies represented in this dataset. Some companies took longer to reach unicorn status but have accrued high valuation as of March 2022. Companies could take longer to achieve unicorn status for a number of reasons, including requiring more funding or taking longer to develop a business model. The final analsys of the trends showed that 2015 had the highest number of companies founded, indicating that it was the year with the largest concentration of unicorn startups in this dataset. Additionally, a trend emerged where companies founded more recently tended to reach unicorn status more quickly, on average. Focusing on 2021, the most recent year with available data, since trends from 2021 could potentially reflect similar patterns in 2022. The highest number of companies achieving a $1 billion valuation occurred in Week 37 of 2021, which corresponds to the third week of September. After that peak, there was a general decline in the number of companies reaching unicorn status.

### Air Quality Probability Density
**Code:** 
[(Air Quality Inital Sampling)](https://github.com/ariannalangton/Portfolio/blob/main/air_quality_index_analysis/AQI_sampling.ipynb)
[(Air Quality Probability Density)](https://github.com/ariannalangton/Portfolio/blob/main/air_quality_index_analysis/airQuality_probabilityDistrib.ipynb)
[(Air Quality Confidence Intervals)](https://github.com/ariannalangton/Portfolio/blob/main/air_quality_index_analysis/AQI_confidence_intervals.ipynb)
[(Air Quality Hypothesis Testing)](https://github.com/ariannalangton/Portfolio/blob/main/air_quality_index_analysis/hypothesis_testing_practice.ipynb)

**Goal:** Use skills to find what probability distribution fits the data, then use Z-score to find outliers, and finally use hypothesis tests and confidence intervals to check for statistical significane. 

**Description:** I will be using data from the United States Environmental Protection Agency (EPA). The data includes information about more than 200 sites, identified by state, county, city, and local site names. One of the main goals is to determine which regions need support to make air quality improvements. Given that carbon monoxide is a major air pollutant, I will investigate data from the Air Quality Index (AQI) with respect to carbon monoxide. An AQI over 10 would qualify the area for support. I will use the central limit theorem to prove that data can be fit by a normal distribution. I will then perform hypothesis tests and calculate confidence intervals to see if the results of the findings are statistically significant and should be used to decide which states need support.

**Skills:** data cleaning, data analysis, data visualization, probability.

**Technology:** Python, Pandas, Numpy, Seaborn, Matplotlib, SciPy

**Results:** Overall, I discovered that the distribution of the aqi_log data is approximately normal. In addition, using statistical methods such a z-scores, it was determined that the site at West Phoenix has worse air quality than the other sites, and is an outlier who should be considered for support. Upon further analysis, I also identified at the 5% significance level that the Los Angeles mean AQI was statistically different from the rest of California, the confidence interval at the 95% level of confidence from this sample data yielded [10.36 , 13.88], which provides the interpretation "given the observed sample AQI measurements, there is a 95% confidence that the population mean AQI for California was between 10.36 and 13.88.” This range is notably greater than 10, and thus should be considered to receive support. In addition, it was appeared that Michigan had an AQI over 10, but upon further teseting I was unable to conclude at the 5% significance level that Michigan's mean AQI was greater than 10, and am unable to recommend it for support.

### Literacy Data Probability Density
**Code:** [(Literacy Data Probability Density)](https://github.com/ariannalangton/Portfolio/blob/main/normal_distrib_literacyData.ipynb)   

**Goal:** Use skills to find what probability distribution fits the data, and then use Z-score to find outliers. One of the main goals is to determine which district has the lowest literacy scores.

**Description:** I will be using data from different districts in the U.S. The data includes information from multiple states, and inlcudes the districts literacy score, OVERALL_LI. 

**Skills:** data cleaning, data analysis, data visualization, probability.

**Technology:** Python, Pandas, Numpy, Seaborn, Matplotlib, SciPy

**Results:** Overall, I discovered that the distribution of the aqi_log data is approximately normal. In addition, using statistical methods, it was determined that districts 434 and 494 have Z-scores less than -3, and so are outliers. As a result, there should be more focus on those districts to improve the literacy score.

### Analyzing Meteroite Landings Recorded by NASA
**Code:** [(NASA_Meteorite_data_analysis.ipynb)](https://github.com/ariannalangton/Portfolio/blob/main/NASA_Meteorite_data_analysis.ipynb)

**Goal:** Use skills to clean and investigate data following EDA process. Find and analyze most common mass, year, geographical location, name type, and meteorite class.

**Description:** The project focused on analyzing a dataset of meteorite landings from the 1400s to 2014. The dataset included name, id, name type, class, mass, fall type, year, and location. The project involved loading the data, cleaning and preprocessing it, performing exploratory data analysis (EDA), analyzing the most common type, year, and landing location of the meteorites.

**Skills:** data cleaning, data analysis, data visualization.

**Technology:** Python, Pandas, Numpy, Seaborn, Matplotlib, SciPy, Plotly Express

**Results:** Using Python functions the analysis revealed that the year with the most meteorites was 1998. However, the year with the most missing data was 2004 and was followed closely by 2003, which could have skewed the data. For location, the most common spot was (0,0), which is most likely an error. The second most common was in Antarctica. The average mass of all the meteorites was 14020 grams. The average mass was also calcualted for year as well as meteroite class. Ofcourse there are many other characteristics that could have been investigated, but this was enough for my goal.

### Chaotic Systems of Differenital Equations
**Code:** [(Chaotic differential Systems of Equations)](https://github.com/ariannalangton/Portfolio/blob/main/chaotic_systems/Chaotic_Systems.ipynb)

**Goal:** Simulate and solve three different chaotic systems of ordinary differential equations; Lorenz, Chua, Rössler. Discover what inital conditions, or coefficients, cause the system to become chaotic attractors. An attractor describes a state to which a dynamical system evolves after a long enough time.

**Description:** Utilized Python to simulate and solve three different chaotic systems of ordinary differential equations; Lorenz, Chua, Rössler. Each system is comprised of their own unique equations and coefficents.
**Skills:** data analysis, data visualization, mathematics.

**Technology:** Python, Pandas, Numpy, Matplotlib, SciPy, mpl_toolkits.mplot3d

**Results:** [(Results Report)](https://github.com/ariannalangton/Portfolio/blob/main/chaotic_systems/chaotic%20attractors%20results.pdf)

## Tableau

### EDA of TikTok Claim Classification
**Dashboard:** [(EDA of TikTok Claim Classification)](https://github.com/ariannalangton/Portfolio/blob/main/tiktok_claim_analysis/tiktok_claim_analysis/EDA_TikTok_Claim_Dashboard.pdf)

**Tableau:** [(TikTok Claim Dashboard on Tableau)](https://public.tableau.com/views/EDAofTiktokClaimClassification/Story1?:language=en-US&:sid=&:redirect=auth&:display_count=n&:origin=viz_share_link)

**Goal:** Use TIkTok claim statistics to build easy to understand visualizations.

**Description:** The project aimed to analyze TikTok video user status, claim status, and video statistics such as like count, view count, video duration, and like count.

**Skills:** Tableau, data visualization, box plots, scatter plot

**Results:** By utilizing Tableau's plots and aggregation functions, I created a scatter plot to show the relationship between a videos like count and view count for claims and opinions. In addition, I visualized the total amount of claims v.s opinions, as well as an author status (active, banned, or under review) and the type of video posted by each status.

### League of Legends Statistics
**Dashboard:** [(League of Legends V13 Statistics Dashboard IMG)](https://github.com/ariannalangton/Portfolio/blob/main/tableau_dashboards/league_of__ledgends_dashboard.png)

**Tableau:** [(League of Legends Tableau Dashboard)](https://public.tableau.com/app/profile/arianna.langton5684/viz/leagueoflegendsstats/Dashboard2)

**Goal:** Use League of Legends Champion statistics v13.1 from Kaggle to create a dashboard on Tableau. Analyzed champions and roles by most played, ban rate, and win rate.

**Description:** The project aimed to analyze more than a hundred champions by examining their win, loss, ban, and pick rates. Additionally, I explored the same characteristics for each of the five possible roles.

**Skills:** data cleaning, data analysis, data visualization.

**Results:** By utilizing Tableau's built-in aggregation functions, I determined that Caitlyn was the most played champion, while Zed was the most banned. Furthermore, Singed had the highest win rate among all champions when played in the Mid role, and Mid being the role with the highest overall win rate. Additionally, I visualized the top 8 most played champions and the roles in which they are most frequently selected.

### Women Elected Officials
**Dashboard:** [(U.S Women Elected Officals Dashboard IMG)](https://github.com/ariannalangton/Portfolio/blob/main/tableau_dashboards/us_women_officials.png)

**Tableau:** [(U.S Women Elected Officials Tableau Dashboard)](https://public.tableau.com/app/profile/arianna.langton5684/viz/U_SWomenElectedOfficialsDemographics/Dashboard2)

**Goal:** Create a Tableau dashboard on the demographics of U.S. women elected officials using data from cawp.rutgers.edu. Analyze race, political party, and state.

**Description:** The project aimed to analyze the demographics of more than a thousand different women elected officials and find trends.

**Skills:** data cleaning, data analysis, data visualization.

**Results:** Using Tableau, I found that 68% of women elected officials are White. The Democratic Party has the highest representation of women, accounting for 64% of all elected women. New Hampshire leads the states with the most elected women, comprising 5.9% of all women in office.

### Grocery Store KPI Dashboard
**Dashboard:** [(Grocery Store KPI Dashboard IMG)](https://github.com/ariannalangton/Portfolio/blob/main/tableau_dashboards/super_market_KPI_dash.png)

**Tableau:** [(Grocery Store KPI Tableau Dashboard)](https://public.tableau.com/app/profile/arianna.langton5684/viz/2015SalesDashboard_17313755663760/profitdashboard)

**Goal:** Create a Tableau dashboard to easily present KPIs such as sales, profits, quantity sold, sales by region, and category wise sales.

**Description:** Analyzed sales data from Kaggle for an anonymous supermarket. Created Tableau dashboards by analyzing sales KPIs for 2015 as well as geographical sales from 2012-2015.

**Skills:** data cleaning, data analysis, data visualization, KPIs, Sales Metrics.

**Results:** Using Tableau, I discovered that sales for 2015 totaled 4.29M, reflecting a 26.2% increase compared to 2014. Additionally, profit saw a 23.8% year-to-date increase, while the quantity sold rose by 25.9%. The highest sales came from the Technology category, with Phones being the top sub-category. The region generating the most profit for the store was Asia, closely followed by Europe.

### Minnesota Traffic Volume Analysis
**Dashboard:** [(Traffic Voulme Dashboard PDF)](https://github.com/ariannalangton/Portfolio/blob/main/traffic_volume_analysis/minnesota_traffic_volume_dash.png)

**Tableau:** [(Traffic Volume Dashboard on Tableau)](https://public.tableau.com/app/profile/arianna.langton5684/viz/MinnesotaTrafficVolumeDashboard_17376035629680/Dashboard1)

**Report:** [(Traffic Volume Analysis)](https://github.com/ariannalangton/Portfolio/blob/main/traffic_volume_analysis/Consulting%20Traffic%20Volume%20proposal.pdf)

**Goal:** Create a Tableau dashboard to easily present patterns in traffic such as holidays, weather, time of day, and by year.

**Description:** Analyzed sales data from Minnesota for any traffic patterns that could reveal a cause for high traffic volume.

**Skills:** data analysis, dashboard visualization, tableau.

**Results:** Using Tableau, I found that August had the highest traffic volume, likely due to end-of-summer activities, while February had the lowest traffic. I also discovered that clear or cloudy days generally see the most traffic, with a decrease during rainy conditions, and the least traffic occurs when it’s foggy or visibility is impaired. Additionally, holidays like New Year’s Day and MLK Jr. Day in January, as well as Labor Day in September, contribute to traffic spikes. Analyzing traffic by hour and day reveals that it peaks during rush hours, as people commute to and from work, and also shows that holidays have minimal overall effect on traffic.

## SQL

## Excel and Sheets

### Cleaning Web Scraped Data for a Directory

**Files:** [(Cleaning Alabama Data)](https://github.com/ariannalangton/Portfolio/tree/main/cleaning_webscraped_data)

**Goal:** The data will be used to create a directory of Jiu-Jutsu gyms for each state, organized by city. The information is gathered through a web-scraping tool that will be used to search for jiu-jutsu gyms in certain cities for each state. My task was to select the appropriate cities and clean and filter the query data using specific criteria to ensure that only relevant gyms are included for each state.

**Description:** The data collection process took place in two stages. First, I compiled a comprehensive list of cities for each state, removing those unlikely to serve marketing purposes, such as cities with small populations, to optimize the search query. Once the relevant cities were identified, I organized the list in Excel, ensuring it was formatted to work with the web scraping tool, which required the format “jiu-jutsu gym in [city] [state].” After proper formatting, the query was executed, and the data was gathered. 

Once the data was received, I began cleaning it in Google Sheets, following specific guidelines. This initial cleanup involved removing gyms that were either located in the wrong state or lacked crucial details like names or addresses. Collaborating with the digital marketer, we established criteria to filter for promising gyms: we focused on those with over 10 reviews and filtered by categories and names containing terms such as BJJ, jiu, jutsu, MMA, martial, Gracie, and ground. We also conducted a final review to eliminate gyms that included terms like TKD, kung fu, or taekwondo, which might have slipped through the initial filters. 

Next, I ensured that the city and address were placed in separate columns, as required by the marketer to import the gyms into the directory. This was done using the "text to columns" function in Excel. I also made any final formatting adjustments, such as removing blank rows, highlighting, or resizing rows as needed. 

As a result, the total number of gyms in the list was significantly reduced. For Alabama, the count dropped from 429 to 73 key Jiu-jutsu gyms that were prioritized for inclusion in the directory.

**Skills:** data cleaning, data analysis, metrics, google sheets, power query/ power tools

**Technology:** google sheets, power tools, web scraping

## Education

Illinois State University |
Bachelor of Science, Physics |
2019 - 2023

## Certificates

Google Data Analytics Professional Certificate (Aug 2024) (Coursera - Google) <br>
Google Advanced Data Analytics Professional Certificate (Jan 2025) (Coursera - Google)

## Contacts
- LinkedIn: [@ariannalangton](https://www.linkedin.com/in/arianna-langton-844b03252)
- Email: anlangton00@gmail.com
