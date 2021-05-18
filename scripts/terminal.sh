#!/bin/bash

print "I told you to not ......Ok, Nothing Happened!.... Just kidding"

print "Memory information\n"
free -m
printf "Disk information\n"
df -h
 
echo "D-Day is on $DDAY"
echo "Today is $(date)"
echo "Linux version : $(uname -r)"
