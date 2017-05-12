# coding: utf-8
#
# Copyright © 2017 .
#
# This file is part of gitinspector.
#
# gitinspector is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# gitinspector is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with gitinspector. If not, see <http://www.gnu.org/licenses/>.
# import xlwt
#
# __excel_book__ = None
# __data_sheet__ = None
#
# def get_excel_book():
#     global __excel_book__
#     if __excel_book__ == None:
#         __excel_book__ = xlwt.Workbook()
#     return __excel_book__
#
# def get_data_sheet():
#     global __data_sheet__
#     if __data_sheet__ == None:
#         __data_sheet__ =  get_excel_book().add_sheet("Data")
#     return __data_sheet__
import xlsxwriter

__excel_book__ = None
__code_type_data_sheet__ = None
__data_sheet__ = None

def get_excel_book():
     global __excel_book__
     if __excel_book__ == None:
         __excel_book__ = xlsxwriter.Workbook("test.xlsx")
     return __excel_book__

def get_data_sheet():
     global __data_sheet__
     if __data_sheet__ == None:
         __data_sheet__ =  get_excel_book().add_worksheet("Changes by month")
     return __data_sheet__


def get_code_type_data_sheet():
    global __code_type_data_sheet__
    if __code_type_data_sheet__ == None:
        __code_type_data_sheet__ = get_excel_book().add_worksheet("Authors by code")
    return __code_type_data_sheet__

def add_chart(sheet,series):
    # Create a new chart object. In this case an embedded chart.
    chart1 = get_excel_book().add_chart({'type': 'column', 'subtype': 'stacked'})
    for serie in series:
        chart1.add_series({
            'name':       serie.name,
            'categories': serie.categories,
            'values':     serie.values,
        })
        # Add a chart title and some axis labels.
  #  chart1.set_title({'name': 'Results of sample analysis'})
   # chart1.set_x_axis({'name': 'Test number'})
    #chart1.set_y_axis({'name': 'Sample length (mm)'})

    # Set an Excel chart style. Colors with white outline and shadow.
    chart1.set_style(10)

    # Insert the chart into the worksheet (with an offset).
    sheet.insert_chart('D2', chart1, {'x_offset': 25, 'y_offset': 10})

class Serie(object):
    name = ''
    categories = ''
    values = ''