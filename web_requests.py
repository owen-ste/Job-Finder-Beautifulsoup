from bs4 import BeautifulSoup
import requests
import time


unfamiliar_li = []
print("Put unfamiliar skills:")
unfamiliar_skill = input('>')
unfamiliar_li = unfamiliar_skill.split()
print(f"Filtering out {unfamiliar_skill}")
undesired_companies = []
desired_company = True


def find_jobs():
    html_text = requests.get('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=python&txtLocation=').text
    soup = BeautifulSoup(html_text, 'lxml')
    jobs = soup.find_all('li', class_ = 'clearfix job-bx wht-shd-bx')
    for job in jobs:
        published_date = job.find('span', class_ = 'sim-posted').span.text
        if 'few' in published_date:
            company_name = job.find('h3', class_ ='joblist-comp-name').text.replace(' ','')
            skills = job.find('span', class_ = 'srp-skills').text.replace(' ','')
            more_info = job.header.h2.a['href']
            for i in unfamiliar_li:
                if i in skills:
                    undesired_companies.append(company_name.strip())
                
    for index, job in enumerate(jobs):
        published_date = job.find('span', class_ = 'sim-posted').span.text
        if 'few' in published_date:
            company_name = job.find('h3', class_ ='joblist-comp-name').text.replace(' ','')
            skills = job.find('span', class_ = 'srp-skills').text.replace(' ','')
            more_info = job.header.h2.a['href']
            desired_company = True
            for j in undesired_companies:
                    if company_name.strip() == j:
                        desired_company = False
            for i in unfamiliar_li:
                if i not in skills and desired_company:
                    with open(f'posts/{index}.txt', 'w') as f:
                        f.write(f"Company Name: {company_name.strip()} \n")
                        f.write(f"Required Skills: {skills.strip()} \n")
                        f.write(f"More Info: {more_info} \n")
                    print(f"File saved: {index}")

if __name__ == '__main__':
    while True:
        find_jobs()
        time_wait = 10
        print(f"Waiting {time_wait} minutes...")
        time.sleep(time_wait * 60.0)