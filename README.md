# instagram_automated
Automated Instagram aggregator page that downloads saved posts and reposts them with appropriate credits and captions. 

EDIT: Due to Instagram regularly updating the way their site is coded, it breaks the web scraper code. Therefore, this script may no longer be working until it is updated for the latest html structure. 

# What is this for?
Instagram is full of unique and innovative UI/UX and Web designers. As someone who is interested in this topic, I find myself constantly looking for inspirtation on Instagram for my own designs. Currently there exists many pages such as @interfacely, @morrre.dsgn, @readymag etc. who act as a sort of aggregator pages. These collect works of designers and repost them on their pages to help spotlight them and provide inspiration for others.

This project similarly tries to set up an aggregator Instagram account, but tries to automate many of the processes invovled. If you would like to see this account in action please visit @ui.expo on Instagram: https://www.instagram.com/ui.expo/


# What each file does

**insta_scrape_saved.py**
- This script automatically downloads all posts that I have saved in the Instagram app into a folder.
- As I see designs that I like during my usual browse of the app, I save them to a specifc Instagram "collection" called "to_post"
- This file then uses the Selenium package to webscrape these images alongside other relvent data.

**post_bot.py**
- Using the instabot package primarily, this file allows me to then repost the saved files to Instagram
- It also allows me to add a pre-written caption with hashtags that credits the original poster.


# Next steps

**insta_scrape.py**
- When this script runs, instead of scraping posts from my saved folder, it instead goes to the "explore" section and inputs a hashtag set in the insta_scraper function
- This then goes through the most recent posts and dowloads them all. 

Next, I will manually go through these and label each one "good" or "bad" (with 1s and 0s). I will also include all the posts I have posted so far or are contained in the saved collection. These will all be automatically labeled "good". 

Once this is completed I will experiment with various Machine Learning models (and perhaps Deep Learning techniques if I have enough data) to create a program that can automatically download and then sort the posts into good and bad. The alogrithm will be based on my own personal preferences for what I subjectively see to be good design. 

**What else could be added?**
- Automatically check for comments and like them
- Reply to comments from a list of pre-set replies
- Use AI techniques to generate custom captions or replies to comments
- Automatically follow other users and like their posts (to help speed up growth)
- Recreate this framework for other topics, e.g. Bushcraft, cooking, cars etc.   
