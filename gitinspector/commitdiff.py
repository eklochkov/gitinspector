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
from gitinspector import extensions
from gitinspector.filediff import FileDiff


class CommitDiff(object):
    key = 0
    email = None
    insertions = 0
    deletions = 0
    commits = 0
    date = None
    author_name = None
    file_name = None

    # get code type of changing (java, sql, etc..)
    def get_code_type(self):
        code_type = None
        if self.file_name:
            extension = FileDiff.get_extension(self.file_name)
            code_type = extensions.get_dict()[extension]
        return code_type