# Learning For Loop in Python
# Print every items of the list using from loop
fruits = ["Apple","Mango","Cherry","Bananas","Orange","Chalta","Pineapple"]
for x in fruits:
    print (x)
print ("=================================================================================")
for e in "Mango Cherry":
    print (e)

print ("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
players = ["Virat Kohli","Rohit Sharma", "Joe Root", "Mustafizur Rahman", "Rashid Khan"]
country = ["India", "Australia", "England", "Bangladesh", "Afghanistan"]
for pc in players:
    for cp in country:
        print (pc,cp)