from bangtal import *

# 룸1
scene1 = Scene('교수실', 'images/배경-1.png') # 장면 생성

# 책장 펼친책 문 문옆쪽지 금고 금고키패드 금고쪽지 화분 화분뒤쪽지 노트북 전원버튼 

# 문 이미지 넣고 좌표 삽입
bookshelf = Object('images/책장.png')
bookshelf.setScale(0.7)
bookshelf.locate(scene1, 1000, 150)
bookshelf.show()

door1 = Object('images/문-오른쪽-닫힘.png')
door1.locate(scene1, 800, 270)  # 위치 조절
door1.show()

doorMemo = Object('images/펼친쪽지.png')
doorMemo.setScale(0.02)
doorMemo.locate(scene1, 750, 470)
doorMemo.show()

safe = Object('images/금고.png')
safe.setScale(0.25)
safe.locate(scene1, 660, 260)
safe.show()

safeMemo = Object('images/금고쪽지.png')
safeMemo.setScale(0.05)
safeMemo.locate(scene1, 690, 360)
safeMemo.show()

safepad = Object('images/키패드.png')
safepad.locate(scene1, 760, 330)
safepad.show()

memo1 = Object('images/쪽지.png')
memo1.setScale(0.15) # 사이즈 조절
memo1.locate(scene1, 580, 145)
memo1.show()

flowerpot = Object('images/화분.png')
flowerpot.locate(scene1, 550, 150)
flowerpot.show()

com = Object('images/컴퓨터.png')
com.setScale(0.8)
com.locate(scene1, 150, 200)
com.show()

comBtn = Object('images/전원버튼.png')
comBtn.setScale(0.08)
comBtn.locate(scene1, 290, 255)
comBtn.show()

openbook = Object('images/펼친책.png')
openbook.setScale(0.5)
openbook.locate(scene1, 300, 50)
#openbook.show()

proMemo = Object('images/교수쪽지.png')
proMemo.setScale(0.3)
proMemo.locate(scene1, 320, 100)
#proMemo.show()

wallMemo = Object('images/벽쪽지.png')
wallMemo.setScale(0.3)
wallMemo.locate(scene1, 320, 100)
#proMemo.show()

potMemo = Object('images/힌트쪽지.png')
potMemo.setScale(0.3)
potMemo.locate(scene1, 320, 100)
#proMemo.show()

key = Object('images/열쇠.png')
key.setScale(0.2) # 사이즈 조절
key.locate(scene1, 700, 400)
#key.show()

# 룸2
scene2 = Scene('연구실', 'images/배경-2.png')

light = Object('images/전등.png')
light.setScale(0.2)
light.locate(scene2, 550, 450)
light.show()

door2 = Object('images/문-왼쪽-열림.png')
door2.locate(scene2, 320, 270)  # 위치 조절
door2.show()

door3 = Object('images/문-오른쪽-닫힘.png')
door3.locate(scene2, 900, 270)  # 위치 조절
door3.show()

#table = Object('images/책상.png')
#table.setScale(0.4)
#table.locate(scene2, 460, 50)
#table.show()

#ladder = Object('images/사다리.png')
#ladder.setScale(0.6)
#ladder.locate(scene2, 1100, 90)
#ladder.show()

keypad = Object('images/키패드.png')
keypad.locate(scene2, 885, 420)
keypad.show()

#password = Object('images/암호.png')
#password.setScale(0.8)
#password.locate(scene2, 350, 30)
#password.show()

# 룸3
scene3 = Scene('???', 'images/배경-2.png')

door4 = Object('images/문-왼쪽-열림.png')
door4.locate(scene2, 320, 270)  # 위치 조절
door4.show()

light = Object('images/전등.png')
light.setScale(0.2)
light.locate(scene3, 550, 450)
light.show()

memo3 = Object('images/쪽지.png')
memo3.setScale(0.15) # 사이즈 조절
memo3.locate(scene3, 600, 145)
memo3.show()


# 마우스 클릭 이벤트

# 책장
def bookshelf_onMouseAction(x, y, action):
    openbook.show()
bookshelf.onMouseAction = bookshelf_onMouseAction

def openbook_onMouseAction(x, y, action):
    openbook.hide()
openbook.onMouseAction = openbook_onMouseAction

# 금고 위 교수 쪽지
def safeMemo_onMouseAction(x, y, action):
    proMemo.show()
safeMemo.onMouseAction = safeMemo_onMouseAction

def proMemo_onMouseAction(x, y, action):
    proMemo.hide()
proMemo.onMouseAction = proMemo_onMouseAction

# 금고 키패드
def safepad_onMouseAction(x, y, action):
    showKeypad('CAB', key)
safepad.onMouseAction = safepad_onMouseAction

# 맞추면 열쇠 뜨게
def key_onKeypad():
    key.show()
    showMessage('금고가 열렸습니다.')
key.onKeypad = key_onKeypad

# 열쇠 넣기
def key_onMouseAction(x, y, action):
    key.pick()
key.onMouseAction = key_onMouseAction

# 문
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

# 벽 메모 보이기
def doorMemo_onMouseAction(x, y, action):
    wallMemo.show()
doorMemo.onMouseAction = doorMemo_onMouseAction

def wallMemo_onMouseAction(x, y, action):
    wallMemo.hide()
wallMemo.onMouseAction = wallMemo_onMouseAction

# 화분
flowerpot.moved = False
def flowerpot_onMouseAction(x, y, action):
    if flowerpot.moved == False:
        if action == MouseAction.DRAG_LEFT:
            flowerpot.locate(scene1, 450, 150)
            flowerpot.moved = True
        elif action == MouseAction.DRAG_RIGHT:
            flowerpot.locate(scene1, 650, 150)
            flowerpot.moved = True
        else:
            flowerpot.locate(scene1, 450, 200)
            flowerpot.moved = True
flowerpot.onMouseAction = flowerpot_onMouseAction

# 화분 쪽지


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

#switch.lighted = True
#def switch_onMouseAction(x, y, action):
#    switch.lighted = not switch.lighted
#    if switch.lighted:
#        scene2.setLight(1)
#        password.hide()
#    else:
#        scene2.setLight(0.2)
#        password.show()
#switch.onMouseAction = switch_onMouseAction

startGame(scene1)