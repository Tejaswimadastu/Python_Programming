# Calculate current bill based on given units
def current_bill(last, present):
    units = present - last
    if units <= 50:
        bill = units * 3.80
    elif units <= 100:
        bill = (50 * 3.80) + (units - 50) * 4.20
    elif units <= 200:
        bill = (50 * 3.80) + (50 * 4.20) + (units - 100) * 5.10
    elif units <= 300:
        bill = (50 * 3.80) + (50 * 4.20) + (100 * 5.10) + (units - 200) * 6.30
    else:
        bill = (50 * 3.80) + (50 * 4.20) + (100 * 5.10) + (100 * 6.30) + (units - 300) * 7.50
    return bill

last = int(input("Enter last month units: "))
present = int(input("Enter present units: "))
print("Current bill amount: ₹{:.2f}".format(current_bill(last, present)))