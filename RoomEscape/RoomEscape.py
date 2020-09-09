from bangtal import *

scene1 = Scene('룸1', 'images/배경-1.png') # 장면 생성

# 문 이미지 넣고 좌표 삽입
door1 = Object('images/문-오른쪽-닫힘.png')
door1.locate(scene1, 800, 270)  # 위치 조절
door1.show()

key = Object('images/열쇠.png')
key.setScale(0.2) # 사이즈 조절
key.locate(scene1, 600, 150)
key.show()

flowerpot = Object('images/화분.png')
flowerpot.locate(scene1, 550, 150)
flowerpot.show()

# 룸2
scene2 = Scene('룸2', 'images/배경-2.png')

door2 = Object('images/문-왼쪽-열림.png')
door2.locate(scene2, 320, 270)  # 위치 조절
door2.show()

door3 = Object('images/문-오른쪽-닫힘.png')
door3.locate(scene2, 900, 270)  # 위치 조절
door3.show()

keypad = Object('images/키패드.png')
keypad.locate(scene2, 885, 420)
keypad.show()

switch = Object('images/스위치.png')
switch.locate(scene2, 880, 440)
switch.show()

password = Object('images/암호.png')
password.locate(scene2, 400, 100)

# 마우스 클릭 이벤트
door1.closed = True;
def door1_onMouseAction(x, y, action):
    if door1.closed:
        if key.inHand(): 
            door1.setImage('images/문-오른쪽-열림.png')
            door1.closed = False
        else:
            showMessage('열쇠가 필요합니다.')
    else:
        scene2.enter()
        # endGame()   # 종료 함수
door1.onMouseAction = door1_onMouseAction

def key_onMouseAction(x, y, action):
    key.pick()
key.onMouseAction = key_onMouseAction

flowerpot.moved = False
def flowerpot_onMouseAction(x, y, action):
    if flowerpot.moved == False:
        if action == MouseAction.DRAG_LEFT:
            flowerpot.locate(scene1, 450, 150)
            flowerpot.moved = True
        elif action == MouseAction.DRAG_RIGHT:
            flowerpot.locate(scene1, 650, 150)
            flowerpot.moved = True
        elif action == MouseAction.DRAG_DOWN:
            flowerpot.locate(scene1, 550, 100)
            flowerpot.moved = True
        else:
            flowerpot.locate(scene1, 450, 200)
            flowerpot.moved = True
flowerpot.onMouseAction = flowerpot_onMouseAction

def door2_onMouseAction(x, y, action):
    scene1.enter()
door2.onMouseAction = door2_onMouseAction

door3.locked = True
door3.closed = True
def door3_onMouseAction(x, y, action):
    if door3.locked:
        showMessage('문이 잠겨 있습니다.')
    elif door3.closed:
        door3.setImage('images/문-오른쪽-열림.png')
        door3.closed = False
    else:
        endGame()   # 종료 함수
door3.onMouseAction = door3_onMouseAction

def door3_onKeypad():
    door3.locked = False
    showMessage('문이 열렸습니다.')
door3.onKeypad = door3_onKeypad

def keypad_onMouseAction(x, y, action):
    showKeypad('BANGTAL', door3)
keypad.onMouseAction = keypad_onMouseAction

switch.lighted = True
def switch_onMouseAction(x, y, action):
    switch.lighted = not switch.lighted
    if switch.lighted:
        scene2.setLight(1)
        password.hide()
    else:
        scene2.setLight(0.2)
        password.show()
switch.onMouseAction = switch_onMouseAction

startGame(scene1)