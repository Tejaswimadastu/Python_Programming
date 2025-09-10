def word_count(s):
    words=s.split()
    return len(words)
x=str(input("Enter string "))
print("Number of words ",word_count(x))