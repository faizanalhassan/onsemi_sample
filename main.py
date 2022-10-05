from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService


def scraper():
    explore_urls = ["https://www.onsemi.com/products/"]
    result_urls = []
    # url =
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    new_explore_found = True
    while len(explore_urls) != 0:
        url = explore_urls.pop(0)  # .shift in node.js
        driver.get(url)
        explore_anchors = driver.find_elements(By.XPATH, "//div[@class='mt-auto']/a[.='Explore']")
        result_anchors = driver.find_elements(By.XPATH, "//div[@class='mt-auto']/a[.='View Parametric Table']")
        for anchor in explore_anchors:
            explore_urls.append(anchor.get_attribute('href'))

        for anchor in result_anchors:
            result_urls.append(anchor.get_attribute('href'))

    print(len(explore_urls), len(result_urls))

    for result_url in result_urls:
        pass


if __name__ == '__main__':
    scraper()


