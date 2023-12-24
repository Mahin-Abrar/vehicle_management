// Copyright (c) 2023, Mahin Abrar and contributors
// For license information, please see license.txt
/* eslint-disable */

frappe.query_reports["Vehicle Test 2"] = {
	"filters": [
		{
			"fieldname": "chassis_number",
			"label": "Chassis Number", 
			"fieldtype": "Link",
			"options": "Vehicle Details",
			},
	]
};
