import requests

def get_trucks(index=0):
    url = ('https://ajax.googleapis.com/ajax/services/search/images?' +
       'start={0}&'.format(index) +
       'v=1.0&q=beeftruck&userip=INSERT-USER-IP')
    r = requests.get(url)
    results = r.json()
    urls = []
    for result in results['responseData']['results']:
        urls.append(result['unescapedUrl'])

    return urls

def lotsoftrucks(desiredImages=20):
    results = []
    index = 0
    while len(results) < desiredImages:
        for result in get_trucks(index=index):
            results.append(result)
        index += 4
    return results
    
