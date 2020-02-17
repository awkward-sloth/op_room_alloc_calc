#!/usr/bin/env python3
import openpyxl
import timeperiod
import operation

file_path = '/home/sh/Documents/operations.xlsx'
wb = openpyxl.load_workbook(file_path)

# get all timeperiods
tp = timeperiod.timepereods(wb)
# get all operations
operations = operation.operations(wb)
# associate operations to timeperiods
for tp in timeperiod.timeperiods(wb):
    for op in operation.operations(wb):
        if tp.id == op.id:
            tp.operations.append(op)

# show timeperiods
for tp in timeperiod.timeperiods(wb):
    tp.show()
#   id, dept, weekday, p_st, p_ed
#   show operations
#     id, dept, o_st, o_ed
