# LBT_Review
Sentiment analysis on La Belle Tonki's Google reviews using Machine Learning.
## Background
Google Maps and Google Business has become one of the most important platform for businesses, especially restaurants, to find and attract new customers, communicate with old ones, and improve the establisments. Reviews left by customers on Google doesn't only give credibility for the restaurant and excites potential diners, but also provide an insight into how the restaurant is operating: what is done right, and what needs improvement. 

As La Belle Tonki gain more popularity, maintaining a good reputation and managing the consistent quality of operation is crucial longevity and further development. Having insights into their own (or other's) Google reviews can be a very benefitial tool.

## Data 
The data was gathered using Selenium and beautifulsoup from Google Maps. Close to 1000 English text reviews were extracted and preprocessed using NLP techniques (removing stop words and punctuations, Lemmatization) along with star ratings and datetime information.
Due to the way Google shows datetime information, more unspecified time was round off to the nearest common time unit (year, month, hour, minute)

## Methods
Used tf-idf to extract important keywords and developing main themes:
1. Food
2. Service
3. Vibe
Using Random Forest model for sentiment analysis. Analyses trend and visualized with graphs

## Discussions
All findings were presented to the restaurant's owners. Details in the Report coming soon.

## Authors

