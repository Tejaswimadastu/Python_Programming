def count_notes(n):
    count_500 = n // 500
    n = n % 500
    count_100 = n // 100
    n = n % 100
    count_50 = n // 50
    n = n % 50
    count_10 = n // 10
    n = n % 10
    if count_500 > 0:
        print(f"{count_500} x 500 notes present")
    if count_100 > 0:
        print(f"{count_100} x 100 notes present")
    if count_50 > 0:
        print(f"{count_50} x 50 notes present")
    if count_10 > 0:
        print(f"{count_10} x 10 notes present")
    if n > 0:
        print(f"Remaining amount that cannot be given in 500, 100, 50, or 10 notes: {n}")

amt = int(input("Enter amount "))
print(count_notes(amt))