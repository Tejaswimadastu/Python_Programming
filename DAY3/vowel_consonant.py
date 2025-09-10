def vowels_consonants(str):
    vowels="aeiouAEIOU"
    v=c=0
    for ch in str:
        if ch.isalpha():
            if ch in vowels:
                v=v+1
            else:
                c=c+1
    return v,c
s = input("Enter a string: ")
v, c = vowels_consonants(s)

print("Vowels:", v)
print("Consonants:", c)