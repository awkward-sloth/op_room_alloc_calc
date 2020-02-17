#!/usr/bin/env python3


class Utils:
    def merged_cell_value(self, sheet, column, row, direction):
        while sheet(column, row).value is None:
            if direction.lower == 'vertical' or 'v':
                row -= 1
            elif direction.lower == 'horisontal' or 'h':
                column -= 1
        return sheet(column, row).value

    def for_each_row(block):
        pass
