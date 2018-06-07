#!/usr/bin/python3

from PyQt5.QtCore import QDate

xmas1 = QDate(2017, 12, 24)
xmas2 = QDate(2018, 12, 24)

now = QDate.currentDate()

dayspassed = xmas1.daysTo(now)
print("{} days have passed since last XMas".format(dayspassed))

nofdays = now.daysTo(xmas2)
print("There are {} days until next XMas".format(nofdays))
