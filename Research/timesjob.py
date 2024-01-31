from bs4 import BeautifulSoup 
import requests
import time
from urllib.parse import urljoin
import re

#Input for search bar
print(f'Put job field')
job= input('>')
print(f'Filtering out {job}')
job_field = job.replace(' ','+')

def sanitize_filename(filename):
    # Replace invalid characters with underscores
    filename= re.sub(r'[\/:*?"<>|]', '_', filename)
    filename=filename.strip('. ')
    return filename


def find_jobs(): 
    
    #goto user given field link
    field_link = requests.get(f'https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&searchTextSrc=&searchTextText=&txtKeywords={job_field}&txtLocation=').text
    soup = BeautifulSoup(field_link,'lxml')
    
    #gets the basic list of every job
    jobs = soup.find_all('li', class_= 'clearfix job-bx wht-shd-bx')

    for index, job in enumerate(jobs):
        
        # Get the link of particular job
        more_info = job.header.h2.a["href"]

        # Request access for that page
        more_info_text = requests.get(more_info).text
        job_link_soup =BeautifulSoup(more_info_text,'lxml')


        #extracts title
        job_title=job_link_soup.find('h1',class_='jd-job-title').text.strip().replace(" ", '')

        #extracts company name
        company = job_link_soup.h2.text.replace(' ','')


        # Extracting job description
        job_description = job_link_soup.find('div', class_ = 'jd-desc job-description-main').get_text(strip=True)
        # Extracting job basic info
        basic_info = job_link_soup.find('div', class_='job-basic-info')
        job_basic_info = basic_info.find_all('li', class_ = 'clearfix')
        if len(job_basic_info)>=2:

            # job function
            job_f_div = job_basic_info[0]
            job_f = job_f_div.find('span', class_='basic-info-dtl')
            if job_f:
                job_function = job_f.get_text(strip=True)
            else:
                job_function = ""

            #job industry
            indus_div = job_basic_info[1]
            indus = indus_div.find('span', class_='basic-info-dtl')
            if indus:
                industry = indus.get_text(strip=True)
            else:
                industry = ""
            
            specialize_div = job_basic_info[2]
            specialize = specialize_div.find('span', class_='basic-info-dtl')
            if specialize:
                specialization = specialize.get_text(strip=True)
            else:
                specialization = ""

            
            quali_div = job_basic_info[3]
            #quali = quali_div.find('ul')
            if quali_div:
                qualification = quali_div.get_text(strip=True)
            else:
                qualification = ""

            #employment_type
            emp_div = job_basic_info[4]
            if emp_div:
                emp = emp_div.get_text(strip=True)
            else:
                emp = ""
            extra_info= ""   
            if len(job_basic_info) >= 6:
            #if (job_basic_info[5]==True):
                extra_div=job_basic_info[5]
                if extra_div:
                    extra_info= extra_div.get_text(strip=True)
                
            

    #       roles={}
     #       if len(job_basic_info) >= 4:
      #          for i in range(len(job_basic_info) - 4, len(job_basic_info)):
       #             role_div = job_basic_info[i]
        #            if role_div:
         #               roles[f'role{i}']= role_div.get_text(strip= True)
          #          else:
           #             roles[f'role{i}'] = ""

        #extracts skills
        skills_container = job_link_soup.find('div', class_='jd-sec job-skills clearfix')
        skills_header = skills_container.find('h3').get_text(strip=True)

        # Check if the header is 'Key Skills'
        if skills_header.lower() == 'key skills':
            #skill_div = skills_container.find('div', class_ = 'clearfix')
            skills_elements = skills_container.find_all('span', class_='jd-skill-tag')
            skills= []
            for skills_element in skills_elements:
                if skills_element.a :
                    skill = skills_element.a.get_text(strip=True)
                else:
                    skill= skills_element.get_text(strip=True)
                skills.append(skill)
        else:
            print("No skills found.")

        # Writes into file 
        job_title_sanitized = sanitize_filename(job_title)
        
        # Writes into file    
        with open(f'TJ/{job_title_sanitized}{index}.txt','w') as f:
            f.write(f'JOB TITLE: {job_title}\n')
            f.write(f"COMPANY NAME: {company.strip()}\n")
            f.write(f"JOB DESCRIPTION: {job_description} \n")
            f.write(f"JOB FUNCTION: {job_function} \n")
            f.write(f"JOB INDUSTRY: {industry} \n")
            f.write(f"SPECIALIZATION: {specialization} \n")
            f.write(f"{qualification} \n")
            f.write(f"{emp} \n")
            f.write(f"{extra_info}\n")
            f.write(f"SKILLS: {', '.join(map(str.strip, skills))} \n")
        print(f'File saved :{job_title}{index}')               

find_jobs()
