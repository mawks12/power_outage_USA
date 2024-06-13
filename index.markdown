---
# Feel free to add content and custom Front Matter to this file.
# To modify the layout, see https://jekyllrb.com/docs/themes/#overriding-theme-defaults

layout: default
---
# The Data
**Overview**  
For this project, we will be working with a dataset of Power outages, covering the years 2000-2016. The documentation for the data specified that these are considered "major" outages, meaning that they affected at least 50,000 customers or caused an unplanned firm load loss of at least 300MW, and was obtained from the U.S. Department of Energy. It was originaly used assesing weather related power outage risks [^fn]. The dataset contained 1534 outages, and 59 different features. In our analysis, we have analized various trends in the data, as well as some of the disitributions of the data. We have also generated a model predicting the outage time using a number of the features in the dataset. Ideally, this kind of a model could be very usefull for keeping the public updated in the early moments of an outage. The Data points that were primiarily of interest to us where features like weather and land usage data. We did some analysis of the peak demand loss during an outage, but this data would not be avaliable untill after an outage had been resolved, so it was not used in our predictive model. All analysis was done in Python, using the Pandas, Numpy, and Scikit-learn libraries, and is publicly available on our GitHub repository, linked in the top right corner of this page.

**Initial Data Cleaning**  
The original dataset contained a number of columns, many of which were not used in our analysis. A complete list of all of the columns in the dataset can be found [here](https://www.sciencedirect.com/science/article/pii/S2352340918307182#bib1) under Table 1. The columns that were used in our analysis were: "TODO: list columns used"
Some of the columns where modified to make them more useful for our analysis. For example, the "OUTAGE.START.DATE" and "OUTAGE.RESTORATION.DATE" columns were converted to datetime objects and merged with the "OUTAGE.START.TIME" and "OUTAGE.RESTORATION.TIME". The "OUTAGE.DURATION" column was also converted to a timedelta object. Afterwords, these were merged into one value, containing the full date and time of the outage. Original Dates and times
where left as seperate values in case they could become usefull in training a prediction model.

A portion of resulting table:  

|   OBS |   YEAR | outageStart         | outageEnd           |
|------|-------|--------------------|--------------------|
|     1 |   2011 | 2011-07-01 17:00:00 | 2011-07-03 20:00:00 |
|     2 |   2014 | 2014-05-11 18:38:00 | 2014-05-11 18:39:00 |
|     3 |   2010 | 2010-10-26 20:00:00 | 2010-10-28 22:00:00 |
|     4 |   2012 | 2012-06-19 04:30:00 | 2012-06-20 23:00:00 |
|     5 |   2015 | 2015-07-18 02:00:00 | 2015-07-19 07:00:00 |

# Data Analysis  
**Univariate Analysis**  
We explored a couple of interesting distributions in our initial analysis. What initialy interested us were the outages by each state, so we created a per capita bar graph where we could look at the distribution of that data. As shown below, we found one interesting data point, namely that deleware has an increibly high number of outages per capita. Upon further exploration, we found that they had a fairly average number of outages for their very low population. More specific analysis would have to be done to determine why this might be the case.
<iframe
    src='assets/univar.html'
    width='100%'
    height='500'
    frameborder='0'
></iframe>


**Bivariate Analysis**  
Something that interested us in the data was if the affects of global warming could be seen on the data. We grouped the data by year, and looked at the preportion of outages that were caused by weather events. We found that the proportion of outages caused by weather events seems to have been decreacing over time, but there does exist one very low data point in 2001 which skews this distribution. This will be of further interest when preforming hypothesis testing.
<iframe
    src='assets/bivar.html'
    width='100%'
    height='500'
    frameborder='0'
></iframe>

**Aggrigate Analysis**
Finialy, we were curious about the very low outage duration values, and if there might be any correlation with weather events causing near zero length outaged. to that end, we genetated the following table, showing average duration based on the anomaly level.

|   ANOMALY.LEVEL |    0.0 |      1.0 |
|----------------|-------|---------|
|            -1.3 |    0   | nan      |
|            -1.1 | 1040   | nan      |
|            -1   |    0   | nan      |
|            -0.9 |    1.4 | nan      |
|            -0.8 |    0   | nan      |
|            -0.7 |    0   | nan      |
|            -0.6 |    0   | nan      |
|            -0.5 |    0   | 728.333  |
|            -0.4 |    0.2 | 157.5    |
|            -0.3 |    0   |  18.3333 |
|            -0.1 |    0   | nan      |
|             0.1 |  nan   |   0      |
|             0.3 |    0   |   0      |
|             0.6 |  nan   |  12      |
|             0.8 |  nan   |   0      |
|             1.6 |    0   | nan      |
|             2.3 |  nan   |   0      |

Sadly, there seem to be too many nan values for us to be able to draw any conclusions from this data, however there do seem to be a couple of very high values that might be worth further investigation.

# Missingness
**Not Missing at Random**  
We would hypothesize that the outage cause column contains values that would not be missing dependent on any other column in the data set, or at least not strongly correlated. Since these values would have to have been filled after determining the cause of an outage, any outage type who's cause is not obvious or difficult to determine would not have made it into the data set. For instance, if an outage was caused by a squirrel chewing through a power line, it would be difficult to determine the cause of the outage, and it would likely not be included in the data set.

**Missing at Random**  
We initialy theorized that most values that were missing might be dependent on the overall wealth of the state, since wealthier states would be able to build more robust and expensive infrasturcture that could more easily log information on power outages. To that end, we grouped all of our values by state and plotted the proportion of missing values for each state against the GDP of that state. We found very little correlation between the two, and so we can not say that the missingness of the data is dependent on the wealth of the state.


<iframe
    src='assets/missing.html'
    width='100%'
    height='500'
    frameborder='0'
></iframe>


# Hypothosis Testing
**Weather Outages**
We were interested in continuing to look into the proportion of weather related outaged over time, so this was the main focus of our hypothesis testing, using the following:  
H<sub>0</sub>: There is no correlation betweeen time and the preportion of weather related power outages  
H<sub>1</sub>: Weather related outages have decreased over time  
We took the data for the plot we generated in our data analysis section, and computed a pearsons R correlation coefficient. The results where interesting, as we found little to no correlation with the 2001 data point present, and very strong correlation when it was removed. Since we were unable to determine the 2001 data point as an outlier, our resulting p value of 0.1 meant that we were unable to reject the null hypothesis. However, we were interested in the cause of the very low preportion, and therefore made a bar graph of the causes of outages during 2001, as can be seen below.

<iframe
    src='assets/hypo.html'
    width='100%'
    height='500'
    frameborder='0'
></iframe>
We can see clearly that there is a very high number of system operability disruptions that occured in 2001. Unfortunately, more detailed information for this does not exist in our dataset, so we are unable to determine the cause of this.

# Predictive Modeling
**Prediction of Outage Time**  
We built a reggression model to predict the duration of an outage based on the features in the dataset. Primaraly, this would be quite usefull for keeping the public informed during an outage, as well as determining the allocation of reasorces during an outage. Since the model is intended to make a prediction at the time of the outage event, certain features that would not be avaliable at that time where not used in the model. For example, the peak demand loss during an outage would not be avaliable until after the outage had been resolved, so it was not used in our model. We used R<sup>2</sup> as our metric for evaluating the model, as it is easy to interperate, and a decent approximation of accuracy when working with regression models. 

**Baseline Model**  
We started with a fairly simple model, trained on the following features:  
- Cause (Nominal): some causes seem to be highly correlated with longer outages, likely because they take longer to fix.
- Customers Affected (Quanitative): The more customers that are affected by an outage, (in theory) the higher the priority of fixing that outage would be
- Total.Sales (Quanitative): the total amount of power that is put out to the customers would likely imply a larger grid, and probably better infrastructer, making outage response time much better
- POPDEN_UC (Quanitative): Population density in urban clusters would correlate to the number of people that are affected, and how large the grid is - like above, larger grid likely means better ability to fix it
- PC.REALGSP.CHANGE (Quanitative): the change in states gross product year on year is probably correlated with how well it is able to run it's power grid, and how much money is in the state at a time. If this goes down suddenly, a state is likely less able to handle difficult outages, because there may be some budget cuts
- Anomaly level (Quanitative): A measruement of how much of an el nino year it is. If this value is more extreme, the weather may be more severe, and therefore make fixing outaged more difficult
- PCT_WATER_INLAND (Quanitative): in theory, this could be usefull in combination with the previous data point, since more water inland probably means more storms and therefore more difficulty fixing power outages

Since we had only one nominal feature, we used a one hot encoder to convert it into a number of binary features. For our other features, a simple standard scalar was applied to normalize the data. Although this step is not strictly nessesary, since we are using a Random Forest Regressor, but we incorporated it in case we determined that a new model might preform better on our prediction problem. We used a Random Forest Regressor as our model, since it is a very robust model that is able to handle a large number of features, and is able to handle non-linear relationships between the features and the target variable, which we did find were present. We used a 5 fold cross validation to evaluate the model, and found that it had an R<sup>2</sup> value of 0.21, which is not very good overall, but possibly could be improved. Ideal, we would like a model that has a high enough R<sup>2</sup> value that it could be usefull for public information. Since 80% of the variance in the data is not explained by the model, it is not currently usefull for this purpose.

**Model Improvement**
One of the first issues we resolved was the number of missing values present in the origional data. Since we were not training on a massive number of features, we were able to individualy analize the missingess of each of the features with missing values, allowing us to impute them more effectively when building our model. In our origional model, we used the ItteritiveImputer from sklearn, however we found that this was not very effective in imputing the missing values, and therefore wrote a custom imputation scheme that uses probabalistic imputation according to a group. This was far more effective in imputing the missing values, and we were able to use this to train a new model. We also two new features to the model. We first took the percentage of water inland and multiplied it by the anomaly level, to encode both values in one, since the percentage of water likely has no strong correlation on its own. Additionaly, we found the preportion of a states population that was affected by an outage, and multiplied this by the total sales, to get a value that would be more indicative of the amount of power that was lost during an outage. We used the same model as before, and found that the R<sup>2</sup> value increased to 0.22. The optimal hyperparameters for the model where found using a grid search, resulting in an ideal number of trees at 10 and a maximum depth of 70. Overall, the model did not predict very well using the given dataset, which is likely to do with the features avaliable to us in this data set. In our reaserch for this project, we came accross an interesting study preforming the same task, whos dataset contained far more detailed causes of an outage, as well as live updates from the power grid [^fn]. Their model preformed far better, and this is likely due to the more detailed data that they had avaliable to them.

# Fairness Evaluation
Afterwords, we evaluated the fairness of our model on different regions, since some regions contained more missing values and are generaly less wealthy than others. As low economic status is likely correlated with a higher number of outages, we wanted to ensure that our model was not biased against these regions. We therefore grouped our data by the region, and computed the R<sup>2</sup> value for each region. We found that the R<sup>2</sup> value was fairly consistent across all regions, as confirmed by the chi-squared test we ran on the data, returing a p value of 0.5. Thus, our model is unlikely to have any bias against any particular region.


[^fn]: [Sayanti Mukherjee, Roshanak Nateghi, Makarand Hastak](https://www.sciencedirect.com/science/article/pii/S0951832017307767)
[^fn]: [Aaron Jaech, Baosen Zhang, Member, IEEE, Mari Ostendorf, Fellow, IEEE and Daniel S. Kirschen, Fellow, IEEE](https://arxiv.org/pdf/1804.01189)