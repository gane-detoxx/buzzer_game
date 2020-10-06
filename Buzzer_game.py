from gpiozero import LED,Button
from time import sleep,time
from random import randrange
player1,player2=0,0
b1=Button(2)
b2=Button(3)
def blink(x):
    l = LED(x)
    l.on()
    sleep(0.2)
    l.off()
    sleep(0.2)
def time_loop(x):
    i=time()
    while True:
        blink(x)
        j=time()
        if j-i>=2:
            break
    
while True:
    a=randrange(1,11)
    time1,time2=0,0
    while True:    
        sleep(a)
        while True:
            blink(17)
            if b1.is_pressed:
                player1+=1
                time_loop(22)
                break
            if b2.is_pressed:
                player2+=1
                time_loop(27)
                break
        break

    x=int(input("Wanna Continue..?(1/0):"))
    if not x:
        break
print("Player 1\t\tPlayer 2")
print(player1,"\t\t",player2)