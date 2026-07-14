#Power Function

name = input("Enter your name: ")
age = int(input("Enter your age: "))
height = float(input("Enter your height(cm): "))
power = int(input("Enter the power level(1-10): "))
money = float(input("Enter the amout of Starter Pack Dollar: "))

print("---ผลการผระเมินพลัง---")

if power + money <= 50:
    print("ไม่ผ่านนะจ๊ะ ถ้าลงสนามเสร็จแน่ เสร็จอนันเปื้อเสื้ออนันเป็ด")
elif power + money > 50 and power + money <= 100:
    print("ผ่านนะจ๊ะ แต่ต้องระวังตัวหน่อยนะ")
    print(f"สวัสดี {name} อายุ {age} ปี สูง {height} เซนติเมตร พลังของคุณคือ {power} และคุณมีเงิน {money} Starter Pack Dollar ตำแหน่งคุณคือ เบ๊ ของพี่ปลื้ม ")
elif power + money > 100 and power + money <= 500:
    print("ผ่านนะจ๊ะ")
    print(f"สวัสดี {name} อายุ {age} ปี สูง {height} เซนติเมตร พลังของคุณคือ {power} และคุณมีเงิน {money} Starter Pack Dollar ตำแหน่งคุณคือ ลูกน้องของพี่ปลื้ม")
elif power + money > 500 and power + money <= 1000:
    print("ผ่านนะจ๊ะ")
    print(f"สวัสดี {name} อายุ {age} ปี สูง {height} เซนติเมตร พลังของคุณคือ {power} และคุณมีเงิน {money} Starter Pack Dollar ตำแหน่งคุณคือ คนสนิทพี่ปลื้ม")
else:
    print("ผ่านนะจ๊ะ")
    print(f"สวัสดี {name} อายุ {age} ปี สูง {height} เซนติเมตร พลังของคุณคือ {power} และคุณมีเงิน {money} Starter Pack Dollar พี่ปลื้มประธานค่าย Starter Pack")
