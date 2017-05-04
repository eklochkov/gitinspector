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
import stashy


class StashIntegration(object):
    stash = None
    user_name = ''
    def __init__(self,url,user_name, password):
        self.user_name = user_name
        self.url = url
        self.stash = stashy.connect('https://'+self.url, self.user_name, password)

    def get_projects_like(self, substring):
        project_list = self.stash.projects.list()
        for i in project_list:
            if i['key'].find(substring) != -1:
              print(i['key'])

    def get_reps_like(self, project_substring):
        project_list = self.stash.projects.list()
        reps = []
        for project in project_list:
            if project['key'].find(project_substring) != -1:
              print("project=",project['key'])
              for rep in  self.stash.projects[project['key']].repos.list():
                  reps.append( 'https://{0}@{1}/scm/{2}/{3}.git'.format(self.user_name,self.url,project['key'],rep['name']))
        return reps