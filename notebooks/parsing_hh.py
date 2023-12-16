from bs4 import BeautifulSoup
from pprint import pprint

with open("../data/htmls/electro3.html", "r", encoding="utf-8") as file:
    html_content = file.read()

soup = BeautifulSoup(html_content, "html.parser")

title_element = soup.find(attrs={"data-qa": "vacancy-title"})
content = title_element.get_text() if title_element else "Job title not found"

salary_element = soup.find(attrs={"data-qa": "vacancy-salary"})
salary = (
    salary_element.span.get_text()
    if salary_element and salary_element.span
    else "Salary not specified"
)

experience_element = soup.find(attrs={"data-qa": "vacancy-experience"})
experience = (
    experience_element.get_text() if experience_element else "Experience not specified"
)

employment_element = soup.find(attrs={"data-qa": "vacancy-view-employment-mode"})
employment = (
    employment_element.get_text()
    if employment_element
    else "Employment mode not specified"
)

description_element = soup.find(attrs={"data-qa": "vacancy-description"})
description = (
    description_element.get_text()
    if description_element
    else "Job description not available"
)

skills_elements = soup.find_all(
    attrs={"data-qa": "bloko-tag bloko-tag_inline skills-element"}
)
skills = (
    " ".join(element.get_text() for element in skills_elements)
    if skills_elements
    else "Skills not specified"
)

raw_address_element = soup.find(
    attrs={"data-qa": "vacancy-view-raw-address"}
)
address = (
    raw_address_element.get_text()
    if raw_address_element
    else "Raw address not available"
)

location_element = soup.find(
    attrs={"data-qa": "vacancy-view-location"}
)
location = (
    location_element.get_text()
    if location_element
    else "Location is not specified"
)

print("Заработная плата: " + salary)
print("Должность: " + content)
print("Локация: " + location)
print("Адрес: " + address)
print("Тип занятости: " + employment)
print("Требуемый опыт работы: " + experience)
print("Описание: " + description)
print("Навыки: " + skills)
