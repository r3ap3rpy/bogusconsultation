from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
import os
import itertools
import argparse
import requests

male = requests.get('https://www2.census.gov/topics/genealogy/1990surnames/dist.male.first?#')
fmale = requests.get('https://www2.census.gov/topics/genealogy/1990surnames/dist.female.first?#')

male = [_.split(' ')[0] for _ in male.text.split('\n') if _]
fmale = [_.split(' ')[0] for _ in fmale.text.split('\n') if _]


parser = argparse.ArgumentParser(description='Auto filler for the bullshi consultation our government spends billions to brainwash people.')
parser.add_argument('-participants','--participants' ,type = int, help='The number of people filling the form.', required=True)
args = parser.parse_args()

if args.participants < 1 or args.participants > 5_000_000:
    raise SystemExit("Must be between 1 and 5_000_000!")


prod = list(itertools.product(male, fmale))

prod = prod[:args.participants]
print(len(prod))

vnev = '//*[@id="vezeteknev"]'
knev = '//*[@id="keresztnev"]'
email = '//*[@id="email_cim"]'
kor = '//*[@id="eletkor"]'

hunvagyok = '/html/body/div[3]/main/section/div/div/div[2]/form/div/div[1]/div[3]/div[1]/label'
lua = '/html/body/div[3]/main/section/div/div/div[2]/form/div/div[1]/div[3]/div[2]/label'
onwards = '/html/body/div[3]/main/section/div/div/div[2]/form/div/div[1]/div[4]/button'


first = '/html/body/div[3]/main/section/form/div[2]/div/div/div[2]/ul/li[8]/label'
second = '/html/body/div[3]/main/section/form/div[3]/div/div/div[2]/ul/li[2]/label'
third = '/html/body/div[3]/main/section/form/div[4]/div/div/div[2]/ul/li[2]/label'
fourth = '/html/body/div[3]/main/section/form/div[5]/div/div/div[2]/ul/li[2]/label'
fifth = '/html/body/div[3]/main/section/form/div[6]/div/div/div[2]/ul/li[2]/label'
sixth = '/html/body/div[3]/main/section/form/div[7]/div/div/div[2]/ul/li[2]/label'
seventh = '/html/body/div[3]/main/section/form/div[8]/div/div/div[2]/ul/li[2]/label'
eigth = '/html/body/div[3]/main/section/form/div[9]/div/div/div[2]/ul/li[2]/label'
ninth = '/html/body/div[3]/main/section/form/div[10]/div/div/div[2]/ul/li[2]/label'
tenth = '/html/body/div[3]/main/section/form/div[11]/div/div/div[2]/ul/li[2]/label'
eleventh = '/html/body/div[3]/main/section/form/div[12]/div/div/div[2]/ul/li[2]/label'
twelveth = '/html/body/div[3]/main/section/form/div[13]/div/div/div[2]/ul/li[2]/label'
thirteenth = '/html/body/div[3]/main/section/form/div[14]/div/div/div[2]/ul/li[2]/label'

answers = (first,second,third,fourth,fifth,sixth,seventh,eigth,ninth,tenth,eleventh,twelveth,thirteenth)

sendin = '/html/body/div[3]/main/section/form/div[15]/div[1]/button'
agree = '/html/body/div[3]/main/section/form/div[16]/div/div/div/div[3]/div[2]/button[2]/strong'

foxy = webdriver.Firefox(executable_path=os.path.sep.join(['source','geckodriver.exe']))
foxy.get("https://nemzetikonzultacio.kormany.hu/")

vnevElement = WebDriverWait(foxy, 10).until(lambda driver: driver.find_element_by_xpath(vnev))
vnevElement.send_keys('anyatoaaakat')
raise SystemExit
knevElement = WebDriverWait(foxy, 10).until(lambda driver: driver.find_element_by_xpath(knev))
knevElement.send_keys('basszaaaamarcon')

emailElement = WebDriverWait(foxy, 10).until(lambda driver: driver.find_element_by_xpath(email))
emailElement.send_keys('anyatoakaaat@basszaamaaarcon.hu')

korElement = WebDriverWait(foxy, 10).until(lambda driver: driver.find_element_by_xpath(kor))
korElement.send_keys('99')

hunvagyokElement = WebDriverWait(foxy, 10).until(lambda driver: driver.find_element_by_xpath(hunvagyok))
hunvagyokElement.click()

luaElement = WebDriverWait(foxy, 10).until(lambda driver: driver.find_element_by_xpath(lua))
luaElement.click()

onwardsElement = WebDriverWait(foxy, 10).until(lambda driver: driver.find_element_by_xpath(onwards))
onwardsElement.click()

for answer in answers:
    target = foxy.find_element_by_xpath(answer)
    foxy.execute_script('arguments[0].scrollIntoView(true);', target)
    element =  WebDriverWait(foxy, 10).until(lambda driver: driver.find_element_by_xpath(answer))
    element.click()



sendinElement = WebDriverWait(foxy, 10).until(lambda driver: driver.find_element_by_xpath(sendin))
sendinElement.click()

agreeElement = WebDriverWait(foxy, 10).until(lambda driver: driver.find_element_by_xpath(agree))
agreeElement.click()

foxy.close()
