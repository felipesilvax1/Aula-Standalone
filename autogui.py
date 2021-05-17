#/usr/bin/python
from os import terminal_size
from Xlib.X import DisableScreenInterval, KBBellDuration
import pyautogui
import time
from time import sleep
#nas colunas superiores importa as biblitotecas
#e na ultima chama da biblioteca time a função sleep
print(f'tira las patitas del tecladito!')
# move mouse pra esse lugar ai ó
pyautogui.moveTo(22,5)
# dá um clique nesse lugar ai
pyautogui.click(22,5,duration=1)
# digita com tempo de meio sec "teams"
pyautogui.typewrite("teams",interval=0.5)
# pressiona a tecla enter
pyautogui.press('enter',interval=1)
#move o mouse até tecla equipes
pyautogui.moveTo(31,209)
#aguarda 2 sec
sleep(3)
#dá dois cliques em equipes
pyautogui.doubleClick(31,209,duration=1)
#aguarda meio sec
sleep(0.5)
#moveparaocanaldequimica
#pyautogui.moveTo(813,271)
#pyautogui.click(813,271,duration=2)