import pyautogui
import webbrowser

url = 'https://www.google.com'
webbrowser.open_new(url)




#for i in range(10):
#    pyautogui.moveTo(100, 100, duration=0.25)
#    pyautogui.moveTo(200, 100, duration=0.25)
#    pyautogui.moveTo(200, 200, duration=0.25)
#    pyautogui.moveTo(100, 200, duration=0.25)

pyautogui.moveTo(500, 50 , duration=0.25)
pyautogui.leftClick(x=500, y=50)
pyautogui.typewrite(' youtube.com\n', interval=0.05)

pyautogui.alert('Esta hecho!')

