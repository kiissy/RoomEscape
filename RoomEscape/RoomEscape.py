from bangtal import *

scene1 = Scene('룸1', 'images/배경-1.png') # 장면 생성

closed1 = True
# 문 이미지 넣고 좌표 삽입
door1 = Object('images/문-오른쪽-열림.png')
door1.locate(scene1, 800, 270)
door1.show()

# 마우스 클릭 이벤트
def door1_onMouseAction(x, y, action):
    global closed1     # 전역임을 알려줘야 함
    if closed1 == True: # 문이 열린 상태에서 클릭해서 닫히면
        door1.setImage('images/문-오른쪽-닫힘.png')
        closed1 = False
    else:
        endGame()   # 종료 함수

door1.onMouseAction = door1_onMouseAction


startGame(scene1)