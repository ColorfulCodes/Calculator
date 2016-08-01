# coding: utf-8
# We will be creating a calulator that prompts the user to select a shape and calculate it's area.

from math import pi

from time import sleep

from datetime import datetime

now = datetime.now()

print "The calculator is now starting up..."

print 'Time is now: %d/%d/%d %d: %d' % (now.month, now.day, now.year, now.hour, now.month)

sleep(1)

hint = "Don't forget to include the correct units"

option = raw_input("Enter C for Circle or T for Triangle below: \n>")

option = option.upper()

if option == "C":

    radius = float(raw_input("Input a radius below please: \n> "))

    area = pi*radius**2

    print "The pie is baking..."

    sleep(1)

    print ("Area: %.2f. \n%s" % (area, hint))


elif option == "T":

    base = float(raw_input("What is the base of the triangle? > "))

    height = raw_input('What is the height of the triangle? > ')

    area = height*base/2

    print "Uni Bi Tri..."

    sleep(1)

    print ('Area is %.2f.' % (area))


else:

    print "That's not a choice bruh. Now I must exit."
