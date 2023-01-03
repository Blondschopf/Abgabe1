#!/usr/bin/env python

#the above just indicates to use python to intepret this file
# ---------------------------------------------------------------
#This mapper code will input a line of text and output <word, 1>
# 
# ---------------------------------------------------------------
import sys             #a python module with system functions for this OS
# ------------------------------------------------------------
#  this 'for loop' will set 'line' to an input line from system 
#    standard input file
# ------------------------------------------------------------
for line in sys.stdin:  
#-----------------------------------
#sys.stdin call 'sys' to read a line from standard input, 
# note that 'line' is a string object, ie variable, and it has methods that you can apply to it,
# as in the next line
# ---------------------------------
    show = ""
    channel = "-"
    viewers = "-"

    line = line.strip()  #strip is a method, ie function, associated
                         #  with string variable, it will strip 
                         #   the carriage return (by default)
    values = line.split(",")  #split line at ",", 
                         #   and return a list of keys
    
    show = values[0]
    if not values[1].isnumeric():
        channel = values[1]
    else:
        viewers = values[1]
        
    print('%s\t%s\t%s' % (show,channel,viewers))