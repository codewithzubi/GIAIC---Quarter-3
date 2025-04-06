import time  # time module ko import karna hoga
import sys   # sys module ko import karna hoga flush ke liye

# Countdown from 1 to 10
for i in range(1, 11):  # 1 se lekar 10 tak print hoga
    print(i, end=" ", flush=True)  # Har number ko space ke saath print karo aur flush karna
    time.sleep(1)  # Har number ke baad 1 second ka delay

# Jab loop complete ho jaye, tab Liftoff! print karo
print("Liftoff!")
