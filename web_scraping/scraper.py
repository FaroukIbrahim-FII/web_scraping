import requests

URL = "https://en.wikipedia.org/wiki/History_of_football_in_England"
res = requests.get(URL)

from bs4 import BeautifulSoup
soup = BeautifulSoup(res.content, 'html.parser')
results_div = soup.find('div', id="mw-content-text")
results_ul = results_div.find_all('span', class_='mw-headline')
results_p = results_div.find_all('p')
results_p.pop(0)

for i in range(11):
    results_p.pop()

results_p.pop(2)
results_p.pop()

for i in range(7):
    results_ul.pop()

all_content = []
for job in results_ul:
    i = 0
    content_dict = {'title':'', 'para':''}
    para_before_strpping = results_p[i]
    if job:
        title = job.get_text().strip()
        content_dict['title'] = title
        para = para_before_strpping.get_text().strip()
        content_dict['para'] = para
        all_content.append(content_dict)
    i += 1

def get_citations_needed_count(url):

    res = requests.get(url)       
    soup = BeautifulSoup(res.text,"html.parser")
    result = soup.find_all("a", title="Wikipedia:Citation needed") 
    return len(result)

def get_citations_needed_report(url):
    citation_list= []
    res = requests.get(url)       
    soup = BeautifulSoup(res.text,"html.parser")
    results = soup.find_all("a", title="Wikipedia:Citation needed")

    for result in results:
        citation_list.append(result.parent.parent.parent.text)

    final = '\n'.join(citation_list)
    return final

wikipedia_url = "https://en.wikipedia.org/wiki/History_of_Mexico"
print(get_citations_needed_count(wikipedia_url))
print(get_citations_needed_report(wikipedia_url))

# import json
# with open('all_content.json', 'w') as f:
#     content = json.dumps(all_content)
#     f.write(content)