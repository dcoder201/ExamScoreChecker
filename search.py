import requests
from bs4 import BeautifulSoup
from lxml import etree

url = "https://ssc.digialm.com///per/g27/pub/2207/touchstone/AssessmentQPHTMLMode1//2207O234/2207O234S31D116816/16812216849417646/9210003349_2207O234S31D116816E1.html"

response = requests.get(url)
soup = BeautifulSoup(response.content, "html.parser")

right_answer = [i.text[0] for i in soup.find_all('td', class_='rightAns')]


option = soup.find_all('td', class_='bold')
chosen_option = [option[i].text for i in range(5, len(option), 6)]

print(chosen_option)


print(f'Total no. of Questions : {len(right_answer)}')

attempted = len([i for i in chosen_option if i.isnumeric()])

print(f'No. of attempted questions: {attempted}')

un_attempted = 100 - attempted

print(f'No. of unattempted questions: {un_attempted}')

print(f'Maximum mark : {"{:.2f}".format(len(right_answer)*2)}')


right = sum([1 for i in range(len(right_answer)) if right_answer[i] == chosen_option[i]])
print(f'No. of right answers: {right}')

print(f'No. of wrong answers: {attempted-right}')

print(f'Total Marks obtained: {"{:.2f}".format( (right * 2) - ((attempted-right) * 0.50) )}')
















