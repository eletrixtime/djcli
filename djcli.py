''''
DJ-AppStore CLI (Command Line Interface)

Made by EletrixTime
Github : https://github.com/EletrixTime/djcli
Under the CC BY 4.0 License
'''

from libs.checker import *
# Imports
from libs.wrapper import *
import json
import os
import time
import sys

import colorama

# ------------------------------------------------------------------------------
print("========================================================================")
print("DJ-AppStore CLI (Command Line Interface)")
print("Made by EletrixTime")
print("========================================================================")
class Utils:
    def check_config():
        global wallet
        if os.path.exists('config.json'):
            with open('config.json', 'r') as f:
                config = json.loads(f.read())
                wallet = config['wallet']
            return True
        else:
            print('Making config json')
            with open('data/config-template.json', 'r') as f:
                templateconfig = f.read()
                templateconfig = json.loads(templateconfig)
                with open('config.json', 'w') as f:
                    wallet_id = input('Enter your wallet ID (type nothing for creating wallet): ')
                    if wallet_id == '':
                        wallet_id = Wallets.create_wallet()
                    templateconfig['wallet'] = wallet_id

                    f.write(json.dumps(templateconfig))
            raise SystemExit
    def help():
        print("Command List:")
        print("\n")
        print("help : Display this help")
        print("list : List all apps")
        print("download <app_id> : Download an app")
        print("wallet : Get Wallet Info")
        print("Version : 1.0")
Utils.check_config()

try:
    sys.argv[1]
except:
    Utils.help()

if sys.argv[1] == 'help':
    Utils.help()
elif sys.argv[1] == 'list':
    print("Listing apps...")
    x = Apps.lists_app()
    
    if x == False:
        print("Error: Can't get apps list")
    for app in x:
        
        print(f'- ID : {app["id"]} | Name : {app["name"]} | Price : {app["price"]} | Views : {app["visits"]} | Version : {app["version"]}')
elif sys.argv[1] == 'download':
    if len(sys.argv) < 3:
        print("Error: No app ID")
        Utils.help()
    else:
        app_id = sys.argv[2]
        print(f'Downloading app {app_id}...')
        Apps.download(app_id,wallet)
elif sys.argv[1] == 'wallet':
    print(f'Wallet ID : {wallet}')
else:
    Utils.help()