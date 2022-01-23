# GET request example
## 1. Install dependencies
### pip install -U requests
import requests
import json

def test_get_request():
    # define url which we have to test
    url = 'https://httpbin.org/get'
    
    # additional headers *if required.
    headers = {'Content-Type': 'application/json' } 

    # send GET request to the url we have defined above
    resp = requests.get(url, headers=headers)       
    
    # validate response headers and body contents, e.g. status code.
    if resp.status_code != 200:
        print('expected 200 status code got %s'%(resp.status_code))
        return

    resp_body = resp.json()
    if resp_body['url'] != url:
        print('expected url is not same got %s'%(url))
        return
    
    # print response full body as text
    print("all success")
    print(resp.text)

test_get_request()   