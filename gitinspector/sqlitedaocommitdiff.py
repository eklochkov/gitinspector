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

from gitinspector.daocommitdiff import DaoCommitDiff
from gitinspector.reportrow import ReportRow


class SqliteDaoCommitDiff(DaoCommitDiff):
    def __init__(self):
        self.connection = sqlite3.connect(":memory:")
        self.cursor = self.connection.cursor()
        self.cursor.execute('''CREATE TABLE changes
                               (id INTEGER, email VARCHAR(100),insertions INTEGER, deletions INTEGER,
                               commits INTEGER, date_diff TEXT, author_name VARCHAR(100), code_type VARCHAR(100), 
                               file_name VARCHAR(256))''')
        self.cursor.execute('''CREATE TABLE commits
                               (email VARCHAR(100), date_commit TEXT)''')
        self.connection.commit()

    def insert_change(self, commit_diff):
        self.cursor.execute('''INSERT INTO changes (id, email, insertions, 
                                                       deletions, commits, date_diff, 
                                                       author_name, code_type, file_name)
                                 VALUES (?,?,?,?,?,?,?,?,?)''',
                            (commit_diff.key, commit_diff.email, commit_diff.insertions,
                             commit_diff.deletions, commit_diff.commits, commit_diff.date,
                            commit_diff.author_name, commit_diff.get_code_type(), commit_diff.file_name,))
        self.connection.commit()

    def insert_commit(self, email, date):
        self.cursor.execute('''INSERT INTO commits (email, date_commit)
                                         VALUES (?,?)''',
                            (email, date,))
        self.connection.commit()

    def get_sum(self): #must return array of ReportRow
        rows = [];
        for row in self.cursor.execute('''SELECT ifnull(d.email, d.author_name) name, d.code_type, 
                                       SUM(d.insertions) insertions, SUM(d.deletions) deletions, 
                                       count(c.email), substr(d.date_diff,1,7) month
                                  FROM changes d
                                  LEFT JOIN commits c
                                  ON c.email = d.email AND d.date_diff= c.date_commit
                                GROUP BY ifnull(d.email, d.author_name), d.code_type, substr(d.date_diff, 1, 7)
                                ORDER BY month, name'''):
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