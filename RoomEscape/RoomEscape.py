from bangtal import *

scene1 = Scene('룸1', 'images/배경-1.png') # 장면 생성

# 문 이미지 넣고 좌표 삽입
door1 = Object('images/문-오른쪽-닫힘.png')
door1.locate(scene1, 800, 270)  # 위치 조절
door1.show()
door1.closed = True;

key = Object('images/열쇠.png')
key.setScale(0.2) # 사이즈 조절
key.locate(scene1, 600, 150)
key.show()

# 마우스 클릭 이벤트
def door1_onMouseAction(x, y, action):

    if door1.closed:
        if key.inHand(): 
            door1.setImage('images/문-오른쪽-열림.png')
            door1.closed = False
        else:
            showMessage('열쇠가 필요합니다.')
    else:
        endGame()   # 종료 함수

door1.onMouseAction = door1_onMouseAction

def key_onMouseAction(x, y, action):
    key.pick()

key.onMouseAction = key_onMouseAction


startGame(scene1)