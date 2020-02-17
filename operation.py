#!/usr/bin/env python3
import utils


class Operation:
    def __init__(self, weekday, department, p_st, p_ed, o_st, o_ed):
        self.weekday = weekday
        self.department = department
        self.p_st = p_st
        self.p_ed = p_ed
        self.o_st = o_st
        self.o_ed = o_ed
        self.id = department + weekday + p_ed.strftime('%H%M')


class Operations:
    def operations(self, wb):
        # creates and returns all the operations from a workbook
        result = []
        # for each worksheet in a workbook,
        for ws in wb:
            # for each rows in a worksheet,
            for row in ws:
                # create new operation.
                op = Operation()
