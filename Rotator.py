import requests
from requests_ip_rotator import ApiGateway, EXTRA_REGIONS
from fake_useragent import UserAgent
import sys

target = "https://httpbin.org"
jumReg = 3
method = "GET"

def getReq():
    responses = [session.get(target, headers={"User-Agent": ua.random}) for _ in range(int(jumReg))]
    return responses
def postReq():
    responses = [session.post(target, headers={"User-Agent": ua.random}) for _ in range(int(jumReg))]
    return responses

if len(sys.argv) == 3:
    gateway = ApiGateway(target, regions=EXTRA_REGIONS, access_key_id=str(sys.argv[1]), access_key_secret=str(sys.argv[2]))
    gateway.start()

    session = requests.Session()
    session.mount(target, gateway)
    ua = UserAgent()

    if method == "GET":
        yuhu = getReq()
        for response in yuhu:
            print(response.status_code)
    elif method == "POST":
        yuhu = postReq()
        for response in yuhu:
            print(response.status_code)

    gateway.shutdown()
else:
    print("\nROTATOR\n\nUsage:\n  [access key id]     - Insert ur aws access key id\n  [access key secret] - Insert ur aws access key secret\n\n  python.exe Rotator.py [access key id] [access key secret]\n")