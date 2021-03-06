import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options


def main():
    """ Main entry point of the app """
    get_omroepzeeland()


def get_omroepzeeland():
        chrome_options = Options()
        # chrome_options.add_argument("--headless")
        browser = webdriver.Chrome(options=chrome_options)
        url = "https://www.omroepzeeland.nl/zoeken?query=windmolens"
        browser.get(url)
        time.sleep(1)

        # find all article links and make a list
        url_list = []
        url_con = browser.find_element_by_class_name('search-results')
        links = url_con.find_elements_by_tag_name("a")
        for url in links:
            url_list.append(url.get_attribute('href'))

        # Create and open csv
        file = open("Data/omroep_zeeland.csv", mode="w", encoding="utf-16")

        # Write header to csv
        file.write(f'Origin;Content\n')

        for url in url_list:
            browser.get(url)
            container = browser.find_elements_by_id('storytelling')

            if container:
                content_blocks = container[0].find_elements_by_tag_name('p')

            else:
                continue

            # tekst uit artikel alle p's bij elkaar
            text = ''
            for block in content_blocks:
                text += block.text
            # print(text)

            # Write new line to csv
            file.write('\n')

            # Write url and text from articles to csv
            # file.write("Omroepzeeland" + ';')
            # file.write(text.replace('\n',''))
            endtext = text.replace('\n','')

            # deleting ad's
            endtext = endtext.replace('Razendsnel toegang tot het laatste Zeeuwse nieuws, het weer, sport en live radio en tv? Download de Omroep Zeeland app voor Android of iPhone/iPad.', '')

            file.write("Omroepzeeland" + ';' + endtext)
            print(endtext)


if __name__ == "__main__":
    """ This is executed when run from the command line """
    main()
