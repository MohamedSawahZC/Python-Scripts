from unittest import result
import requests
from bs4 import BeautifulSoup
import csv
import lxml
from itertools import zip_longest

job_title = []
company_name = []
locations_name = []
job_skill = []
links = []

# 2nd Step use request to fetch the url

result = requests.get(
    "https://wuzzuf.net/search/jobs/?q=Back-end+developer&a=hpb")

# 3rd step save page content/markup

src = result.content

# print(src)

# 4th step create soup object to parse content

soup = BeautifulSoup(src, "lxml")

# print(soup)

# 5th step find the element containing info we need

job_titles = soup.find_all("h2", {"class": "css-m604qf"})
company_names = soup.find_all("a", {"class": "css-17s97q8"})
locations_names = soup.find_all("span", {"class": "css-5wys0k"})
job_skills = soup.find_all("div", {"class": "css-y4udm8"})

# 6th step loop over the list to get needed info only without tags and added to another lists

for i in range(len(job_titles)):
    job_title.append(job_titles[i].text)
    company_name.append(company_names[i].text)
    locations_name.append(locations_names[i].text)
    job_skill.append(job_skills[i].text)
    links.append(job_titles[i].find("a").attrs['href'])


# 7th step create csv file and fill it with values
file_list = [job_title, company_name, locations_name, job_skill, links]
exported = zip_longest(*file_list)
with open('Web Scrapping/jobs.csv', "w") as myfile:
    wr = csv.writer(myfile)
    wr.writerow(['Job Title', "Company", "Locations", "Job Skills", "Links"])
    wr.writerows(exported)
