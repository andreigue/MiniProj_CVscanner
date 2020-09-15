#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#install the python-docx module using "pip3 install python-docx"
"""
Created on Sun Sep  6 19:18:51 2020

@author: andrei
"""

import re
#import docx

#get document text
'''doc = docx.Document("/home/andrei/Desktop/testDocument.docx")
all_paras = doc.paragraphs

for para in all_paras:
    print(para.text)
    print("-------")
'''

doc = open('/home/andrei/Desktop/gitProjects/MiniProd/CVScanner/testDocument.txt')
docContent = doc.read()

phoneNumRegex = re.compile(r'''(
        (\d{3} | \(\d{3}\))?    #possible area code (just three digits, or digits between parantheses)
        (\s | - | \.)?          #possile separator (space, dash, or dot)
        (\d{3})                 #first three digits
        (\s | - | \.)           #separator
        (\d{4})                 #last 4 digits
        )''', re.VERBOSE)       #VERBOSE allows us to comment inside the regex

print(phoneNumRegex.findall(docContent))    #gives not-so-nice look    

#Phone number finder
matches = []
for groups in phoneNumRegex.findall(docContent):
    phoneNum = '-'.join([groups[1], groups[3], groups[5]])
    matches.append(phoneNum)
if (len(matches)>1):
    print("More than one phone number found. Unecessary. -1 pt.")
else:
    print("phone number found: " + phoneNum+ ". +1 pt.")

#Email finder
emailRegex = re.compile(r'''(
        [a-zA-Z0-9]+       #username
        @                       # @ symbol
        [a-zA-Z0-9]          #domain name
        (\.[a-zA-Z]{2,4})       # dot-something, 2 to 4 characters long
        )''', re.VERBOSE)
for groups in emailRegex.findall(docContent):
    matches.append(groups[0])
    print(groups[0])

# pattern = "[a-zA-Z0-9]+@[a-zA-Z]+\.(com|edu|net|ca)"   #for testing


 


#mo = phoneNumRegex.search(docContent)
#print("the phone number is : " + mo.findall())