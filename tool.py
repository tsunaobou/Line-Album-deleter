#必ずLINEPC版の画面がフルスクリーンかつアルバムタブの状態で行うこと。

import pyautogui
import time
import pyscreeze

num = int(input("アルバム数を入力せよ"))

time.sleep(3) #待機時間

for i in range(1,num+1):
    a = pyautogui.moveTo(1276,457) #アルバム編集ボタンへ移動
    pyautogui.click(a) #クリック

    b = pyautogui.moveTo(1338,547) #アルバム削除ボタンへ移動
    pyautogui.click(b) #クリック

    c = pyautogui.moveTo(900,572) #そこへ移動
    pyautogui.click(c) #クリック

    time.sleep(2) #画像が削除されるまでの間待つ