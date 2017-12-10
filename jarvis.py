import requests

if __name__=="__main__":
    res=requests.get("http://google.com")
    print(res.text)
