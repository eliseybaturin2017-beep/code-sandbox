import os
import shutil
import time
import random
left=0
top=0
x=1
y=1

# эта функция работает так что расставить кубы рядом не получится
def cube(x, y, l, t, s):
    cols, _ = shutil.get_terminal_size()
    if x > cols or l > cols:
        print(f"\033[91mОшибка: ширина {x + l} превышает ширину терминала! ({cols})\033[91m")
        return
    if y <= 0:
        print(f'\033[91mОшибка: высота {y} невозможно!\033[91m')
        return
    s1 =' ' * l + s * x + '\n'
    print('\n' * t + s1 * y)

def _clear_terminal():
    # Определяем операционную систему
    os.system('cls' if os.name == 'nt' else 'clear')

def animateRight(posishon=-1):
    global left
    global top
    global y
    global x

    _clear_terminal()
    left += posishon
    cube(x, y, left, top, '.')
    time.sleep(0.2)
    _clear_terminal()

def animateUp(posishon=-1):
    global left
    global top
    global y
    global x

    _clear_terminal()
    top += posishon
    cube(x, y, left, top, '.')
    time.sleep(0.2)
    _clear_terminal()

def animateYDecrease(posishon=-1):
    global left
    global top
    global y
    global x

    _clear_terminal()
    y += posishon
    cube(x, y, left, top, '.')
    time.sleep(0.2)
    _clear_terminal()

def animateXDecrease(posishon=-1):
    global left
    global top
    global y
    global x

    _clear_terminal()
    x += posishon
    cube(x, y, left, top, '.')
    time.sleep(0.2)
    _clear_terminal()

def animateYUp(posishon=1):
    global left
    global top
    global y
    global x

    _clear_terminal()
    y += posishon
    cube(x, y, left, top, '.')
    time.sleep(0.2)
    _clear_terminal()

def animateXUp(posishon=1):
    global left
    global top
    global y
    global x

    _clear_terminal()
    x += posishon
    cube(x, y, left, top, '.')
    time.sleep(0.2)
    _clear_terminal()

def animateZoomDecrease():
    animateXDecrease()
    animateYDecrease()

def animateZoomUp():
    animateXUp()
    animateYUp()

def animateLeft(posishon=1):
    global left
    global top
    global y
    global x

    _clear_terminal()
    left += posishon
    cube(x, y, left, top, '.')
    time.sleep(0.2)
    _clear_terminal()

def animateTop(posishon=1):
    global left
    global top
    global y
    global x

    _clear_terminal()
    top += posishon
    cube(x, y, left, top, '.')
    time.sleep(0.2)
    _clear_terminal()

def animateRotateMoveV1(R):
    for i in range(R):
        for i1 in range(20):
            animateLeft()
        for i2 in range(10):
            animateTop()
        for i3 in range(20):
            animateRight()
        for i4 in range(10):
            animateUp()

def animateRotateMoveV2():
    for i1 in range(20):
        animateLeft()
    for i2 in range(10):
        animateTop()
    for i3 in range(20):
        animateRight()
    for i4 in range(10):
        animateUp()

def animateRollingV1(R):
    for i in range(R):
        for i1 in range(20):
            animateLeft()
            animateTop()
        for i2 in range(30):
            animateRight()
        for i3 in range(20):
            animateUp()
        for i4 in range(10):
            animateLeft()

def animateRollingV2():
    for i1 in range(20):
        animateLeft()
        animateTop()
    for i2 in range(30):
        animateRight()
    for i3 in range(20):
        animateUp()
    for i4 in range(10):
        animateLeft()
def animatePulseZoomV1(R):
    for i in range(R):
        for i1 in range(6):
            animateZoomUp()
        for i2 in range(6):
            animateZoomDecrease()

def animatePulseZoomV2():
    for i1 in range(6):
        animateZoomUp()
    for i2 in range(6):
        animateZoomDecrease()
def animateSupris(Supris):
    superSupris = ['100 gold', '150 HP']
    NotOrdinarySupris = ['30 gold', '65 HP']
    OrdinarySupris = ['10 gold', '15 HP']
    animateRotateMoveV1(3)
    if Supris == 'superSupris':
        print(random.choice(superSupris))
        time.sleep(1)
    elif Supris == 'NotOrdinarySupris':
        print(random.choice(NotOrdinarySupris))
        time.sleep(1)
    elif Supris == 'OrdinarySupris':
        print(random.choice(OrdinarySupris))
        time.sleep(1)
