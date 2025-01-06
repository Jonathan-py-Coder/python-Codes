# Creating a Dictonary
books={"name":"The hound of te Baskervilles", "author":"Sir Aurther Conan Doyle","genre":"Mystery", "year published": "1901-1902" }
# printing the Dictonary
print (books)
# writing the required dictionary value
print (books["author"])
# printing the keys 
print (books.keys())
# Printing all the values
print (books.values())
for key in books.keys():
    print(key,books[key])
if "author" in books:
    print (books["author"])
else:
    print ("thee key does not exist")
books["ratings"]="4.8 stars"
print(books)
books["genre"]="Horror"
print(books["genre"])
del(books["author"])
print(books)