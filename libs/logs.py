import colorama

def log(text):
    print(colorama.Fore.GREEN + text + colorama.Fore.RESET)
def error(text):
    print(colorama.Fore.RED + text + colorama.Fore.RESET)