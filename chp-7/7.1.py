import re
dateRegex = re.compile(r'(\d\d)/(\d\d)/(\d\d\d\d)')
no = dateRegex.search('The Date is 29/02/2323.')
day = no.group(1)
month = no.group(2)
year = no.group(3)
if int(month) in (4,6,8,11) and int(day) in range(1,31):
    print(no.group(),";its a valid date")
elif int(month) == 2:
    if int(day) == 29 and int(year)%4==0 and (not int(year)%100==0 or int(year)%400==0):
        print(no.group(),";its a valid date")
    elif int(day) in (0,29):
            print(no.group(),";its a valid date")
    else:
        print(no.group(),";its not a valid date")