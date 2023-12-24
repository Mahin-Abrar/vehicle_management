# Copyright (c) 2023, Mahin Abrar and contributors
# For license information, please see license.txt

import frappe
from frappe import _

def execute(filters=None):
    return get_columns(filters), get_data(filters)



## for generating the columns     
def get_columns(filters):
    return [
		 {
       "fieldname": "chassis_number",
       "label": "Chassis Number", 
       "fieldtype": "Data"
       },
        {"fieldname": "car_model", "label": "Car Model","": "Link", "options": "Car Model"},
        {"fieldname": "model_year","label": "Model Year", "fieldtype": "Int"},
        {"fieldname": "shape","label": "Shape",  "fieldtype": "Data"},
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
	]
##for fetching the values for the column
def get_data(filters):
    conditions = create_conditions(filters)
    query = frappe.db.sql("""    select
            vd.chassis_number,vd.car_model,vd.model_year,vd.shape,vd.auction_grade,vd.package,vd.color,vd.milage,vd.cc,vd.seat_capacity,vd.origin_country,va.status,vp.sale_price,vp.grand_total,vp.customer
        FROM
            `tabVehicle Details` vd         
            LEFT JOIN
            `tabVehicle Availability` va ON vd.chassis_number = va.vehicle_chassis_no
            LEFT JOIN
            `tabVehicle Price` vp ON vd.chassis_number = vp.vehicle_chassis_no %s """ % (conditions), filters, as_list = 1)
    return query


def create_conditions(filters):
    conditions = ""
    if filters.get('chassis_number'):
        conditions += "where vd.chassis_number = %(chassis_number)s"
        
    # if filters.get('chassis_number'):
    #     conditions += "and vd.chassis_number = %(chassis_number)s"
    return conditions