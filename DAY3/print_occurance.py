def print_occurrence(s):
    freq = {}
    for ch in s:
        freq[ch] = freq.get(ch, 0) + 1
    result = ""
    for ch in sorted(freq.keys()):
        result += ch + str(freq[ch])
    return result

s = input("Enter a string: ")
print(print_occurrence(s))
