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
data = []

# Function to onfirming the existence of 'admins.json' which stores the admin
# data for persistent list:
def readList(file):
    if os.path.isfile(file) == True:
        with open(file, 'r') as f:
            data = json.load(f)
            return data

# Function to save the list to 'admins.json':
def saveList(file, data):
    with open(file, 'w') as f:
        json.dump(data, f, sort_keys=True, indent=4)

# Created lists for each role within each day:
def addKeys():
    for days in week.keys():
        keys = {'new' : [], 'ongo' : [], 'hand' : [], 'chat' : [] , 'shad' : []}
        week[days]=keys

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
def sortAdmins():
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

admins = readList('admins.json')
addKeys()
sortAdmins()
saveList('weekPool.json', week)

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
