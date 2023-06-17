from typing import Dict, Any

import requests
from bs4 import BeautifulSoup

link = "https://career.habr.com/vacancies"
vacancylink  = {}
search_vacancy = input('Введите специальность:')
salary = input('Введите желаемый уровень дохода:')
n = 2
i =0
response=[]
payload = {'page': 1, 'q': search_vacancy,'salary': salary, 'type': 'all'}
request = requests.get(link, params = payload)
response.append(request.text)

while request.ok and n < 6:
    payload = {'page': n, 'q': search_vacancy, 'type': 'all'}
    request = requests.get(link, params=payload)
    response.append(request.text)
    n += 1
    i +=1
for resp in response:
    soup = BeautifulSoup(resp, "html.parser")
    allNews = soup.findAll('a', class_='vacancy-card__title-link')

    for new in allNews:
        v = {new.text: "https://career.habr.com"+new.get('href')}
        vacancylink.update(v)
print(vacancylink)
