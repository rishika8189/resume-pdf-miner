#!/usr/bin/env python
# coding: utf-8

# In[8]:


import re
import csv
import os
from pdfminer.high_level import extract_text

phone_pattern=re.compile(r"\b\d{10}\b") 
email_pattern=re.compile(r"[\w\.-]+@[\w\.-]+")
college_pattern=re.compile(r".*?\b(?:college|university|institute|school)\s+(?:of\s+)?[\w\s-]+.*",re.IGNORECASE)
degree_pattern=re.compile(r".*\b(?:bachelor|bachelors|master|masters|b.tech|m.tech)\b.*",re.IGNORECASE) 
skill_pattern = re.compile(r"(?i)\b(python|java|c\+\+|javascript|aws|power bi|sql|data analytics|statistics|machine learning|ms excel|eda|data visualisation)\b")  
exp_pattern = re.compile(r'^.*?\bintern\b.*?$', re.IGNORECASE | re.MULTILINE) 

resume_folder = 'C:/Users/arora/Desktop/onelogica/OneLogica/OneLogica'

for resume_file in os.listdir(resume_folder):

      if resume_file.endswith('.pdf'):
  
        pdf_path = os.path.join(resume_folder,resume_file)
        text = extract_text(pdf_path)

        name = text.strip().split('\n')[0]   
        phone = phone_pattern.findall(text)
        email = email_pattern.findall(text)
        college = college_pattern.findall(text)
        degree = degree_pattern.findall(text)
        skills = skill_pattern.findall(text)
        experience = exp_pattern.findall(text)   

        with open('C:/Users/arora/Desktop/onelogica/pdfminer/output_pdf.xlsx', 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([name,phone,email,college,degree,skills,experience])
print('Resume extraction complete!')


# In[ ]:




