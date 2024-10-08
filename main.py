import pyautogui as autoGui

autoGui.PAUSE = 1

screenWidth, screenHeight = autoGui.size()

# print(f"{screenWidth}, {screenHeight}")

# print(screenHeight*.75)

# autoGui.moveTo(screenWidth*.15, screenHeight*.7)

# print(autoGui.KEYBOARD_KEYS)

# autoGui.hotkey('win', 'r')
# autoGui.typewrite('chrome')
# autoGui.keyDown('enter')
#
# autoGui.typewrite('valor do dolar hoje')
# autoGui.keyDown('enter')
#
# autoGui._mouseMoveDrag(moveOrDrag='move',x=-1668, y=387,xOffset=0,yOffset=0,duration=1)
# autoGui.mouseDown()
# autoGui._mouseMoveDrag(moveOrDrag='move',x=-1668, y=387,xOffset=75,yOffset=0,duration=.5)
# autoGui.hotkey('ctrl','c')
# autoGui.mouseUp()
#
# autoGui.hotkey('win', 'r')
# autoGui.typewrite('notepad')
# autoGui.keyDown('enter')
# autoGui.hotkey('ctrl','v')

# autoGui.moveTo(x=-1374, y=368)
print(autoGui.position())

option = autoGui.confirm('Clique na opção desejada', buttons = ['Excel', 'Word', 'Notepad'])


if option == 'Excel':
    autoGui.hotkey('win', 'r')
    autoGui.typewrite('excel')
    autoGui.keyDown('enter')
    autoGui.keyDown('enter')
    autoGui.typewrite('Aberto o excel')



elif option == 'Word':
    autoGui.hotkey('win', 'r')
    autoGui.typewrite('winword')
    autoGui.keyDown('enter')
    autoGui.keyDown('enter')
    autoGui.typewrite('Aberto o word')

elif option == 'Notepad':
    autoGui.hotkey('win', 'r')
    autoGui.typewrite('notepad')
    autoGui.keyDown('enter')
    autoGui.typewrite('Aberto o notepad')