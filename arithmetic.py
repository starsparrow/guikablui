#!/usr/bin/python3

from PyQt5.QtCore import QDateTime, Qt

now = QDateTime.currentDateTime()

print("Today:", now.toString(Qt.ISODate))
print("Adding 12 days: {}".format(now.addDays(12).toString(Qt.ISODate)))
print("Subtracting 22 days: {}".format(now.addDays(-22).toString(Qt.ISODate)))

print("Adding 50 seconds: {}".format(now.addSecs(50).toString(Qt.ISODate)))
print("Adding 3 months: {}".format(now.addMonths(3).toString(Qt.ISODate)))
print("Adding 12 years: {}".format(now.addYears(12).toString(Qt.ISODate)))

