import requests
import bs4
url = "https://www.geeksforgeeks.org/50-common-ports-you-should-know/"
header = {
    "User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36"
}
html = requests.get(url,headers=header)
bs  = bs4.BeautifulSoup(html.text,"html.parser")
tbody_list = bs.find_all("tbody")
# print(tbody)
tr = tbody_list[0].find_all("tr")
common_port = []
count = 0
for _ in range(len(tr)):
    if(tr[_].th.text =="6665-6669"):
        continue
    common_port.append(tr[_].th.text)
if __name__ == "__main__":
    print(common_port)
# print(bs.html.title.text)