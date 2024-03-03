# Copyright (c) 2024, Mahin Abrar and contributors
# For license information, please see license.txt
import json
from datetime import date

import frappe
from frappe import _, throw
from frappe.model.document import Document
from frappe.utils import formatdate, getdate, today

class Calendar(Document):
	pass
@frappe.whitelist()
def get_events():
	
	data = frappe.db.sql("""
		 SELECT CONCAT('Holiday: ', description) as subject, '#000000' as color, holiday_date as exp_start_date, holiday_date as exp_end_date FROM `tabHoliday` UNION SELECT CONCAT('Task: ', subject) as subject, '#ffffff' as color, exp_start_date as exp_start_date, exp_end_date as exp_end_date  FROM `tabTask`
		""", as_dict=True)
	return data
# import frappe
# import json

# @frappe.whitelist()
# def get_events(start, end, filters=None):
#     """Returns events for Gantt / Calendar view rendering.

#     :param start: Start date-time.
#     :param end: End date-time.
#     :param filters: Filters (JSON).
#     """
#     if filters:
#         filters = json.loads(filters)
#     else:
#         filters = []

#     if start:
#         filters.append(["Holiday", "holiday_date", ">", frappe.utils.getdate(start)])
#     if end:
#         filters.append(["Holiday", "holiday_date", "<", frappe.utils.getdate(end)])

#     holidays = frappe.get_list(
#         "Holiday",
#         fields=["holiday_date", "holiday_date", "name","description"],
#         filters=filters,
#         update={"allDay": 1}
#     )

#     tasks = get_task_events(start, end)  

#     combined_events = holidays + tasks  

#     print(holidays)
#     return combined_events


# def get_task_events(start, end):
#     """Returns task events for Gantt / Calendar view rendering.

#     :param start: Start date-time.
#     :param end: End date-time.
#     """
#     filters = [
#         ["Task", "exp_start_date", "<=", end],
#         ["Task", "exp_end_date", ">=", start]
#     ]

#     task_events = frappe.get_list(
#         "Task",
#         fields=["name", "exp_start_date", "exp_end_date", "subject", "color"],
#         filters=filters
#     )

#     return task_events





# @frappe.whitelist()
# def get_events(start, end, filters=None):
# 	"""Returns events for Gantt / Calendar view rendering.

# 	:param start: Start date-time.
# 	:param end: End date-time.
# 	:param filters: Filters (JSON).
# 	"""
# 	if filters:
# 		filters = json.loads(filters)
# 	else:
# 		filters = []

# 	if start:
# 		filters.append(["Holiday", "holiday_date", ">", getdate(start)])
# 	if end:
# 		filters.append(["Holiday", "holiday_date", "<", getdate(end)])

# 	return frappe.get_list(
# 		"Holiday List",
# 		fields=[
# 			"name",
# 			"`tabHoliday`.holiday_date",
# 			"`tabHoliday`.description",
# 			"`tabHoliday List`.color",
# 		],
# 		filters=filters,
# 		update={"allDay": 1},
# 	)
