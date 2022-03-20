# -------=imports=-------
import os, pyttsx3, keyboard, time, schedule
from datetime import *

engine = pyttsx3.init()

warning = "Внимание, в связи с текущем временем компьютер выключится через 5 минут! Что бы отменить это действие нажмите клавишу Insert, она находиться слева выше от клавиши Enter!"
warning2 = "Внимание вы отменили выключение!"

hour = input("Введите час (если это одно число введите с нулём в начале, например 00, 02): ")
minute = input("Введите минуту(ы) (если это одно число введите с нулём в начале, например 00, 02): ")
second = input("Введите секунду(ы) (если это одно число введите с нулём в начале, например 00, 02): ")

def main():

    def no():
        x = 1

        while x:

            if keyboard.is_pressed("Insert"):
                os.system("shutdown -a")
                print(warning2)
                engine.say(warning2)
                engine.runAndWait()

                x = 0


    def off():
        print(warning)
        engine.say(warning)
        engine.runAndWait()
        os.system("shutdown -s -t 300")

        no()

    schedule.every().day.at(f"{hour}:{minute}:{second}").do(off)

    while 1:

        schedule.run_pending()

if __name__ == "__main__":
    main()
