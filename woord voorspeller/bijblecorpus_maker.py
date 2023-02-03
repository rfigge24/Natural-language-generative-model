# -*- coding: utf-8 -*-
"""
Created on Fri May 20 12:25:44 2022

@author: rfigg
"""

with open("./Het-Boek.txt", "r", encoding = "utf-8") as conn:
    text = conn.read()

lines = text.splitlines()

onlylines = []

for line in lines:
    if len(line.split() ) > 4:
        verse = line.split()[0]
        onlylines.append(line.replace(verse, ""))



with open("./Het-Boek-cleaned.txt", "w", encoding = "utf-8") as outfile:
    for line in onlylines:
        outfile.write(line)
    
        