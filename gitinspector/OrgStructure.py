import logging
from xlrd import open_workbook


class OrganizationMember(object):
    # Имя сотрудника	Должность	Группа	Роль	Емкость	Компания	Рабочая группа	Рабочий центр	Электронная почта

    def __init__(self, name, position, adm_team, role, capacity, company, team, work_centre, email):
        self.name = name
        self.position = position
        self.adm_team = adm_team
        self.role = role
        self.capacity = capacity
        self.company = company
        self.team = team
        self.work_centre = work_centre
        self.email = email

    def __str__(self):
        return ("OrganizationMember object:\n"
                "  name = {0}\n"
                "  position = {1}\n"
                "  adm_team = {2}\n"
                "  role = {3}\n"
                "  capacity = {4} \n"
                "  company = {5} \n"
                "  team = {6} \n"
                "  work_centre = {7} \n"
                "  email = {8} "
                .format(self.name, self.position, self.adm_team, self.role, self.capacity, self.company,
                        self.team, self.work_centre, self.email))


class OrganizationStructure(object):
    def __init__(self):
        self.members = []

    def add_member(self, member):
        self.members.append(member)

    def load_from_excel(self, filename):
        logging.info("Load org structure from "+ filename)
        wb = open_workbook(filename)
        for sheet in wb.sheets():
            number_of_rows = sheet.nrows
            number_of_columns = sheet.ncols
            for row in range(1, number_of_rows):
                values = []
                for col in range(number_of_columns):
                    value = (sheet.cell(row, col).value)
                    try:
                        value = str(int(value))
                    except ValueError:
                        pass
                    finally:
                        values.append(value)
                item = OrganizationMember(*values)
                self.add_member(item)

        #for item in self.members:
        #    print(item)

        logging.info("Loaded "+ str(len(self.members)))