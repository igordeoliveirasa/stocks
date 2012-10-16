import sys


while True:
    max_value = float(raw_input("Enter the max stock value: "))
    print "You must sell when the value reaches: %.2f" %  (max_value - (max_value * 0.15))