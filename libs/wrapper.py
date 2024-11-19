#API Wrapper for DJ-AppStore

import requests
import json
import urllib3
from libs import logs
import tarfile
import os

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
API_URL = "https://45.90.12.31:6517/"
#logs.log("[DEBUG] : API_URL : " + API_URL)
class Wallets:
    def create_wallet():
        try:
            x = requests.get(url=API_URL + 'wallet/add',verify=False)
            if x.status_code != 200:
                return False
            return x.json()["id"]
        except Exception as e:
            logs.error("Can't create wallet : " + str(e))
            return False
class Apps:
    def lists_app():
        try:
            x = requests.get(url=API_URL + 'get/windows',verify=False)
            if x.status_code != 200:
                return False
            return x.json()
        except Exception as e:
            logs.error("Can't get apps list : " + str(e))
            return False
    def download(app_id,wallet):
        try:
            x = requests.get(url=API_URL + f'/buy/windows/{app_id}?wallet={wallet}',verify=False)
            if x.status_code != 200:
                logs.error("Can't download app do you have enough coins ? [STATUS : " + str(x.status_code) + "]")
                return False
            if not os.path.exists('data/apps'):
                os.mkdir('data/apps')
            with open(f'data/apps/{app_id}.exe', 'wb') as f:
                f.write(x.content)
            #create a alias to run the app (on windows)E
            
            print("Saved into : data/apps/" + app_id + ".exe")
            if os.name == 'nt':
                os.system(f'start data/apps/{app_id}.exe')
            else:
                os.system(f'cd {EXE_PATH} && ./data/apps/{app_id}.exe')
            return True

        except Exception as e:
            logs.error("Can't download app : " + str(e))
            return False