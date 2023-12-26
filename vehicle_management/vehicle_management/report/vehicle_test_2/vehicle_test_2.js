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
				"fieldname": "from_date",
				"label": "From Date",
				"fieldtype": "Date",
				// "options":"Vehicle Price"
				},
				{
				"fieldname": "to_date",
				"label": "To Date",
				"fieldtype": "Date",
				// "options":"Vehicle Price"
				}
				
	]
};
