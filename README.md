# Arianna Langton - Data Analyst Portfolio
## About
Hi, I'm Arianna! I have an analytical background in Physics and currently, I am on track to complete the Advanced Google Data Analytics Professional Certificate. I have developed a strong foundation in the physical sciences and mathematics. My passion for mathematics and problem-solving has naturally led me to pursue a career in data analytics. I am excited to bring my technical and analytical skills to the field of data science as an entry-level data specialist. 

During my studies, I honed my ability to work with complex data and developed a keen eye for identifying patterns and trends. I also gained experience in laboratory techniques, data management, and statistical analysis, which I believe will be valuable assets in my role as a data specialist.

In my free time, I enjoy exploring new data analysis tools and techniques, and I am always looking for opportunities to expand my knowledge and skills. Whether working on a team or independently, I am driven by the thrill of discovering new insights and the satisfaction of using data to solve complex problems.

This is a repository to showcase skills, share projects and track my progress in Data Analytics.
## Table of Contents
- [About](https://github.com/ariannalangton/Portfolio/blob/main/README.md#about)
- [Portfolio Projects](https://github.com/ariannalangton/Portfolio/blob/main/README.md#portfolio-projects)
  - Python
    - [(EDA of TikTok Claim Classification)](https://github.com/ariannalangton/Portfolio/blob/c94ec4fcd1acb20a80d4908f507b00f14b955fd5/tiktok_claim_analysis/tiktok_video_stats.ipynb)
    - [(Investment Analysis)](https://github.com/ariannalangton/Portfolio/blob/38d1a4317bf731a6ed63411959ac17e9273022d3/inevstor_analysis.ipynb)
    - [(Air Quality Probability Density)](https://github.com/ariannalangton/Portfolio/blob/bc2899d2ba3eac19c2004f078ec27446a7830c78/airQuality_probabilityDistrib.ipynb)
    - [(Unicorn Companies)](https://github.com/ariannalangton/Portfolio/blob/23547f2771f055c2d4e124c110c900657fcff94c/unicorn_companies.ipynb)
    - [(Literacy Data Probability Density)](https://github.com/ariannalangton/Portfolio/blob/bc2899d2ba3eac19c2004f078ec27446a7830c78/normal_distrib_literacyData.ipynb)      
    - [(NASA Meteorite Analysis)](https://github.com/ariannalangton/Portfolio/blob/ef320e76983f81345d6d69b4d4bc14628d79b3f7/NASA_Meteorite_data_analysis.ipynb)
    - [(Time to Become a Unicorn Company)](https://github.com/ariannalangton/Portfolio/blob/03b054d573a757fa627a0645e8603680212eb1c0/time_to_unicorn_analysis.ipynb)
    - [(Chaotic Systems of Differential Equations)](https://github.com/ariannalangton/Portfolio/blob/504d9f5afff2dddbe197ccc0b9234bba5ea340b6/Chaotic_Systems.ipynb)
  - Tableau
    - [(My Tableau Public)](https://public.tableau.com/app/profile/arianna.langton5684/vizzes)
      - [(EDA of TikTok Claim Classification)](https://github.com/ariannalangton/Portfolio/blob/c5d8aef94117dba2fb00d0b446391a9867ff0ddc/EDA_TikTok_Claim_Dashboard.pdf)
      - [(League of Legends V13.1 Statistics)](https://github.com/ariannalangton/Portfolio/blob/5b5126c4eb52a489c2b5a16a198298328f6093d6/league_of__ledgends_dashboard.png)
      - [(U.S Women Elected Officals dashboard)](https://github.com/ariannalangton/Portfolio/blob/a3e2b93bd28c35742cffb0a9d3f3b0ee5d6185c5/us_women_officials.png)
      - [(Grocery Store KPI Dashboard)](https://github.com/ariannalangton/Portfolio/blob/9e84e895d87f93f932188b19805f45b936bea026/profit%20dashboard.png)

- [Education](https://github.com/ariannalangton/Portfolio/blob/main/README.md#education)  
- [Certificates](https://github.com/ariannalangton/Portfolio/blob/main/README.md#certificates)
- [Contact](https://github.com/ariannalangton/Portfolio/blob/main/README.md#contacts)
 
## Portfolio Projects
In this section I will list data analytics projects briefly describing the technology stack used to solve cases.

### Analyzing TikTok Video Statistics

**Code:** [(TikTok Claim Analysis)](https://github.com/ariannalangton/Portfolio/blob/main/tiktok_claim_analysis/tiktok_video_stats.ipynb)
[(Claim Hypthosesis Testing)](https://github.com/ariannalangton/Portfolio/blob/main/tiktok_claim_analysis/tiktok_hypothesis_testing.ipynb)

**Goal:** Use skills to clean and investigate data following EDA process. Analyze data for TikTok videos and discover trends.

**Description:** For this project I will assist the TikTok analyst team by doing some Exploratory Data Analysis (EDA) and data visualization on a dataset provided by the google data anlytics certificate. The TikTok management team asked to see a Python notebook showing data structuring and cleaning, as well as any matplotlib/seaborn visualizations plotted to help us understand the data. I will analyze claim counts to opinion counts, as well as boxplots of statistics such as “video duration,” “video like count,” “video comment count,” and “video view count” to check for outliers. In addition, I will do a breakdown of “author ban status” counts.

**Skills:** data cleaning, data analysis, data visualization.

**Technology:** Python, Pandas, Numpy, Seaborn, Matplotlib

**Results:** I observed that TikTok videos flagged as claims receive significantly more views than those flagged as opinions, despite a similar number of videos being posted for both categories. Furthermore, the author status of the user is mainly active across both claim types. However, the proportion of active authors is greater in the opinion category. This suggests that users posting claims are more likely to have their accounts banned or under review. Additionally, all video statistics showed a right-skewed distribution, except for video duration, which exhibited a fairly uniform distribution. Overall, videos that posts claims are likely to get more views and likes than those that are opinions, but the account status is more likely to be banned or under review.

### Analyzing Industries and Countires for Investments

**Code:** [(Investment Analysis)](https://github.com/ariannalangton/Portfolio/blob/main/inevstor_analysis.ipynb)

**Goal:** Use skills to clean and investigate data following EDA process. Analyze data for companies in different industries and countries.

**Description:** I provided insights to an imaginary investing firm. To help them decide which companies to invest in next, the firm wants insights into unicorn companies–companies that are valued at over one billion dollars. The data I used for this task provides information on over 1,000 unicorn companies, including their industry, country, year founded, and select investors. The investor wants companies in the hardware industry based in Beijing, San Francisco, and London. They also want to investigate companies in the artificial intelligence industry based in London. They requested a list of the top 20 countries sorted by company valuations in each country as well as a global valuation map of all countries except United States, China, India, and United Kingdom

**Skills:** data cleaning, data analysis, data visualization.

**Technology:** Python, Pandas, Numpy, Seaborn, Matplotlib

**Results:** 
The analysis identified eight companies that meet the criteria for the Hardware and Artificial Intelligence industries. These companies are: Bitmain, Global Switch, Chipone, Density, BenevolentAI, Geek+, TERMINUS Technology, and Tractable. Additionally, the top five countries ranked by valuation are Germany, Sweden, Australia, France, and Canada. A plot of the top twenty companies is available in the notebook. It is also noteworthy that Europe has a high concentration of unicorn companies in a specific region.

### Air Quality Probability Density
**Code:** [(Air Quality Probability Density)](https://github.com/ariannalangton/Portfolio/blob/bc2899d2ba3eac19c2004f078ec27446a7830c78/airQuality_probabilityDistrib.ipynb)

**Goal:** Use skills to find what probability distribution fits the data, and then use Z-score to find outliers. 

**Description:** I will be using data from United States Environmental Protection Agency (EPA). The data includes information about more than 200 sites, identified by state, county, city, and local site names. One of the main goals is to determine which regions need support to make air quality improvements. Given that carbon monoxide is a major air pollutant, I will investigate data from the Air Quality Index (AQI) with respect to carbon monoxide.

**Skills:** data cleaning, data analysis, data visualization, probability.

**Technology:** Python, Pandas, Numpy, Seaborn, Matplotlib, SciPy

**Results:** Overall, I discovered that the distribution of the aqi_log data is approximately normal. In addition, using statistical methods, it was determined that the site at West Phoenix has worse air quality than the other sites, and is an outlier. finally, the EPA should consider allocating more resources toward further examining this site in order to improve its air quality."

### Analyzing Unicorn Companies and Investment Data

**Code:** [(unicorn_companies.ipynb)](https://github.com/ariannalangton/Portfolio/blob/23547f2771f055c2d4e124c110c900657fcff94c/unicorn_companies.ipynb)

**Goal:** Use skills to clean and investigate data following EDA process. Analyze data trends and find 'Unicorn Companies.'

**Description:** I provided insights to an imaginary investing firm. To help them decide which companies to invest in next, the firm wants insights into unicorn companies–companies that are valued at over one billion dollars. The data I used for this task provides information on over 1,000 unicorn companies, including their industry, country, year founded, and select investors. I will use this information to gain insights into how and when companies reach this prestigious milestone and to make recommendations for next steps to the investing firm.

**Skills:** data cleaning, data analysis, data visualization.

**Technology:** Python, Pandas, Numpy, Seaborn, Matplotlib

**Results:** Using Python functions the analysis revealed that there are 1074 unicorn companies represented in this dataset. Some companies took longer to reach unicorn status but have accrued high valuation as of March 2022. Companies could take longer to achieve unicorn status for a number of reasons, including requiring more funding or taking longer to develop a business model.

### Literacy Data Probability Density
**Code:** [(Literacy Data Probability Density)](https://github.com/ariannalangton/Portfolio/blob/bc2899d2ba3eac19c2004f078ec27446a7830c78/normal_distrib_literacyData.ipynb)   

**Goal:** Use skills to find what probability distribution fits the data, and then use Z-score to find outliers. One of the main goals is to determine which district has the lowest literacy scores.

**Description:** I will be using data from different districts in the U.S. The data includes information from multiple states, and inlcudes the districts literacy score, OVERALL_LI. 

**Skills:** data cleaning, data analysis, data visualization, probability.

**Technology:** Python, Pandas, Numpy, Seaborn, Matplotlib, SciPy

**Results:** Overall, I discovered that the distribution of the aqi_log data is approximately normal. In addition, using statistical methods, it was determined that districts 434 and 494 have Z-scores less than -3, and so are outliers. As a result, there should be more focus on those districts to improve the literacy score.

### Analyzing Meteroite Landings Recorded by NASA
**Code:** [(NASA_Meteorite_data_analysis.ipynb)](https://github.com/ariannalangton/Portfolio/blob/ef320e76983f81345d6d69b4d4bc14628d79b3f7/NASA_Meteorite_data_analysis.ipynb)

**Goal:** Use skills to clean and investigate data following EDA process. Find and analyze most common mass, year, geographical location, name type, and meteorite class.

**Description:** The project focused on analyzing a dataset of meteorite landings from the 1400s to 2014. The dataset included name, id, name type, class, mass, fall type, year, and location. The project involved loading the data, cleaning and preprocessing it, performing exploratory data analysis (EDA), analyzing the most common type, year, and landing location of the meteorites.

**Skills:** data cleaning, data analysis, data visualization.

**Technology:** Python, Pandas, Numpy, Seaborn, Matplotlib, SciPy, Plotly Express

**Results:** Using Python functions the analysis revealed that the year with the most meteorites was 1998. However, the year with the most missing data was 2004 and was followed closely by 2003, which could have skewed the data. For location, the most common spot was (0,0), which is most likely an error. The second most common was in Antarctica. The average mass of all the meteorites was 14020 grams. The average mass was also calcualted for year as well as meteroite class. Ofcourse there are many other characteristics that could have been investigated, but this was enough for my goal.

### Analyzing when companies become a Unicorn Company

**Code:** [(Time to Become a Unicorn Company)](https://github.com/ariannalangton/Portfolio/blob/03b054d573a757fa627a0645e8603680212eb1c0/time_to_unicorn_analysis.ipynb)

**Goal:** Use skills to clean and investigate data following EDA process. Analyze the data for how long it takes companies to reach the status of unicorn company.

**Description:** I offered insights to a hypothetical investment firm to assist them in determining which companies to invest in next. The firm sought information on unicorn companies—those valued at over one billion dollars. The data I analyzed included details on over 1,000 unicorns, such as their industry, country, founding year, and key investors. The investor was particularly interested in understanding the patterns and timing of when companies achieve unicorn status, so I analyzed the data across various timeframes, including years, months, weeks, and quarters.

**Skills:** data cleaning, data analysis, data visualization.

**Technology:** Python, Pandas, Numpy, Seaborn, Matplotlib

**Results:** The analysis showed that 2015 had the highest number of companies founded, indicating that it was the year with the largest concentration of unicorn startups in this dataset. Additionally, a trend emerged where companies founded more recently tended to reach unicorn status more quickly, on average. Focusing on 2021, the most recent year with available data, since trends from 2021 could potentially reflect similar patterns in 2022. The highest number of companies achieving a $1 billion valuation occurred in Week 37 of 2021, which corresponds to the third week of September. After that peak, there was a general decline in the number of companies reaching unicorn status.


### Chaotic Systems of Differenital Equations
**Code:** [(Chaotic differential Systems of Equations)](https://github.com/ariannalangton/Portfolio/blob/504d9f5afff2dddbe197ccc0b9234bba5ea340b6/Chaotic_Systems.ipynb)

**Goal:** Simulate and solve three different chaotic systems of ordinary differential equations; Lorenz, Chua, Rössler. Discover what inital conditions, or coefficients, cause the system to become chaotic attractors. An attractor describes a state to which a dynamical system evolves after a long enough time.

**Description:** Utilized Python to simulate and solve three different chaotic systems of ordinary differential equations; Lorenz, Chua, Rössler. Each system is comprised of their own unique equations and coefficents.
**Skills:** data analysis, data visualization, mathematics.

**Technology:** Python, Pandas, Numpy, Matplotlib, SciPy, mpl_toolkits.mplot3d

**Results:** [(Results Report)](https://github.com/ariannalangton/Portfolio/blob/8b0abda58593d44e2154e09d479c0a5d6e0bceb7/chaotic%20attractors%20results.pdf)

### EDA of TikTok Claim Classification
**Dashboard:** [(EDA of TikTok Claim Classification)](https://github.com/ariannalangton/Portfolio/blob/f71bee213af1bddaca0a58d7f12e75ba229103cb/tiktok_claim_analysis/EDA_TikTok_Claim_Dashboard.pdf)

**Tableau:** [(TikTok Claim Dashboard on Tableau)](https://public.tableau.com/views/EDAofTiktokClaimClassification/Story1?:language=en-US&:sid=&:redirect=auth&:display_count=n&:origin=viz_share_link)

**Goal:** Use TIkTok claim statistics to build easy to understand visualizations.

**Description:** The project aimed to analyze TikTok video user status, claim status, and video statistics such as like count, view count, video duration, and like count.

**Skills:** Tableau, data visualization, box plots, scatter plot

**Results:** By utilizing Tableau's plots and aggregation functions, I created a scatter plot to show the relationship between a videos like count and view count for claims and opinions. In addition, I visualized the total amount of claims v.s opinions, as well as an author status (active, banned, or under review) and the type of video posted by each status.

### League of Legends V13.1 Statistics
**Dashboard:** [(League of Legends V13 Statistics Dashboard IMG)](https://github.com/ariannalangton/Portfolio/blob/5b5126c4eb52a489c2b5a16a198298328f6093d6/league_of__ledgends_dashboard.png)

**Tableau:** [(League of Legends Tableau Dashboard)](https://public.tableau.com/app/profile/arianna.langton5684/viz/leagueoflegendsstats/Dashboard2)

**Goal:** Use League of Legends Champion statistics v13.1 from Kaggle to create a dashboard on Tableau. Analyzed champions and roles by most played, ban rate, and win rate.

**Description:** The project aimed to analyze more than a hundred champions by examining their win, loss, ban, and pick rates. Additionally, I explored the same characteristics for each of the five possible roles.

**Skills:** data cleaning, data analysis, data visualization.

**Results:** By utilizing Tableau's built-in aggregation functions, I determined that Caitlyn was the most played champion, while Zed was the most banned. Furthermore, Singed had the highest win rate among all champions when played in the Mid role, and Mid being the role with the highest overall win rate. Additionally, I visualized the top 8 most played champions and the roles in which they are most frequently selected.

### U.S Women Elected Officials
**Dashboard:** [(U.S Women Elected Officals Dashboard IMG)](https://github.com/ariannalangton/Portfolio/blob/a3e2b93bd28c35742cffb0a9d3f3b0ee5d6185c5/us_women_officials.png)

**Tableau:** [(U.S Women Elected Officials Tableau Dashboard)](https://public.tableau.com/app/profile/arianna.langton5684/viz/U_SWomenElectedOfficialsDemographics/Dashboard2)

**Goal:** Create a Tableau dashboard on the demographics of U.S. women elected officials using data from cawp.rutgers.edu. Analyze race, political party, and state.

**Description:** The project aimed to analyze the demographics of more than a thousand different women elected officials and find trends.

**Skills:** data cleaning, data analysis, data visualization.

**Results:** Using Tableau, I found that 68% of women elected officials are White. The Democratic Party has the highest representation of women, accounting for 64% of all elected women. New Hampshire leads the states with the most elected women, comprising 5.9% of all women in office.

### Grocery Store KPI Dashboard
**Dashboard:** [(Grocery Store KPI Dashboard IMG)](https://github.com/ariannalangton/Portfolio/blob/9e84e895d87f93f932188b19805f45b936bea026/profit%20dashboard.png)

**Tableau:** [(Grocery Store KPI Tableau Dashboard)](https://public.tableau.com/app/profile/arianna.langton5684/viz/2015SalesDashboard_17313755663760/profitdashboard)

**Goal:** Create a Tableau dashboard to easily present KPIs such as sales, profits, quantity sold, sales by region, and category wise sales.

**Description:** Analyzed sales data from Kaggle for an anonymous supermarket. Created Tableau dashboards by analyzing sales KPIs for 2015 as well as geographical sales from 2012-2015.

**Skills:** data cleaning, data analysis, data visualization, KPIs, Sales Metrics.

**Results:** Using Tableau, I discovered that sales for 2015 totaled 4.29M, reflecting a 26.2% increase compared to 2014. Additionally, profit saw a 23.8% year-to-date increase, while the quantity sold rose by 25.9%. The highest sales came from the Technology category, with Phones being the top sub-category. The region generating the most profit for the store was Asia, closely followed by Europe.

## Education

Illinois State University |
Bachelor of Science, Physics |
2019 - 2023

## Certificates

Google Data Analytics Professional Certificate (Aug 2024) (Coursera - Google)

## Contacts
- LinkedIn: [@ariannalangton](https://www.linkedin.com/in/arianna-langton-844b03252)
- Email: anlangton00@gmail.com
