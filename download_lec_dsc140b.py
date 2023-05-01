# Download DSC140B Lectures PDFs.
# PDF will have a file name in the format of "LEC_2_Linear_Algrebra.pdf" for "Lecture 2 Linear Algrebra", for example.

import requests
import os
from bs4 import BeautifulSoup

# make a request to the website
url = 'http://dsc140b.com/index.html'
response = requests.get(url)

# path of the folder to save the pdfs
file_path = '/Users/daphneyang/Desktop/DSC140B/Lectures/'

# parse the HTML response with Beautiful Soup
soup = BeautifulSoup(response.text, 'html.parser')

sections = soup.findAll('h3', class_="schedule-week-component-title")
for sec in sections:
    if sec.text.strip() == "Dr. Eldridge's Lectures":
        all_list = sec.parent.findAll('li', class_='schedule-resource')
        for li in all_list:
            links = li.findAll('a')
            for link in links:
                pdf_link = link.get('href')
                if pdf_link.split('/')[-1] == 'marked.pdf':
                    lecture_title = ' '.join([s.strip()
                                             for s in li.span.strings]).strip()
                    lecture_title = lecture_title + '.pdf'
                    lecture_title = file_path + \
                        lecture_title.replace(
                            ' ', '_').replace('Lecture', 'LEC')

                    if not os.path.exists(lecture_title):
                        pdf_link = 'http://dsc140b.com/' + pdf_link
                        pdf = requests.get(pdf_link)
                        with open(lecture_title, 'wb') as f:
                            f.write(pdf.content)
