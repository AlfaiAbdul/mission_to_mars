# # Scraping

# Dependencies
from bs4 import BeautifulSoup
import requests
import pymongo
from splinter import Browser
import tweepy
import time
import pandas as pd

# Scrape function
def Scrape():

    print("Scrape communication Active")
    print("----------------------------------")
    print("-----------------------------")
    print("------------------------")
    print("-------------------")
    print("--------------")
    print("---------")
    print("---")

    # Empty dictionary
    mars_dict = {}

    # ## NASA Mars News

    # Mars News URL
    url = "https://mars.nasa.gov/news/"

    # Retrieve page with the requests module
    html = requests.get(url)

    # Create BeautifulSoup object; parse with 'html.parser'
    soup = BeautifulSoup(html.text, 'html.parser')

    # Get title & description
    news_title = soup.find('div', 'content_title', 'a').text
    news_p = soup.find('div', 'rollover_description_inner').text

    # Add to dict
    mars_dict["news_title"] = news_title
    mars_dict["news_p"] = news_p

    print("NEWS TITLE & DESCRIPTION ACQUIRED")


    # ## JPL Mars Space Images

    # JPL Mars URL
    url = "https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars"

    # Setting up splinter
    executable_path = {'executable_path':'./chromedriver'}
    browser = Browser('chrome', **executable_path, headless=False)
    browser.visit(url)

    # through pages
    time.sleep(5)
    browser.click_link_by_partial_text('FULL IMAGE')
    time.sleep(5)
    browser.click_link_by_partial_text('more info')
    time.sleep(5)

    # BeautifulSoup object (parse with html.parser)
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')

    # Get featured image
    results = soup.find('article')
    extension = results.find('figure', 'lede').a['href']
    link = "https://www.jpl.nasa.gov"
    featured_image_url = link + extension

    mars_dict["featured_image_url"] = featured_image_url

    print("---Image Acquired---")


    # ## Mars Weather

    # Twitter API key and token
    consumer_key = "l74SDiLmcEx1I20Y5pDLztp3S"
    consumer_secret = "KVGUQc7Dfw8UIJGIILwW7RfypF7CAzqt2RO4Z90hLkBafdKJC9"
    access_token = "948782567410380800-eQzM7rwLaSQpxNZ6cZgegIAgcfCymal"
    access_token_secret = "9shx4gxSCkMWTfBhvVDKojHtBDKwpHwCj1LaylGF9Ao5r"

    # Tweepy Authenticate
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth, parser=tweepy.parsers.JSONParser())

    # Target User
    target_user = "@MarsWxReport"

    # Get tweet
    tweet = api.user_timeline(target_user, count=1)[0]

    # Store weather
    mars_weather = tweet['text']

    mars_dict["mars_weather"] = mars_weather

    print("---Weather Acquired---")


    # ## Mars Facts

    # Mars Facts URL
    url = "https://space-facts.com/mars/"

    # Retrieve page with the requests 
    html = requests.get(url)

    # BeautifulSoup object (parse with html.parser)
    soup = BeautifulSoup(html.text, 'html.parser')

    # Empty dict for info.
    mars_profile = {}

    # Get info
    results = soup.find('tbody').find_all('tr')

    # Stor info.
    for result in results:
        key = result.find('td', 'column-1').text.split(":")[0]
        value = result.find('td', 'column-2').text
        
        mars_profile[key] = value
        
    # Create DataFrame
    profile_df = pd.DataFrame([mars_profile]).T.rename(columns = {0: "Value"})
    profile_df.index.rename("Description", inplace=True)

    # DataFrame to html
    profile_html = "".join(profile_df.to_html().split("\n"))

    # Adding to dictionary
    mars_dict["profile_html"] = profile_html

    print("FACTS ACQUIRED")


    # ## Mars Hemispheres

    # Mars Hemispheres URL
    url = "https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"

    # list of image urls
    hemisphere_image_urls = []


    # ### Valles Marineris

    # Setting up splinter
    executable_path = {'executable_path':'./chromedriver'}
    browser = Browser('chrome', **executable_path, headless=False)
    browser.visit(url)

    # through pages
    time.sleep(5)
    browser.click_link_by_partial_text('Valles Marineris Hemisphere Enhanced')
    time.sleep(5)

    # BeautifulSoup object (parse with html.parser)
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')

    # Store link
    valles_link = soup.find('div', 'downloads').a['href']

    # Create dict
    valles_marineris = {
        "title": "Valles Marineris Hemisphere",
        "img_url": valles_link
    }

    # Append dict
    hemisphere_image_urls.append(valles_marineris)


    # ### Cerberus

    # Setting up splinter
    executable_path = {'executable_path':'./chromedriver'}
    browser = Browser('chrome', **executable_path, headless=False)
    browser.visit(url)

    # through pages
    time.sleep(5)
    browser.click_link_by_partial_text('Cerberus Hemisphere Enhanced')
    time.sleep(5)

    # BeautifulSoup object (parse with html.parser)
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')

    # Store link
    cerberus_link = soup.find('div', 'downloads').a['href']

    # Create dict
    cerberus = {
        "title": "Cerberus Hemisphere",
        "img_url": cerberus_link
    }

    # Append dict
    hemisphere_image_urls.append(cerberus)


    # ### Schiaparelli

    # Setting up splinter
    executable_path = {'executable_path':'./chromedriver'}
    browser = Browser('chrome', **executable_path, headless=False)
    browser.visit(url)

    # through pages
    time.sleep(5)
    browser.click_link_by_partial_text('Schiaparelli Hemisphere Enhanced')
    time.sleep(5)

    # BeautifulSoup object (parse with html.parser)
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')

    # Store link
    schiaparelli_link = soup.find('div', 'downloads').a['href']

    # Create dict
    schiaparelli = {
        "title": "Schiaparelli Hemisphere",
        "img_url": schiaparelli_link
    }

    # Append dict
    hemisphere_image_urls.append(schiaparelli)


    # ### Syrtis Major

    # Setting up splinter
    executable_path = {'executable_path':'./chromedriver'}
    browser = Browser('chrome', **executable_path, headless=False)
    browser.visit(url)

    # through pages
    time.sleep(5)
    browser.click_link_by_partial_text('Syrtis Major Hemisphere Enhanced')
    time.sleep(5)

    # BeautifulSoup object (parse with html.parser)
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')

    # Store link
    syrtis_link = soup.find('div', 'downloads').a['href']

    # Create dict
    syrtis_major = {
        "title": "Syrtis Major Hemisphere",
        "img_url": syrtis_link
    }

    # Append dict
    hemisphere_image_urls.append(syrtis_major)

    # Add to dict
    mars_dict["hemisphere_image_urls"] = hemisphere_image_urls

    print("Images Acquired")
    print("---")
    print("---------")
    print("--------------")
    print("-------------------")
    print("------------------------")
    print("-----------------------------")
    print("----------------------------------")
    print("Scraping is complete")

    return mars_dict