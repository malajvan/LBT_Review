from bs4 import BeautifulSoup
import pandas as pd
import numpy as np
with open('source.html','r') as source:
    soup = BeautifulSoup(source,'html.parser')
reviews=(soup.find_all("div",class_="jftiEf fontBodyMedium")) #reviews
reviewer_name, profile,review_id,text,star,time=[],[],[],[],[],[]

for re in reviews:
    reviewer_name.append(re['aria-label'])
    review_id.append(re['data-review-id'])
    profile.append(re.find("div",class_="WNxzHc qLhwHc").find("a")['href'])
    star.append(re.find("span",class_="kvMYJc")['aria-label'][1])
    time.append(re.find("span",class_="rsqaWe").getText().replace('\n', ' '))
    text.append(re.find("div",class_="MyEned").getText().replace('\n\n', ' ')[6:])
df = pd.DataFrame({'reviewer_name':reviewer_name, 'review_id': review_id, 'profile_href':profile, 'star':star,'time':time, 'text':text})
df.index.name='index'
df.to_csv('reviews.csv')

    


"""
understanding the data:
    * data-review-id: componenets from the same review
    * MyEned: class name for review texts
    * class="kvMYJc":aria-label is stars: ie. " 5 stars ", " 1 star "...
    * class="WNxzHc qLhwHc": reviewers' profile
    * class="rsqaWe": reviews' time : "ago"
    * jstcache="345": # of reviews given of reviewer
"""

"""
todo:
    * finish dataframe
    * convert time to a standard time?
    * clean data    

"""