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

import logging

from gitinspector.daocommitdiff import DaoCommitDiff
from gitinspector.reportrow import ReportRow

__SqliteDaoCommitDiff__ = None
__code_type_data_sheet__ = None
__data_sheet__ = None


def get_sqlite_dao():
    global __SqliteDaoCommitDiff__
    if __SqliteDaoCommitDiff__ == None:
        __SqliteDaoCommitDiff__ = SqliteDaoCommitDiff()
    return __SqliteDaoCommitDiff__

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
        self.cursor.execute('''CREATE TABLE org_members
                               (id INTEGER, email VARCHAR(100), name TEXT, position TEXT, adm_team TEXT, role TEXT, capacity INTEGER, company TEXT,
                                 team TEXT, work_centre TEXT)''')
        self.connection.commit()

    def insert_change(self, commit_diff):
        self.cursor.execute('''INSERT INTO changes (id, email, insertions, 
                                                       deletions, commits, date_diff, 
                                                       author_name, code_type, file_name)
                                 VALUES (?,?,?,?,?,?,?,?,?)''',
                            (commit_diff.key, commit_diff.email.lower(), commit_diff.insertions,
                             commit_diff.deletions, commit_diff.commits, commit_diff.date,
                             commit_diff.author_name, commit_diff.get_code_type(), commit_diff.file_name,))
        self.connection.commit()

    def insert_commit(self, email, date):
        self.cursor.execute('''INSERT INTO commits (email, date_commit)
                                         VALUES (?,?)''',
                            (email.lower(), date,))
        self.connection.commit()

    def get_sum(self):  # must return array of ReportRow
        rows = [];
        for row in self.cursor.execute('''SELECT ifnull(o.name,ifnull(d.email, d.author_name)) name, d.code_type, 
                                       SUM(d.insertions) insertions, SUM(d.deletions) deletions, 
                                       count(c.email), substr(d.date_diff,1,7) month
                                  FROM changes d
                                  LEFT JOIN commits c
                                  ON c.email = d.email AND d.date_diff= c.date_commit
                                  LEFT JOIN org_members o
                                  ON o.email = d.email 
                                GROUP BY ifnull(o.name,ifnull(d.email, d.author_name)), d.code_type, substr(d.date_diff, 1, 7)
                                ORDER BY month, name'''):
            logging.info(row)
            report_row = ReportRow();
            report_row.author_name = row[0];
            report_row.code_type = row[1];
            report_row.insertions = row[2];
            report_row.deletions = row[3];
            report_row.commits = row[4];
            report_row.month = row[5];
            rows.append(report_row);
        return rows;

    def get_code_type_data(self):  # must return array of array with sum modifies with code type as column
        data = [];
        headings = ['Author'];
        sql_pivot = 'SELECT ifnull(o.name,ifnull(d.email, d.author_name)) name '
        for row in self.cursor.execute('''SELECT d.code_type
                                  FROM changes d
                                  GROUP BY code_type
                                  ORDER BY code_type'''):
            headings.append(row[0])
            sql_pivot += ", SUM(CASE WHEN code_type='" + row[0] + "'   THEN d.insertions + d.deletions END) " + row[
                0].replace(' ', '') + " "
        sql_pivot += ''' FROM changes d
                         LEFT JOIN org_members o
                             ON o.email = d.email 
                         GROUP BY ifnull(o.name,ifnull(d.email, d.author_name))'''
        data.append(headings)
        for row in self.cursor.execute(sql_pivot):
            logging.info(row)
            data.append(row)

        return data;

    def close(self):
        self.cursor.close()
        self.connection.close()

    def insert_org_structure(self, org_structure):
        for item in org_structure.members:
            self.cursor.execute('''INSERT INTO org_members (id, email, name, position, adm_team, role, capacity, company,
                                 team, work_centre)
                                     VALUES (?,?,?,?,?,?,?,?,?,?)''',
                                (1, item.email.lower(), item.name, item.position, item.adm_team, item.role, item.capacity, item.company,
                                 item.team, item.work_centre,))
        self.connection.commit()

    def get_sum_by_team(self):  # must return array of array with sum modifies as column by team
        rows = [];
        for row in self.cursor.execute('''SELECT ifnull(o.team,ifnull(o.name,ifnull(d.email, d.author_name))) name, d.code_type, 
                                       SUM(d.insertions) insertions, SUM(d.deletions) deletions, 
                                       count(c.email), substr(d.date_diff,1,7) month
                                  FROM changes d
                                  LEFT JOIN commits c
                                  ON c.email = d.email AND d.date_diff= c.date_commit
                                  LEFT JOIN org_members o
                                  ON o.email = d.email 
                                GROUP BY ifnull(o.team,ifnull(o.name,ifnull(d.email, d.author_name))), d.code_type, substr(d.date_diff, 1, 7)
                                ORDER BY month, name'''):
            logging.info(row)
            report_row = ReportRow();
            report_row.author_name = row[0];
            report_row.code_type = row[1];
            report_row.insertions = row[2];
            report_row.deletions = row[3];
            report_row.commits = row[4];
            report_row.month = row[5];
            rows.append(report_row);
        return rows;