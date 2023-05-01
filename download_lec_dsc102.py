# Download WI23 DSC102 Lectures PDFs.
# PDF will have a file name in the format of "DSC102_LEC_5_Computer_Organization_Part_2-b.pdf" 
# for "LEC 5 Computer Organization Part 2-b", for example.

import requests
import os
from bs4 import BeautifulSoup

# make a request to the website
url = 'https://rod-albuyeh-labs.github.io/dsc102-sp23/'
response = requests.get(url)

# path of the folder to save the pdfs
file_path = '/Users/daphneyang/Desktop/DSC102/Lectures/'

# parse the HTML response with Beautiful Soup
soup = BeautifulSoup(response.text, 'html.parser')

lecs = soup.findAll('strong', class_="label label-lecture")
for lec in lecs:
    link_component = lec.parent.find('a')
    link = link_component.get('href')

    lecture_title = file_path + ('DSC102_' + lec.text.strip() + ' ' +
                                 link_component.text).strip().replace(':', '')\
        .replace(' ', '_') + '.pdf'

    if not os.path.exists(lecture_title):
        pdf_link = url + link
        pdf = requests.get(pdf_link)
        with open(lecture_title, 'wb') as f:
            f.write(pdf.content)
