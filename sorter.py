#!/usr/bin/python3
# Written by joshthehero91

# Function to check the roles called by 'sortAdmin()': 
def roleCheck(roles, adminName, weekday):
    for i in roles:
        if i == 'n':
            if adminName not in weekday['new']:
                weekday['new'].append(adminName)
        if i == 'o':
            if adminName not in weekday['ongo']:
                weekday['ongo'].append(adminName)
        if i == 'h':
            if adminName not in weekday['hand']:
                weekday['hand'].append(adminName)
        if i == 'c':
            if adminName not in weekday['chat']:
                weekday['chat'].append(adminName)
        if i == 's':
            if adminName not in weekday['shad']:
                weekday['shad'].append(adminName)

# Function to sort admins into pools based on days and roles:
def sortAdmins(admins, week):
    for adminName, v in admins.items():
        shift = v['shift']
        roles = v['roles']
        for s in shift:
            if s == '1':
                weekday = week['sun']
                roleCheck(roles, adminName, weekday)
            if s == '2':
                weekday = week['mon']
                roleCheck(roles, adminName, weekday)
            if s == '3':
                weekday = week['tue']
                roleCheck(roles, adminName, weekday)
            if s == '4':
                weekday = week['wed']
                roleCheck(roles, adminName, weekday)
            if s == '5':
                weekday = week['thu']
                roleCheck(roles, adminName, weekday)
            if s == '6':
                weekday = week['fri']
                roleCheck(roles, adminName, weekday)
            if s == '7':
                weekday = week['sat']
                roleCheck(roles, adminName, weekday)
    print('')
    print('----------------------')
    print('Sun')
    print(week['sun'])
    print('')
    print('Mon')
    print(week['mon'])
    print('')
    print('Tue')
    print(week['tue'])
    print('')
    print('Wed')
    print(week['wed'])
    print('')
    print('Thu')
    print(week['thu'])
    print('')
    print('Fri')
    print(week['fri'])
    print('')
    print('Sat')
    print(week['sat'])
    print('')
