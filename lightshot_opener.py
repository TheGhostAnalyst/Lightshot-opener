import random
import string
import webbrowser
import pyinputplus as Pyip
from pathlib import Path
from datetime import datetime

all_links = []
try:
    num_links = Pyip.inputInt("How many links do you want to generate: ")

    for i in range(num_links):
        a1 = ''.join(random.choice(string.ascii_lowercase) for _ in range(2))
        b1 = ''.join(random.choice(string.digits) for _ in range(4))
    
        link = (f"https://prnt.sc/{a1}{b1}")
        all_links.append(link)
        print(f'Link Generated: {link}')
    print('Link generated above:')
    save = Pyip.inputStr("\nDo you want to save these links to a file? (yes/no): ").strip().lower()
    if save in ['yes', 'y']:
        with open('all_links.txt', 'a') as f:
            now = datetime.now()
            timestamp = now.strftime('%Y-%m-%d %H:%M')
            f.write(f"######################################\n{timestamp}\n")
            for link in all_links:
                f.write(f"{link}\n")
        the_path = Path('all_links.txt').resolve()
        print(f'\nYour generated links have been saved in {the_path} ')
    else:
        print("Links have not been saved.")

    open_in_browser = Pyip.inputStr("Do you want to open these links in your web browser? (yes/no): ").strip().lower()
    if open_in_browser in ['yes', 'y']:
        for link in all_links:
            webbrowser.open(link)
        print("Links have been opened in your web browser.")
    else:
        print("Links have not been opened.")
except KeyboardInterrupt:
    print('\nProcess interrupted. Exiting...')
except Exception as e:
    print(f"An error occurred: {e}")
