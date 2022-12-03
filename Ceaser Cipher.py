pt = input("Enter your Plain Text: ")
key = int(input("Enter the Key: "))
ans = ""
for ch in pt:
    if ch.isalpha():
        ans+=chr(ord(ch)+key)
    elif ch.isdigit():
        ans+=str(int(ch)+key)
    else:
        ans+=ch
print("The encrypted Text is:",ans)