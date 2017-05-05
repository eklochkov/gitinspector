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
__data_sheet__ = None

def get_excel_book():
     global __excel_book__
     if __excel_book__ == None:
         __excel_book__ = xlsxwriter.Workbook("test.xlsx")
     return __excel_book__

def get_data_sheet():
     global __data_sheet__
     if __data_sheet__ == None:
         __data_sheet__ =  get_excel_book().add_worksheet()
     return __data_sheet__