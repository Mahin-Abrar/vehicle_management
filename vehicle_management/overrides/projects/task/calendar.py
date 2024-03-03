# import json

# import frappe
# from frappe import _
# from frappe.utils import formatdate, getdate, today


# @frappe.whitelist()
# def get_events(doctype, start, end, field_map, filters=None, fields=None):
# 	field_map = frappe._dict(json.loads(field_map))
# 	fields = frappe.parse_json(fields)

# 	doc_meta = frappe.get_meta(doctype)
# 	for d in doc_meta.fields:
# 		if d.fieldtype == "Color":
# 			field_map.update({"color": d.fieldname})

# 	filters = json.loads(filters) if filters else []

# 	if not fields:
# 		fields = [field_map.start, field_map.end, field_map.title, "name"]

# 	if field_map.color:
# 		fields.append(field_map.color)

# 	start_date = "ifnull(%s, '0001-01-01 00:00:00')" % field_map.start
# 	end_date = "ifnull(%s, '2199-12-31 00:00:00')" % field_map.end

# 	filters += [
# 		[doctype, start_date, "<=", end],
# 		[doctype, end_date, ">=", start],
# 	]
# 	fields = list({field for field in fields if field})
# 	print("??????????????????????????????????//")
# 	print (frappe.get_list(doctype, fields=fields, filters=filters))
# 	return frappe.get_list(doctype, fields=fields, filters=filters)
# # @frappe.whitelist()
# # def get_events(start, end, filters=None):
# # 	"""Returns events for Gantt / Calendar view rendering.

# # 	:param start: Start date-time.
# # 	:param end: End date-time.
# # 	:param filters: Filters (JSON).
# # 	"""
# # 	if filters:
# # 		filters = json.loads(filters)
# # 	else:
# # 		filters = []

# # 	if start:
# # 		filters.append(["Holiday", "holiday_date", ">", getdate(start)])
# # 	if end:
# # 		filters.append(["Holiday", "holiday_date", "<", getdate(end)])

# # 	return frappe.get_list(
# # 		"Holiday List",
# # 		fields=[
# # 			"name",
# # 			"`tabHoliday`.holiday_date",
# # 			"`tabHoliday`.description",
# # 			"`tabHoliday List`.color",
# # 		],
# # 		filters=filters,
# # 		update={"allDay": 1},
# # 	)



