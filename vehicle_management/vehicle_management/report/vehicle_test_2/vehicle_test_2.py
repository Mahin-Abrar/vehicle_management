# Copyright (c) 2023, Mahin Abrar and contributors
# For license information, please see license.txt

import frappe
from frappe.query_builder import DocType
from frappe import _

def execute(filters=None):  
    if not filters: filters = {}
    if filters.get('from_date') and filters.get('to_date') and filters.get('to_date') < filters.get('from_date'):
        frappe.throw("The 'From Date' ({}) must be before the 'To Date' ({})".format(filters.from_date, filters.to_date))
    return get_columns(filters), get_data(filters)


####using query builder #####
def get_data(filters):
    vehicle_details=frappe.qb.DocType("Vehicle Details")
    vehicle_availability=frappe.qb.DocType("Vehicle Availability")
    vehicle_price=frappe.qb.DocType("Vehicle Price")
    query=(
        frappe.qb.from_(vehicle_details)
        .left_join(vehicle_availability)
        .on(vehicle_details.chassis_number ==vehicle_availability.vehicle_chassis_no)
        .left_join(vehicle_price)
        .on(vehicle_details.chassis_number ==vehicle_price.vehicle_chassis_no)
        .select(vehicle_details.chassis_number, vehicle_details.car_model, vehicle_details.model_year,
            vehicle_details.shape, vehicle_details.auction_grade, vehicle_details.package,
            vehicle_details.color, vehicle_details.milage, vehicle_details.cc,
            vehicle_details.seat_capacity, vehicle_details.origin_country,
            vehicle_availability.status, vehicle_price.sale_price,
            vehicle_price.posting_date,
            vehicle_price.grand_total, vehicle_price.customer) 
     )
    
    if filters.get("chassis_number"):
        query = query.where(vehicle_details.chassis_number ==filters.get("chassis_number"))
    if filters.get("car_model"):
        query = query.where(vehicle_details.car_model ==filters.get("car_model"))
    if filters.get("shape"):
        query = query.where(vehicle_details.shape ==filters.get("shape"))
    if filters.get("origin_country"):
        query = query.where(vehicle_details.origin_country ==filters.get("origin_country"))
    if filters.get('from_date'):
        query = query.where(vehicle_price.posting_date >= filters.get('from_date'))
    if filters.get('to_date'):
        query = query.where(vehicle_price.posting_date <= filters.get('to_date'))
    
    data=query.run(as_dict=True)
    return data

# for generating the columns     
def get_columns(filters):
    return [
		 {
       "fieldname": "chassis_number",
       "label": "Chassis Number", 
       "fieldtype": "Link",
       "options": "Vehicle Details"
       },
        {"fieldname": "car_model", "label": "Car Model","fieldtype": "Link", "options": "Car Model"},
        {"fieldname": "model_year","label": "Model Year", "fieldtype": "Int"},
        {"fieldname": "shape","label": "Shape",  "fieldtype": "Select","options": [" ", "Old", "New"],},
        {"fieldname": "auction_grade","label": "Auction Grade", "fieldtype": "Data"},
        {"fieldname": "package","label": "Package",  "fieldtype": "Data"},
        {"fieldname": "color", "label": "Color", "fieldtype": "Data"},
        {"fieldname": "milage", "label": "Milage", "fieldtype": "Float"},
        {"fieldname": "cc", "label": "CC","fieldtype": "Int"},
        {"fieldname": "seat_capacity", "label": "Seat Capacity","fieldtype": "Int"},
        {"fieldname": "origin_country", "label": "Origin Country","fieldtype": "Data"},
        {"fieldname": "status", "label": "Vehicle Status","fieldtype": "Select"},
        {"fieldname": "sale_price", "label": "Sale Price","fieldtype": "Currency"},
        {"fieldname": "grand_total", "label": "Grand Total","fieldtype": "Currency"},
        {"fieldname": "customer", "label": "Customer","fieldtype": "Data"},
        {"fieldname": "posting_date", "label": "Posting Date","fieldtype": "Date"}
	]