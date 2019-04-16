import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

__author__ = "Your Name"
__version__ = "0.1.0"
__license__ = "MIT"


def main():
    """ Main entry point of the app """
    get_twitter()


def get_twitter():
    # Setup selenium instance
    chrome_options = Options()
    # chrome_options.add_argument("--headless")
    browser = webdriver.Chrome(options=chrome_options)
    url = "https://twitter.com/search?q=%20windmolens&src=typd&lang=nl"
    browser.get(url)
    time.sleep(1)

    # Define body and scroll down to load tweets
    body = browser.find_element_by_tag_name('body')

    scroll_count = 0
    tweet_count = 0
    while True:
        scroll_count += 1
        body.send_keys(Keys.END)
        time.sleep(0.1)
        if scroll_count % 100 is 0:
            print(f"@{scroll_count}")
            new_tweet_count = len(browser.find_elements_by_class_name('_timestamp'))
            if new_tweet_count == tweet_count:
                print("True")
                break
            else:
                print("False")
                print(f'Old Tweet Count: {str(tweet_count)}')
                print(f'New Tweet Count: {str(new_tweet_count)}')
                tweet_count = new_tweet_count

    # Get all tweets and dates
    tweets = browser.find_elements_by_xpath("//p[@class='TweetTextSize  js-tweet-text tweet-text']")
    dates = browser.find_elements_by_class_name('_timestamp')
    tweet_info_containers = browser.find_elements_by_xpath("//div[@class='ProfileTweet-actionList js-actions']")

    comment_counts = []
    retweet_counts = []
    for info in tweet_info_containers:
        counts = info.find_elements_by_class_name('ProfileTweet-actionCountForPresentation')
        comment_counts.append(counts[0])
        retweet_counts.append(counts[1])

    # Create and open csv
    file = open("Data/tweets.csv", mode="w", encoding="utf-16")
    # Write header to csv
    file.write(f'Origin,Timestamp,Content,Title,Comment_count,Retweet_count\n')
    for i, tweet in enumerate(tweets):
        # Prepare data for csv
        date = dates[i].get_attribute("data-time")
        tweet = tweet.text.replace(',', '').replace('\n', '')
        comment_count = comment_counts[i].text
        retweet_count = retweet_counts[i].text
        if comment_count is '':
            comment_count = 0
        if retweet_count is '':
            retweet_count = 0
        file.write(f'twitter,{date},{tweet},Null,{comment_count},{retweet_count}\n')
    file.close()


if __name__ == "__main__":
    main()
