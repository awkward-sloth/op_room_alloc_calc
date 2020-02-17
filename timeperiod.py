#!/usr/bin/env python3
import utils
import datetime
import operation


class Timeperiod:
    # stores data
    def __init__(self, weekday, department, st_time, ed_time):
        self.weekday = weekday
        self.department = department
        self.st_time = st_time
        self.ed_time = ed_time
        self.id = department + weekday + ed_time.strftime('%H%M')
        self.operations = []

    def total_time(self):
        # returns total time within the
        # allocated timeperiods of the operations
        result = datetime.timedelta(0)
        for op in self.operations:
            result += op.time
        return result

    def show(self):
        print(self.id)
        print('\t' + self.total_time)
        for op in self.operations:
            print('\t' + op.id + op.o_st, op.o_ed)


class Timeperiods:
    #collection of Timeperiod
    def timeperiods(self, wb):
        # creates and returns all timeperiods from a workbook
        result = []
        # for each worksheet in a workbook,
        for ws in wb:
            # for each rows in a worksheet,
            for row in ws:
                # create new timeperiod.
                tp = Timeperiod(utils.merged_cell_value(ws, 2, row, 'v'),   # wd
                                utils.merged_cell_value(ws, 3, row, 'v'),   # dept
                                ws(4, row).value,   # st_time
                                ws(5, row).value)   # ed_time
                # if the same kind of timeperiod is not on the list, append
                if result.index(tp.id) is not None:
                    result.append(tp)
        # return the result
        return result
