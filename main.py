from selenium import webdriver

chrome_driver_path = "/Users/prog/VScode/python/webdev/chromedriver"

driver = webdriver.Chrome(executable_path=chrome_driver_path)

sony_90mm_url = "https://www.amazon.com/Sony-SEL90M28G-Standard-Prime-Mirrorless-Cameras/dp/B00U29GNEG/ref=sr_1_1?dchild=1&keywords=sony+90mm&qid=1625705826&s=apparel&sr=1-1"

driver.get(sony_90mm_url)

response = driver.find_element_by_id("priceblock_ourprice")

print(response.text)

driver.quit()

# <span id = "priceblock_ourprice" class = "a-size-medium a-color-price priceBlockBuyingPriceString" >$1, 098.00 < /span >


# //*[@id="h.e02b498c978340a_87"]/div/div/ul[1]/li[2]/p
