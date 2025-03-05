import random
import time

num= random.randint(1,4)
time.sleep(2)
thais=1
guigas=2
tata=3
gui=4

print(num)
if num == thais:
    print('parabens é a \033[31m thais\033[m')
elif num == guigas:
    print('parabens é o \033[31m guigas\033[m')
elif num == tata:
    print('parabens é a \033[31m tata\033[m')
elif num == gui:
    print('parabens é o \033[31m gui\033[m')
    