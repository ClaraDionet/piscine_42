#!/usr/bin/python3

"""
    opensearch.py
    MediaWiki API Demos
    Demo of `Opensearch` module: Search the wiki and obtain
	results in an OpenSearch (http://www.opensearch.org) format
    MIT License
"""
import sys
import requests
import dewiki

def get_data(search):
    S = requests.Session()
    URL = "https://fr.wikipedia.org/w/api.php"

    PARAMS = {
        "action": "query",
        "titles": search,
        "prop": "revisions",
        "rvprop": "content",
        "rvsection": "0",
        "format": "json"
    }

    R = S.get(url=URL, params=PARAMS)
    DATA = R.json()

    # PAGES = DATA["query"]["pages"]

    # for k, v in PAGES.items():
    #     for cat in v['categories']:
    #         print(cat["title"])

    # r = s.get(url=url, params=params)
    # data = r.json()
    txt = DATA.get('query')

    return dewiki.from_string(txt)

if __name__ == '__main__' :
    print(get_data(sys.argv[1:]))




#!/usr/bin/python3
# coding : utf8

# import sys
# import requests
# import json
# import dewiki

# def write_in_file(req, txt):
#     print(txt)
    # filename = req.replace(" ", "_") + ".wiki"
    # f = open(filename, "w")
    # f.write(txt)
    # f.close()

# def process_request(req):
#     url = 'https://fr.wikipedia.org/w/api.php'
#     payload = {'action':'query', 'titles':req, 'prop':'revisions','rvprop':'content','format':'json'}
#     r = requests.get(url,params=payload)
#     #print("debug url = ", r.url)
#     if r.status_code != 200:
#         print("Erreur HTTP, code ", str(r.status_code))
#         exit(1)
#     res = r.json()
#     #print("debug : res=", res)
#     if res.get('query'):
#         #print('debug : query trouve')
#         query = res['query']
#         if query.get('pages'):
#             pages = query['pages']
#             #print('debug : pages trouve')
#             txt = ""
#             for pageid in pages:
#                 page = pages[pageid]
#                 if page.get('revisions'):
#                     revisions = page['revisions']
#                     #print('debug : revisions trouve ',revisions)
#                     if revisions[0].get('*'):
#                         #print('debug : contentu trouve ',revisions[0]['*'] )
#                         txt += revisions[0]['*'] + "\n" 
                
#                     txt = dewiki.from_string(txt)
#             return txt
#             # write_in_file(req, txt)

# def usage():
#     print("Usage : python3 request_wikipedia.py chaine_de_recherche")

# if __name__ == '__main__':
#     if len(sys.argv) == 2:
#         print(process_request(sys.argv[1]))
#     else :
#         usage()