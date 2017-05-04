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
from .commitdiff import CommitDiff
class DaoCommitDiff(object):
    def insert(self, CommitDiff):
        raise NotImplementedError(_("Method insert not yet supported in") + " \"" + self.__class__.__name__ + "\".")

    def get_sum(self): #must return array of ReportRow
            raise NotImplementedError(_("Method insert not yet supported in") + " \"" + self.__class__.__name__ + "\".")

    def close(self):
        raise NotImplementedError(_("Method insert not yet supported in") + " \"" + self.__class__.__name__ + "\".")