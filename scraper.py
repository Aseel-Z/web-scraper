import requests
from bs4 import BeautifulSoup
import json


def get_citations_needed_count(url):

    response = requests.get(url)
    page_contents = BeautifulSoup(response.content, 'html.parser').find_all('a', title = 'Wikipedia:Citation needed')
    return len(page_contents)



def get_citations_needed_report(url):
    response = requests.get(url)
    page_contents = BeautifulSoup(response.content, 'html.parser').find_all('a', title = 'Wikipedia:Citation needed')
    final_output = ''
    final_output_arr = []
    for tag in page_contents:
        final_output+=f'{tag.parent.parent.parent.text}\n'
        final_output_arr.append(f'paragraph: {tag.parent.parent.parent.text}')
    json_obj = json.dumps(final_output_arr)

    with open('citation-needed.json','w') as file:
        file.write(json_obj)

    return final_output
   

if __name__ == '__main__':
    url = 'https://en.wikipedia.org/wiki/History_of_Mexico'
    print(get_citations_needed_count(url))
    print(get_citations_needed_report(url))