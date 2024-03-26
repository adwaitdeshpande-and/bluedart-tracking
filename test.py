from bs4 import BeautifulSoup
import requests
# import os
from tabulate import tabulate

def remove_blank_string(content:list):
    output_list = []
    content.pop(0)
    content.pop()
    for item in content:
        if item != "":
            output_list.append(item)
    return output_list

def get_status(id:int):
    url = f"https://www.bluedart.com/trackdartresultthirdparty?trackFor=0&trackNo={id}"
    class_name = "panel-bd-List"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "lxml")
    div_element = soup.find("div", class_=class_name)
    div_content = ""
    if div_element:
        div_content = div_element.text.strip()
    return(div_content.splitlines())

def get_content(id:id):
    url = f"https://www.bluedart.com/trackdartresultthirdparty?trackFor=0&trackNo={id}"
    div_id = f"SCAN{id}"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "lxml")
    div_element = soup.find("div", id=div_id)
    if div_element:
        div_content = div_element.text.strip()
        return(in_table(remove_blank_string(div_content.splitlines())))
    else:
        return(f"Div element with ID '{div_id}' not found.")

def in_table(data:list):
    sublists = []
    for i in range(0, len(data), 4):
        sublist = data[i:i + 4]
        sublists.append(sublist)
    table = str(sublists[:2])
    return table
