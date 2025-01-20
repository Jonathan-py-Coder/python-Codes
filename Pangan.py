string=input("what sting to you want to check for voels? ")
vowels={"a": 0 , "e":0,"i":0,"o":0,"u":0}
for a in string:
        if a in vowels:
            vowels[a] +=1
print("the baluse in the dictionary vowels are", vowels)

str=input("enter a sentance ")
charcount ={}

for m in str:
      if  m.isalpha():
            if m in charcount:
                  charcount[m]+=1
            else:
                  charcount[m]=1
print("charcount")

number= input("enter a number ")

numcount={"0":0,"1":0,"2":0,"3":0,"4":0,"5":0,"6":0,"7":0,"8":0,"9":0, }

for s in str:
            if s in numcount:
                  numcount[m]+=1
pangram = True
for count in numcount.values():
      if count == 0:
            pangram=False
if pangram == True:
    print("enter number is a pangram number")
else:
    print("enter number is not a pangram number")

