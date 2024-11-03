from helper_functions import prompt_help, prompt_convert_image, prompt_downsize_image, prompt_info, prompt_exit
from prompt_toolkit import prompt
import os
def clear_screen():
    if os.name == 'nt':
        _ = os.system('cls')                 
    else:
        _ = os.system('clear')

def main():
    prompt_help()
    while True:
        try:
            action = prompt("> ")
            if action.lower() == "convert":
                prompt_convert_image()
            elif action.lower() == "downsize":
                prompt_downsize_image()
            elif action.lower() == "info":
                prompt_info()
            elif action.lower() == "exit":
                print("Have a good day ^^.")
                break
            elif action.lower() == "help":
                prompt_help()
            elif action.lower() == "clear":
                clear_screen()
            else:
                print("Invalid command, run help for available commands.")
        except (KeyboardInterrupt, EOFError) :
            if prompt_exit():
                print("Have a good day ^^.")
                break
            else:
                continue

