#!/usr/bin/env python
# coding: utf-8

# In[1]:


from bs4 import BeautifulSoup
import requests


# In[2]:


#function to extract product title
def get_title(soup):
    try:
        title=soup.find('span',attrs={"id":"productTitle"})
        title_string=title.get_text(strip=True)
    except AttributeError:
        title_string=""
    return title_string

#function to extract product price
def get_price(soup):
    try:
        price=soup.find('span',attrs={"class":"a-offscreen"})
        if price is not None:
            price_string=price.get_text(strip=True)
        else:
            price_string=""
    except AttributeError:
        price_string=""
    return price_string

#function to extract product rating
def get_rating(soup):
    try:
        rating=soup.find('span',attrs={"class":"a-icon-alt"})
        if rating is not None:
            rating_string=rating.get_text(strip=True)
        else:
            rating_string=""
    except AttributeError:
        rating_string=""
    return rating_string

#function to extract number of user reviews
def get_review_count(soup):
    try:
        review_count=soup.find('span',attrs={"id":"acrCustomerReviewText"})
        if review_count is not None:
            review_count_string=review_count.get_text(strip=True)
        else:
            review_count_string=""
    except AttributeError:
        review_count_string=""
    return review_count_string

#function to extract availability status
def get_availability(soup):
    try:
        availability=soup.find('div',attrs={"id":"availability"})
        if availability is not None:
            availability_string=availability.get_text(strip=True)
        else:
            availability_string=""
    except AttributeError:
        availability_string=""
    return availability_string

if __name__=="__main__":
    headers={
        "User-Agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36",
        "Accept-Language": "en-US,en;q=0.5"

    }
    
    url="https://www.amazon.com/Sony-PlayStation-Pro-1TB-Console-4/dp/B07K14XKZH/"
    
    webpage=requests.get(url,headers=headers)
    soup=BeautifulSoup(webpage.content,"html.parser")
    
    print("Product Title =",get_title(soup))
    print("Product Price =",get_price(soup))
    print("Product Rating =",get_rating(soup))
    print("Number of Product Reviews =",get_review_count(soup))
    print("Availability =",get_availability(soup))


# In[ ]:




