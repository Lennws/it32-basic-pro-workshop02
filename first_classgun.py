#ทำภาระกิจลับขายปืนโหด

quantity = int(input("กี่กระบอก "))
cost_price = int(input("กระบอกละกี่บาท "))
sell_price = float(input("ขายเท่าไหร่ "))
team_members = int(input("ไปทำภาระกิจกี่คน "))

all_price = quantity * cost_price
total_price = quantity * sell_price
profit = total_price - all_price
boss = profit * 20/100
gege = (profit - boss) / 3


print(f"ต้นทุนทั้งหมด , {all_price} บาท")
print(f"รายรับทั้งหมด , {total_price} บาท")
print(f"กำไรสุทธิ , {profit} บาท")
print(f"จำนวนเงินที่หักไปให้บอส , {boss} บาท")
print(f"มีลูกน้องเข้าร่วมปฏิบัติการนี้ {team_members} คน และจะได้รับคนละ {gege} บาท")