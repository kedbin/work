import requests

with requests.Session() as s:
    r = s.get('https://raw.githubusercontent.com/kedbin/work/main/custom.xml')
data = r.text
x = 1
loop = int(input('How many tenants do you want to import? : '))
for i in range(0,loop):
    if x == 1:
        firstname = input('Tenant\'s firstname : ')
        lastname = input('Tenant\'s lastname : ')
        cardnumber = input('Tenant\'s cardnumber : ')
        begindata= data.replace('fsn1',firstname)
        begindata= begindata.replace('lsn1', lastname)
        begindata= begindata.replace('230897',cardnumber)
        begindata = begindata.replace('</CrossFire>', '')
        x +=1
    elif x == loop :
        firstname = input('Tenant\'s firstname : ')
        lastname = input('Tenant\'s lastname : ')
        cardnumber = input('Tenant\'s cardnumber : ')
        enddata = data[142::].replace('fsn1',firstname)
        enddata = enddata.replace('lsn1',lastname)
        enddata = enddata.replace('230897',cardnumber)
    else:
        firstname = input('Tenant\'s firstname : ')
        lastname = input('Tenant\'s lastname : ')
        cardnumber = input('Tenant\'s cardnumber : ')
        middledata = data[142::].replace('fsn1',firstname)
        middledata = middledata.replace('lsn1', lastname)
        middledata = middledata.replace('230897',cardnumber)
        middledata = middledata.replace('</CrossFire>', '')
        x +=1
newimport = begindata + middledata + enddata
print(newimport)
    