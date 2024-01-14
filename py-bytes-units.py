#!/bin/python3

import sys
import re
import math

def unitsSupported():
    print(f"These are the only supported units:\nBase 10: {units_10}\nBase 2: {units_2}")

def validFormat():
    print("Valid format for initial value to convert: [number][units]\n(Do not include brackets)")

def toBytesBase10(num, units):
    return num * math.pow(1000, units_10.index(units))

def toBytesBase2(num, units):
    return num * math.pow(1024, units_2.index(units))

def fromBytesBase10(num, units):
    return num / math.pow(1000, units_10.index(units))

def fromBytesBase2(num, units):
    return num / math.pow(1024, units_2.index(units))

units_10 = ["B", "KB", "MB", "GB", "TB"]
units_2 = ["B", "KiB", "MiB", "GiB", "TiB"]

if len(sys.argv) == 1:
    print("Please enter number to convert and destination units.")
    unitsSupported()
    validFormat()
    exit(1)

if (len(sys.argv) == 2):
    print("Please enter destination units.")
    unitsSupported()
    exit(1)

number_origin = sys.argv[1]
units_destination = sys.argv[2]

hide_units = sys.argv[3] == "-h" if (len(sys.argv) == 4) else False

number = float(re.search("[0-9]*\.*[0-9]*", number_origin).group())
units_origin = re.search("[A-Z]?i?B", number_origin).group()

type_origin = 1 + int(bool(re.search("i", units_origin)))
type_destination = 1 + int(bool(re.search("i", units_destination)))

try:
    if type_origin == 1:
        units_10.index(units_origin)
    else:
        units_2.index(units_origin)
except:
    print("The given origin units are invalid.")
    unitsSupported()
    exit(1)

try:
    if type_destination == 1:
        units_10.index(units_destination)
    else:
        units_2.index(units_destination)
except:
    print("The given destination units are invalid.")
    unitsSupported()
    exit(1)

bytes_converted = toBytesBase10(number, units_origin) if type_origin == 1 else toBytesBase2(number, units_origin)
result = fromBytesBase10(bytes_converted, units_destination) if type_destination == 1 else fromBytesBase2(bytes_converted, units_destination)

result = int(result) if result.is_integer() else result

print_units = "" if hide_units else units_destination

print(f"{result}{print_units}")

