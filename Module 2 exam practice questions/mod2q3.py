# Take five subjects assign marks for each and every subjects. Find out the total marks and percentage. [take user input]
math = int (input ("Math marks out of 100 : "))
bengali = int (input ("Bengali marks out of 100 : "))
english = int (input ("English marks out of 100 : "))
computer = int (input ("Computer marks out of 100 : "))
lifescience = int (input ("Life Science marks out of 100 : "))
percentage = ((math + bengali + english + computer + lifescience) * 100) / 500
print (percentage,"%")