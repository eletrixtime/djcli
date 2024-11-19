# Librarie checker
import os
with open('requirements.txt', 'r') as f:
    requirements = f.read().splitlines()
    for requirement in requirements:
        try:
            exec(f"import {requirement}")
        except ModuleNotFoundError:
            print(f"Error: Missing library {requirement}")
            if os.name == 'nt':
                os.system('pip install ' + requirement)
            else:
                os.system('pip3 install ' + requirement)
            exit()