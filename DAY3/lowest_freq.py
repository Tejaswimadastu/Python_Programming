def lowest_frequency_char(s):
    freq = {}
    for ch in s:
        freq[ch] = freq.get(ch, 0) + 1
    min_char = min(freq, key=freq.get)
    return min_char, freq[min_char]

s = input("Enter a string: ")
ch, count = lowest_frequency_char(s)
print(f"Lowest frequency character: '{ch}' appears {count} times")
