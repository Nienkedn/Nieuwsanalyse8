import time
import datetime
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def main():
    get_nu_nl()


def get_nu_nl():
    # Setup selenium instance
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    browser = webdriver.Chrome(options=chrome_options)
    url = "https://www.nu.nl/tag/windmolens"
    browser.get(url)
    time.sleep(1)

    # Scroll down until the load more button has reached it's end
    while len(browser.find_elements_by_link_text("Laad meer artikelen")) > 0:
        # Scroll down to load more articles and find needed elements
        scroll_button = browser.find_element_by_link_text('Laad meer artikelen')
        browser.execute_script("arguments[0].click();", scroll_button)
        time.sleep(0.1)

    # find all article links and make a list
    containers = browser.find_elements_by_xpath("//div[@class='block-content clearfix']")
    url_list = []

    for container in containers:
        urls_con = container.find_elements_by_class_name('trackevent')
        for url_con in urls_con:
            url_list.append(url_con.get_attribute('href'))
    print(url_list[-1])

    # Create and open csv
    file = open("Data/nu_nl.csv", mode="w", encoding="utf-16")
    # Write header to csv
    file.write(f'Origin,Timestamp,Content,Title,Comment_count,Retweet_count\n')
    for url in url_list:
        browser.get(url)
        # Get timestamp article
        date_con = browser.find_element_by_xpath("//span[@class='pubdate small']")
        date = date_con.get_attribute('innerHTML')
        timestamp = datetime.datetime.strptime(date, "%d-%m-%y %H:%M").timestamp()

        # Get content article
        content_articles = browser.find_element_by_xpath("//div[@data-type='article.body']")
        raw_content = content_articles.find_element_by_class_name('block-content')
        contents = raw_content.find_elements_by_tag_name('p')
        content_complete = ""
        for p in contents:
            content_complete += p.get_attribute('innerHTML')

        # Get title article
        article_title = browser.find_element_by_xpath("//h1[@class='title fluid']")

        # Write data to csv
        content = content_complete.replace(',', '').replace('\n', '')
        article_title = article_title.text.replace(',', '')
        file.write(f'nu.nl,{timestamp},{content},{article_title},0,0\n')
    file.close()


if __name__ == "__main__":
    """ This is executed when run from the command line """
    main()
