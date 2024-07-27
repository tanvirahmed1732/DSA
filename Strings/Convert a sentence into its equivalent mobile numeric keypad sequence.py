strr = ["2", "22", "222","3", "33", "333","4", "44", "444","5", "55", "555",
       "6", "66", "666","7", "77", "777", "7777","8", "88", "888","9", "99", "999", "9999"]
s=input("Enter the string(note: only in capital form): ")
ans=str()
for i in s:
    if i == " ": #if there is any space in the string, we need to press 0 once
        ans+="0"
    else:
        ans+=strr[ord(i)-ord("A")] # I am using asscii value here to access the corresponding keys from the strr list.
print(ans)