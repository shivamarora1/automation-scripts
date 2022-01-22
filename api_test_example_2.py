import requests

def test_get_pub_games():
    url = "https://pub.gamezop.com/v4/games"

    # required query params
    pubId ="rJ49y5XJx"
    lang= "en"

    params={"id":pubId,"lang":lang}
    headers = {}

    response = requests.get(url=url,params=params)
    if response.status_code != 200:
        print("expected %d but got %d"%(200,response.status_code))
        return

    resposeJSON = response.json()

    # case 1: check if key exists in result array?
    keyName = 'games'
    if not keyName in resposeJSON:
        print("key %s not exists in response"%(keyName))
        return

    # case 2: check games array has non zero values?
    if len(resposeJSON[keyName])==0:
        print("games array has no values")
        return

    # case 3: check if games array has n number of games?
    gamesRequired = 100
    if len(resposeJSON[keyName])<gamesRequired:
        print("games array does not have %d games info"%(gamesRequired))
        return

    print("All cases passed")

test_get_pub_games()