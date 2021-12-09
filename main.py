#!/usr/bin/python
import re
def paranoyc():
    while True:
        name = str(input("Enter name: "))
        if "Stop" in (" " + name.upper() + " ") or "stop" in (" " + name.lower() + " "):
            break
        if not name.isalpha() or re.search(r'[^-a-zA-Z-а-яА-ЯёЁ]', name):
            print("Can use only latin and cyrillic symbols. Please retry!")
        else:
            while True:
                try:
                    v1 = int(input("enter number v1: "))
                except ValueError:
                    print("Can use only whole numbers. Please retry!")
                else:
                    if v1 < 0:
                        print("Can use numbers above zero. Please retry!")
                    else:
                        while True:
                            try:
                                v2 = int(input("Enter number v2: "))
                            except ValueError:
                                print("Can use only whole numbers. Please retry!")
                            else:
                                if v2 < 0:
                                    print("Can use numbers above zero. Please retry!")
                                else:
                                    while True:
                                        try:
                                            v3 = float(input("Enter number v3: "))
                                        except ValueError:
                                            print("Can use only numbers. Please retry!")
                                        else:
                                            if v3 == 0:
                                                print("Can use numbers above zero. Please retry!")
                                            else:
                                                print(f"{name}, hi!")
                                                v1 = int(f"{v1}" * 3)
                                                v2 = int(f"{v2}" * 2)
                                                v3 = float(f"{v3}")
                                                s = (v1 + v2) / v3
                                                print("Your sum = " + "%.2f" % s)
                                                break
                                    break
                        break
            break

paranoyc()
