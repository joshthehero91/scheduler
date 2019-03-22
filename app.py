#!/usr/bin/python3
# Written by joshthehero91

# Importing modules:
import os
import sys
import json

# Creating empty dictionary:
admins = {}
week = {
        'sun': {},
        'mon': {},
        'tue': {},
        'wed': {},
        'thu': {},
        'fri': {},
        'sat': {},
       }

# Function to onfirming the existence of 'admins.json' which stores the admin
# data for persistent list:
def readList():
    if os.path.isfile('admins.json') == True:
        with open('admins.json', 'r') as f:
            admins = json.load(f)
            return admins

# Function to save the list to 'admins.json':
def saveList():
    with open('admins.json', 'w') as f:
        json.dump(admins, f, sort_keys=True, indent=4)

# Function to create the lists to hold the avaible admins:
def addKeys():
    for days in week.keys():
        keys = {'new' : set([]), 'ongo' : set([]), 'hand' : set([]), 'chat' : set([]) , 'shad' : set([])}
        week[days]=keys

# Function to add the admins to the list of avaible admins based on roles:
def addList(adminName, days, key):
    weekdays = week[days][key]
    add =  weekdays.add(adminName)
    if 'n' in roles:
        add
    if 'o' in roles:
        add
    if 'h' in roles:
        add
    if 'c' in roles:
        add
    if 's' in roles:
        add

# Function to add the admins to the list of avaible admins based on shift:
def setShift(shift, roles, adminName):
    for days, v in week.items():
        for key, v in week[days].items():
            weekdays = week[days][key]
            addAdmin = addList(adminName, days, key)
            if '1' in shift:
                addAdmin
            if '2' in shift:
                addAdmin
            if '3' in shift:
                addAdmin
            if '4' in shift:
                addAdmin
            if '5' in shift:
                addAdmin
            if '6' in shift:
                addAdmin
            if '7' in shift:
                addAdmin

# Function to sort admins into availibility:
def sortAdmins(roles):
    for k, v in admins.items():
        adminName = k
        shift = v['shift']
        roles = v['roles']
        setShift(shift, roles, adminName)

admins = readList()
addKeys()
sortAdmins()

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
