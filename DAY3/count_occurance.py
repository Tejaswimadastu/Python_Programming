def find_occurance(s,ch):
    positions=[]
    for i in range(len(s)):
        if s[i]==ch:
            positions.append(i)
    return positions
s=input("Enter a string ")
ch=input("Enter a character ")
positions=find_occurance(s,ch)
if positions:
    print("Total occurrences:", len(positions))
else:
    print(f"Character '{ch}' not found in the string.")