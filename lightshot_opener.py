import random
import string
import webbrowser
for i in range(5):

    a = string.ascii_lowercase
    a1 = ( ''.join(random.choice(a) for i in range(2)))
 
    b = string.digits
    b1 = ( ''.join(random.choice(b) for i in range(4)))
 
    url = "https://prnt.sc/"
 
    link = url+a1+b1
    webbrowser.open(link)
