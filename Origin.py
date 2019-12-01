# import the libs
from selenium import webdriver
import time


#initial for user, password, and url
usr ='type your email here'
psswd = 'type your password here'
url = 'https://www.origin.com/'

# create the initial window
browser = webdriver.Chrome("D:\Workplace\learningpython\chromedriver")

# go to the home page
browser.get(url)

#for maximize window
browser.maximize_window()

# storing the current window handle to get back to dashbord
mainPage = browser.current_window_handle

# wait for page to load completely
time.sleep(5)

# click on the sign in tab
browser.find_element_by_xpath("//*[@id='shell']/section/div/nav/div/div[5]/ul/li[1]/origin-cta-login/origin-cta-primary").click()
# wait for page to load completely
time.sleep(2)


# changing the handles to access login page
for handle in browser.window_handles:
    if handle != mainPage:
        loginPage = handle

# change the control to signin page
browser.switch_to.window(loginPage)
# enter the email
browser.find_element_by_id('email').send_keys(usr)
# enter the password
browser.find_element_by_id('password').send_keys(psswd)
# click the login button
browser.find_element_by_xpath("//*[@id='logInBtn']").click()

# wait for page to load completely
time.sleep(2)
# change control to main page
browser.switch_to.window(mainPage)
# wait for page to load completely
time.sleep(5)
#Type Battle field V in searchbox and press enter
browser.find_element_by_xpath("//*[@id='shell']/section/div/nav/div/div[1]/div[3]/origin-global-search/div/form/label/div/input").send_keys('battle field v')
# wait for page to load completely
time.sleep(5)
#choose battle field V
browser.find_element_by_xpath('//*[@id="content"]/origin-search-page/div/origin-search-results[1]/div/ul/li[1]/origin-store-premier-browse-tile/div/otkex-hometile/a/div/h1[1]').click()


print('Done')


