from selenium import webdriver

# Will test our web service.
# Will get the application URL as an input, open a browser to that URL, select the score
# element in our web page, check that it is a number between 0 to 1000 and return a
# boolean value if it’s true or not.
def test_scores_service(app_url):
    driver = webdriver.Chrome(executable_path="C:\\Users\\Hodaya\\Downloads\\chromedriver.exe")
    driver.get(app_url)
    score_element = driver.find_element_by_xpath('//*[@id="score"]')
    score = int(score_element.text)
    return True if score <= 100 and score >= 1 else False

# Will call our tests function.
# The main function will return -1 as an OS exit code if the tests failed and 0 if it passed.
def main_function():
    flag = test_scores_service("http://127.0.0.1:5000/score_server")
    return 1 if flag == False else 0

print(main_function())