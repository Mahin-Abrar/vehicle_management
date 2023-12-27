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
			{
				"fieldname": "car_model",
				"label": "Car Model", 
				"fieldtype": "Link",
				"options": "Car Model",
				},
				{
				"fieldname": "shape",
				"label": "Shape", 
				"fieldtype": "Select",
				"options": [" ","Old","New"],
				},
				{
				"fieldname": "origin_country",
				"label": "Origin Country", 
				"fieldtype": "Link",
				"options": "Country",
				},
				{
					fieldname: "from_date",
					label: "Date From Filter",
					fieldtype: "Date",
					default: frappe.datetime.add_months(frappe.datetime.get_today(), -1)
				},
				{
					fieldname: "to_date",
					label: "Date To Filter",
					fieldtype: "Date",
					default: frappe.datetime.get_today()
				}
				
	]
};
