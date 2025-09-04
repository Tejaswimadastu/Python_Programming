def number_to_words(n):
    ones=["zero","one","two","three","four","five","six","seven","eight","nine"]
    if n==0:
        print("Zero")
        return
    words=[]
    while n>0:
        digit=n%10
        words.append(ones[digit])
        n=n//10
    print(' '.join(reversed(words)))
x=int(input("Enter a number "))
number_to_words(x)