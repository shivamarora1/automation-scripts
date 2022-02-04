# GET request example
## 1. Install dependencies
### pip install -U requests
import requests

def test_get_request():
    # define url which we have to test
    link = 'https://httpbin.org/get'
    
    # additional headers *if required.
    hd = {'Content-Type': 'application/json' } 

    # send GET request to the url we have defined above
    resp = requests.get(url=link, headers=hd)       
    
    # validate response headers and body contents, e.g. status code.
    # case 1:
    if resp.status_code != 200:
        print('expected 200 status code got %s'%(resp.status_code))
        return

    resp_body = resp.json()
    print(resp_body)

    # case 2: verify url key of response
    if resp_body['url'] != link:
        print('expected url is not same got %s'%(link))
        return
    
    # print response full body as text
    print("all success")
    # print(resp.text)

test_get_request()   