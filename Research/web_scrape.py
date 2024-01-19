import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

print(f'Put job field that you want')
user_input = input('>')
print(f'Filtering out {user_input}')

def get_job_links(category_link):

    category_html = requests.get(category_link).text
    category_soup = BeautifulSoup(category_html, 'lxml')
    job_elements = category_soup.find_all('h1', class_='text-primary font-weight-bold media-heading h4')

    for index, job_element in enumerate(job_elements):
        link_element = job_element.a['href']
        if link_element:
            #provides link of respective job
            job_link = urljoin('https://merojob.com/', link_element)
            
            response = requests.get(job_link)
            job_link_soup=BeautifulSoup(response.text,'lxml')

            # Extracts title
            job_title=job_link_soup.find('h1',class_='h4 mb-0 text-primary').text

            # Extracts basic info
            basic_info_element= job_link_soup.find('div', class_='card-body p-0 table-responsive')
            if basic_info_element:
                basic_info=basic_info_element.get_text(strip=True)
            else:
                job_title = ""

            #Extract Job Specification
                
            #job_specif_element= job_link_soup.find('tr', class_='table table-hover m-0')
                
            # Extract Job Specification
            job_specif_elements = job_link_soup.find_all('div', class_='card-body p-0 table-responsive')
            if len(job_specif_elements) >= 2:
                job_specif_div = job_specif_elements[1]
                job_specif_table = job_specif_div.find('table', class_='table table-hover m-0')

                if job_specif_table:
                    job_specif_div_text = job_specif_div.get_text(strip=True)

                else:
                    job_specif = ""

            # Extracts Other Specification
            job_ospecif_element= job_link_soup.find('div', class_='card-text p-2')
            if job_ospecif_element:
                job_ospecif= job_ospecif_element.get_text(strip=True)
            else:
                job_ospecif = ""

            # Extracts Job Description
            job_descrip_element= job_link_soup.find('div', class_='card-text p-2',itemprop ='description')
            if job_descrip_element:
                job_descrip= job_descrip_element.get_text(strip=True)
            else:
                job_descrip = ""

            # Writes into file 
                
            with open(f'JD/{index}.txt','w') as f:
                f.write(f'JOB TITLE: {job_title.strip()}\n\n')
                f.write(f"BASIC INFO: {basic_info} \n\n")
                f.write(f"JOB SPECIFICATION: {job_specif_div_text} \n\n")
                f.write(f"OTHER SPECIFICATION: {job_ospecif} \n\n")
                f.write(f"JOB DESCRIPTION: {job_descrip} \n\n")
            print(f'File saved :{index}')




html_text = requests.get('https://merojob.com/').text
soup = BeautifulSoup(html_text, 'lxml')

# Finds the browse jobs section
category_elements = soup.find_all('div', class_='category-list rounded py-2 col-md-4 py-1')

for category_element in category_elements:
    link_element = category_element.find('a')

    # Provides the selected field link
    if link_element:
        category_name = link_element.text.strip()
        category_link = urljoin('https://merojob.com/', link_element.get('href'))  

        if user_input.lower() in category_name.lower():
            job_data_list = get_job_links(category_link)      
    else:
        print("No 'a' element found in category.")


