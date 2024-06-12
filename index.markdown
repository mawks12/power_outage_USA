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
Some of the columns where modified to make them more useful for our analysis. For example, the "OUTAGE.START.DATE" and "OUTAGE.RESTORATION.DATE" columns were converted to datetime objects and merged with the "OUTAGE.START.TIME" and "OUTAGE.RESTORATION.TIME".The "OUTAGE.DURATION" column was also converted to a timedelta object.






[^fn]: [Sayanti Mukherjee, Roshanak Nateghi, Makarand Hastak](https://www.sciencedirect.com/science/article/pii/S0951832017307767)