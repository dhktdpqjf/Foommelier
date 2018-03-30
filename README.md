# Foommelier
Food recommendation system based on content-based filtering recommendation algorithm with Python

HMR Food recommendation
- This is on target to busy people like college students or office workers who can't spend their time cooking very much.
 
1. Data Set - Data set is gathered from Ottugi, Lotte Food, Bae-min-chan which are big food distribution company and make a delivery of instant food.
  
2. Data Analysis
- Normalization 
  : all of portion size, nutrient, calories are continuous variable which needs to be normalized.

- Clustering
  : We need to figure out which cluster a record is included in. So we performed K-means algorithm which helps to make 500 records to
    14 clusters.

- Pearson correlation coefficient
  : It is made use of collaborative filtering algorithm and pearson correlation coefficient in it. 

Open your fridge
- This is for people who enjoy cooking at home with food ingredients from their fridge.
 
1. Data Set
- Data set is collected from Naver Recipe page. Data crawling is also programmed with python and HTML. 
  
2. Data Analysis
- Normalization
  : We set 5.0 to main ingredients and 2.5 to supplementary ingredients which are offered at the service page clearly when we use data       crawler program. This works when we perform the filtering algorithm with euclidian distance score for weights.
  
- Euclidian distance score
  : It is made use of collaborative filtering algorithm and euclidian distance score is applied to it.
  
3. Front end
  It offers hyperlinks to click on which links to the service page showing cooking process of food.

Let's have dinner 
- This is menu planning service based on health. Users can enter their health information like chronic disease, BMI or what they want to focus(ex. bulk-up, losing weight). This is a program not only to recommend menu but also make estimate of user's grade for it.

1. Data Set
- Data set is brought from Open your Fridge data set. 
  
2. Data Analysis
- Linear Regression Analysis
  : We set the customer satisfaction to dependent variable and perform linear regression analysis. 
