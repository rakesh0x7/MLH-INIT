import requests
from bs4 import BeautifulSoup

req1 = requests.get("https://www.polywork.com/rakesh")
soup1 = BeautifulSoup(req1.content, "html.parser")
res1 = soup1.title

print("TITLE")
print(res1.get_text())

html1 =soup1.contents
html1 = soup1.prettify("utf-8")
with open("output1.html", "w") as file:
    file.write(str(soup1))


req2 = requests.get("https://www.polywork.com/baileyluu")
soup2 = BeautifulSoup(req2.content, "html.parser")
res2 = soup2.title

print("TITLE")
print(res2.get_text())

html2 =soup2.contents
html2 = soup2.prettify("utf-8")
with open("output2.html", "w") as file:
    file.write(str(soup2))
