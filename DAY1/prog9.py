cno=int(input("Enter consumer number "))
cname=str(input("Enter consumer name "))
pread=int(input("Enter present month reading "))
lread=int(input("Enter last month reading "))
units=lread-pread
print("Consumer number ",cno)
print("Consumer name ",cname)
print("Present reading ",pread)
print("Last reading ",lread)
print("Units ",units)
current_bill=3.80*units
print("Current bill ",current_bill)