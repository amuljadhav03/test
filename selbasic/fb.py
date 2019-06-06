from selenium import webdriver

bro = 'firefox'
if(bro =='chrome'):
    driver = webdriver.Chrome(executable_path="C:/Users/AMUL JADHAV/Downloads/Drivers/chromedriver.exe")
elif(bro =='firefox'):
    driver = webdriver.Firefox(executable_path='C:/Users/AMUL JADHAV/Downloads/Drivers/geckodriver.exe')
else:
    print("no browser path")

driver.get('https://www.facebook.com')

