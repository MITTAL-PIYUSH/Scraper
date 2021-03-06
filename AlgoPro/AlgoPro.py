"""
Requirements
Needs python 3.6
"""

import requests
import sys
import os.path

def link_preperation():
    links_final = []

    with open("index.txt") as f:
        links_list_raw = (f.read().splitlines())
    for prepared_end in links_list_raw:
        links_final.append(prepared_end.replace(" ", "%20"))
    return links_final


# works for vids - if needed i can change for make fxns for other formats too
def download(url, path, iteration):
    with open(path, 'wb') as f:

        print(f"Downloaded started | File number : {iteration}")
        response = requests.get(url, stream=True)
        total = response.headers.get('content-length')

        if total is None:
            f.write(response.content)
        else:
            downloaded = 0
            total = int(total)
            for data in response.iter_content(chunk_size=max(int(total / 1000), 1024 * 1024)):
                downloaded += len(data)
                f.write(data)
                done = int(50 * downloaded / total)
                sys.stdout.write('\r[{}{}]'.format('█' * done, '.' * (50 - done)))
                sys.stdout.flush()
            print()
            print(f"File Number {iteration} downloaded!")
    sys.stdout.write('\n')


if __name__ == '__main__':
    file_number = 0
    file_input = input()
    links_list = link_preperation()
    for query in links_list:

        dwn_link = "https://edu.tuts.workers.dev/[%20Techseries.dev%20]%20-Tech%20Interview%20Pro/AlgoPro%20_" \
                   "%20Coding%20Interview%20Practice%20Sessions/" + query
        file_name = query.replace("%20", " ")
        file_path = file_input + "\\" + file_name
        file_number += 1
        if os.path.exists(file_path):
            print("Already Downloaded.. Skipped!")
            continue
        else:
            download(dwn_link, file_path, file_number)
