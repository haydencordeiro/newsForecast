from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import unicodedata
import smtplib

chrome_options = Options()  
chrome_options.add_argument("--headless")
driver = webdriver.Chrome(chrome_options=chrome_options)
# driver=webdriver.Firefox()
driver.get("https://www.ndtv.com/latest?pfrom=home-mainnavgation")

a=driver.find_elements_by_xpath('//div[@class="nstory_header"]')
b=driver.find_elements_by_xpath('//div[@class="new_storylising_contentwrap"]')
msg=''
for i in range(len(a)):
	headline=a[i].text
	summary=b[i].text
	summary=summary[len(headline):]
	link=driver.find_element_by_partial_link_text(headline[:len(headline)//2])
	link=(link.get_attribute('href'))
	
	msg+=headline+'\n'+summary+'\n'+link+'\n\n'


	# print(headline)
	# msg+=headline+'\n'
	# msg+=summary[len(headline):]+'\n\n'
	# print(headline)
	# print(summary[len(headline):])
	# tempHeadline=headline.split()
	# print(headline)
	# indexOf=tempHeadline.index('2020,')
	# tempHeadline=tempHeadline[indexOf+1:]
	# headline=''
	# for i in tempHeadline:
	# 	headline+=i+' '
	# print(headline)



	


def send(m):
	toaddrs=["brijitjoffy8910@gmail.com","adnsequeira20@gmail.com"]
	try:
	if(len(m)<10):
		m='No Task For today'
		fromaddr = 'brijitjoffy8910@gmail.com'
		username = 'brijitjoffy8910@gmail.com'
		msg = 'Subject: {}\n\n{}'.format("Here's some latest news", m)
		print(msg)
		password ='wjtgcdwwlppjkslz'
		server = smtplib.SMTP('smtp.gmail.com:587')
		server.starttls()
		server.login(username,password)
		server.sendmail(fromaddr, toaddrs, msg)
		server.quit()
		print('send')
			
	except:
		print('error occured')




# print(m)
send(msg)