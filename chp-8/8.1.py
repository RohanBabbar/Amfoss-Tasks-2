import pyinputplus as pi
prices = {'wheat':30,"white":28,"sourdough":35,"chicken":10,"turkey":12,"ham":9,"tofu":7,"cheddar":5,"swiss":8,"mozzarella":3,"mayo":4,"mustard":6,"lettuce":8,"tomato":5}
list=[]
print("Which type of bread")
response1 = list.append(pi.inputMenu(['wheat', 'white', 'sourdough']))
# print(response)
print("which meat ")
response2 = list.append(pi.inputMenu(['chicken','turkey','ham','tofu']))
# print(go)
print("Do You want Cheese ?")
response3 = pi.inputYesNo()
# print(tell)
if response3 == "yes":
    cheese = list.append(pi.inputMenu(['cheddar','swiss','mozzarella']))
print("Do yyou want mayo ?")
extra = pi.inputYesNo()
if extra == 'yes':
    list.append('mayo')
print("Do yyou want mustard ?")
extra = pi.inputYesNo()
if extra == 'yes':
    list.append('mustard')
print("Do yyou want lettuce ?")
extra = pi.inputYesNo()
if extra == 'yes':
    list.append('lettuce')
print("Do yyou want tomato ?")
extra = pi.inputYesNo()
if extra == 'yes':
    list.append('tomato')
number = pi.inputInt('How Many Sandwiches ?', min = 1)
x = 0
for i in list:
    x += (prices[i] * number)
print("Total Cost of the sandwich is: ", x)