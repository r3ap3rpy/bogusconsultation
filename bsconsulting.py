from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from queue import Queue

import os
import itertools
import argparse
import requests
import threading


if not os.sys.platform == "win32":
    raise SystemExit("This script can only run on windows!")

parser = argparse.ArgumentParser(description='Auto filler for the bullshi consultation our government spends billions to brainwash people.')
parser.add_argument('-participants','--participants' ,type = int, help='The number of people filling the form.', required=True)
parser.add_argument('-threads','--threads', type = int, help = "The number of worker threads.", required = False, default=8)
args = parser.parse_args()

male = requests.get('https://www2.census.gov/topics/genealogy/1990surnames/dist.male.first?#')
fmale = requests.get('https://www2.census.gov/topics/genealogy/1990surnames/dist.female.first?#')

male = [_.split(' ')[0] for _ in male.text.split('\n') if _]
fmale = [_.split(' ')[0] for _ in fmale.text.split('\n') if _]

if args.participants < 1 or args.participants > 5_000_000:
    raise SystemExit("Must be between 1 and 5_000_000!")

JobQueue = Queue()
print(f"Running on {args.threads} thread(s)!")
prod = list(itertools.product(male, fmale))

prod = prod[:args.participants]
print(f"Number of participiants: {len(prod)}")








class BSinfo(threading.Thread):
    def __init__(self, jobqueue):
        threading.Thread.__init__(self)
        self.jobqueue = jobqueue
        self.vnev = '//*[@id="vezeteknev"]'
        self.knev = '//*[@id="keresztnev"]'
        self.email = '//*[@id="email_cim"]'
        self.kor = '//*[@id="eletkor"]'
        self.hunvagyok = '/html/body/div[3]/main/section/div/div/div[2]/form/div/div[1]/div[3]/div[1]/label'
        self.lua = '/html/body/div[3]/main/section/div/div/div[2]/form/div/div[1]/div[3]/div[2]/label'
        self.onwards = '/html/body/div[3]/main/section/div/div/div[2]/form/div/div[1]/div[4]/button'
        self.first = '/html/body/div[3]/main/section/form/div[2]/div/div/div[2]/ul/li[8]/label'
        self.second = '/html/body/div[3]/main/section/form/div[3]/div/div/div[2]/ul/li[2]/label'
        self.third = '/html/body/div[3]/main/section/form/div[4]/div/div/div[2]/ul/li[2]/label'
        self.fourth = '/html/body/div[3]/main/section/form/div[5]/div/div/div[2]/ul/li[2]/label'
        self.fifth = '/html/body/div[3]/main/section/form/div[6]/div/div/div[2]/ul/li[2]/label'
        self.sixth = '/html/body/div[3]/main/section/form/div[7]/div/div/div[2]/ul/li[2]/label'
        self.seventh = '/html/body/div[3]/main/section/form/div[8]/div/div/div[2]/ul/li[2]/label'
        self.eigth = '/html/body/div[3]/main/section/form/div[9]/div/div/div[2]/ul/li[2]/label'
        self.ninth = '/html/body/div[3]/main/section/form/div[10]/div/div/div[2]/ul/li[2]/label'
        self.tenth = '/html/body/div[3]/main/section/form/div[11]/div/div/div[2]/ul/li[2]/label'
        self.eleventh = '/html/body/div[3]/main/section/form/div[12]/div/div/div[2]/ul/li[2]/label'
        self.twelveth = '/html/body/div[3]/main/section/form/div[13]/div/div/div[2]/ul/li[2]/label'
        self.thirteenth = '/html/body/div[3]/main/section/form/div[14]/div/div/div[2]/ul/li[2]/label'
        self.sendin = '/html/body/div[3]/main/section/form/div[15]/div[1]/button'
        self.agree = '/html/body/div[3]/main/section/form/div[16]/div/div/div/div[3]/div[2]/button[2]/strong'

        self.answers = (self.first,self.second,self.third,self.fourth,self.fifth,self.sixth,self.seventh,self.eigth,self.ninth,self.tenth,self.eleventh,self.twelveth,self.thirteenth)
    def run(self):
        while True:
            CurrentParticipiant = self.jobqueue.get()
            print(CurrentParticipiant)

            self.foxy = webdriver.Firefox(executable_path=os.path.sep.join(['source','geckodriver.exe']))
            self.foxy.get("https://nemzetikonzultacio.kormany.hu/")

            self.vnevElement = WebDriverWait(self.foxy, 10).until(lambda driver: driver.find_element_by_xpath(self.vnev))
            self.vnevElement.send_keys(CurrentParticipiant[0])

            self.knevElement = WebDriverWait(self.foxy, 10).until(lambda driver: driver.find_element_by_xpath(self.knev))
            self.knevElement.send_keys(CurrentParticipiant[1])
            
            self.emailElement = WebDriverWait(self.foxy, 10).until(lambda driver: driver.find_element_by_xpath(self.email))
            self.emailElement.send_keys(f'{CurrentParticipiant[0]}@{CurrentParticipiant[1]}.hu')
            
            self.korElement = WebDriverWait(self.foxy, 10).until(lambda driver: driver.find_element_by_xpath(self.kor))
            self.korElement.send_keys('99')
            
            self.hunvagyokElement = WebDriverWait(self.foxy, 10).until(lambda driver: driver.find_element_by_xpath(self.hunvagyok))
            self.hunvagyokElement.click()
            
            self.luaElement = WebDriverWait(self.foxy, 10).until(lambda driver: driver.find_element_by_xpath(self.lua))
            self.luaElement.click()
            
            self.onwardsElement = WebDriverWait(self.foxy, 10).until(lambda driver: driver.find_element_by_xpath(self.onwards))
            self.onwardsElement.click()
            
            for answer in self.answers:
                self.target = self.foxy.find_element_by_xpath(answer)
                self.foxy.execute_script('arguments[0].scrollIntoView(true);', self.target)
                self.element =  WebDriverWait(self.foxy, 10).until(lambda driver: driver.find_element_by_xpath(answer))
                self.element.click()

            self.sendinElement = WebDriverWait(self.foxy, 10).until(lambda driver: driver.find_element_by_xpath(self.sendin))
            self.sendinElement.click()

            self.agreeElement = WebDriverWait(self.foxy, 10).until(lambda driver: driver.find_element_by_xpath(self.agree))
            self.agreeElement.click()

            self.foxy.close()
            self.jobqueue.task_done()


for ppl in prod:
    JobQueue.put(ppl)

for i in range(args.threads):
    t = BSinfo(JobQueue)
    t.setDaemon(True)
    t.start()



JobQueue.join()

raise SystemExit()

