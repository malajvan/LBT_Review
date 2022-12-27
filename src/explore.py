from bs4 import BeautifulSoup
import pandas as pd
import numpy as np
import nltk
import re
import datetime
from dateutil.relativedelta import relativedelta

with open('source.html','r') as source:
    soup = BeautifulSoup(source,'html.parser')
reviews=(soup.find_all("div",class_="jftiEf fontBodyMedium")) #reviews
reviewer_name, profile,review_id,text,star,time=[],[],[],[],[],[]

stopwords=nltk.corpus.stopwords.words('english')

for r in reviews: #initializing dataframe and clean up text
    reviewer_name.append(r['aria-label'])
    review_id.append(r['data-review-id'])
    profile.append(r.find("div",class_="WNxzHc qLhwHc").find("a")['href'])
    star.append(r.find("span",class_="kvMYJc")['aria-label'][1])
    time.append(r.find("span",class_="rsqaWe").getText().replace('\n', ' '))
    text.append(r.find("div",class_="MyEned").getText().replace('\n\n', ' '))
df = pd.DataFrame({'reviewer_name':reviewer_name, 'review_id': review_id, 'profile_href':profile, 'star':star,'time':time, 'text':text})
df.index.name='index'
# df.to_csv('reviews.csv')

clean_text=[]
#clean data
for r in text:
    r=r.lower()
    r=re.sub("[^a-z]",' ',r)
    r=r.split()
    r=[w for w in r if not w in set(stopwords)]
    r=' '.join(r)
    #getting only the translated part
    if 'translated google' in r:
        r=r.split('translated google')
        r=r[1]
    clean_text.append(r)

#convert time from relative to approximate literal 
current_date=datetime.datetime(2022, 12, 20,0,0,0)  #last time data collected was Dec 20th 2022
# print( current_date.strftime("%Y/%m/%d, %H:%M:%S"))
clean_time=[] 
for d in time:
    d=d.strip()
    d=d.split()
    if d[0]=="a":
        d[0]=1
    if d[1] in ["month","year","week",'day','hour','minute']:
        d[1]=d[1]+'s'
    d=current_date+eval(f"relativedelta({d[1]}=-{d[0]})")

    clean_time.append(d)

clean_df = pd.DataFrame({'reviewer_name':reviewer_name, 'review_id': review_id, 'profile_href':profile, 'star':star,'time':clean_time, 'text': clean_text})
clean_df.to_csv('clean_reviews.csv')



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


"""