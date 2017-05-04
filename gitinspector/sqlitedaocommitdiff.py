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
import sqlite3

from gitinspector.reportrow import ReportRow


class SqliteDaoCommitDiff(object):
    def __init__(self):
        self.connection = sqlite3.connect(":memory:")
        self.cursor = self.connection.cursor()
        self.cursor.execute('''CREATE TABLE commits
                               (id INTEGER, email VARCHAR(100),insertions INTEGER, deletions INTEGER,
                               commits INTEGER, date_diff TEXT, author_name VARCHAR(100), code_type VARCHAR(100), 
                               file_name VARCHAR(256))''')
        self.connection.commit()

    def insert(self, commit_diff):
        self.cursor.execute('''INSERT INTO commits (id, email, insertions, 
                                                       deletions, commits, date_diff, 
                                                       author_name, code_type, file_name)
                                 VALUES (?,?,?,?,?,?,?,?,?)''',
                            (commit_diff.key, commit_diff.email, commit_diff.insertions,
                             commit_diff.deletions, commit_diff.commits, commit_diff.date,
                            commit_diff.author_name, commit_diff.get_code_type(), commit_diff.file_name,))
        self.connection.commit()



    def get_sum(self): #must return array of ReportRow
        rows = [];
        for row in self.cursor.execute('''SELECT ifnull(email, author_name) name, code_type, 
                                       SUM(insertions) insertions, SUM(deletions) deletions, 
                                       SUM(commits), substr(date_diff,1,7) month
                                  FROM commits 
                                GROUP BY ifnull(email, author_name), code_type, substr(date_diff, 1, 7)
                                ORDER BY month, email'''):
            print(row)
            report_row = ReportRow();
            report_row.author_name = row[0];
            report_row.code_type = row[1];
            report_row.insertions = row[2];
            report_row.deletions = row[3];
            report_row.commits = row[4];
            report_row.month = row[5];
            rows.append(report_row);
        return rows;

    def close(self):
        self.cursor.close()
        self.connection.close()