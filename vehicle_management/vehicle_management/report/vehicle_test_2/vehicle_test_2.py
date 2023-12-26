# Copyright (c) 2023, Mahin Abrar and contributors
# For license information, please see license.txt

import frappe
from frappe.query_builder import DocType
from frappe import _

def execute(filters=None):
    return get_columns(filters), get_data(filters)



## for generating the columns     
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

## without using query builder##################
# def create_conditions(filters):
#     VehicleDetails=frappe.qb.DocType("Vehicle Details")
#     VehicleAvailability=frappe.qb.DocType("Vehicle Availability")
#     VehiclePrice=frappe.qb.DocType("Vehicle Price")
#     conditions = ""
#     if filters.get('chassis_number'):
#         conditions += "where VehicleDetails.chassis_number = %(chassis_number)s"
        
#     if filters.get('car_model'):
#         conditions += "where VehicleDetails.car_model = %(car_model)s"
        
#     if filters.get('shape'):
#         conditions += "where VehicleDetails.shape = %(shape)s"    
    
#     if filters.get('origin_country'):
#         conditions += "where VehicleDetails.origin_country = %(origin_country)s"    
      
#     return conditions

####using query builder #####
def get_data(filters):
    # conditions=create_conditions(filters)
    VehicleDetails=frappe.qb.DocType("Vehicle Details")
    VehicleAvailability=frappe.qb.DocType("Vehicle Availability")
    VehiclePrice=frappe.qb.DocType("Vehicle Price")
    query=(
        frappe.qb.from_(VehicleDetails)
        .left_join(VehicleAvailability)
        .on(VehicleDetails.chassis_number ==VehicleAvailability.vehicle_chassis_no)
        .left_join(VehiclePrice)
        .on(VehicleDetails.chassis_number ==VehiclePrice.vehicle_chassis_no)
        .select(VehicleDetails.chassis_number, VehicleDetails.car_model, VehicleDetails.model_year,
            VehicleDetails.shape, VehicleDetails.auction_grade, VehicleDetails.package,
            VehicleDetails.color, VehicleDetails.milage, VehicleDetails.cc,
            VehicleDetails.seat_capacity, VehicleDetails.origin_country,
            VehicleAvailability.status, VehiclePrice.sale_price,
            VehiclePrice.posting_date,
            VehiclePrice.grand_total, VehiclePrice.customer)
       
     )
    if filters.get("chassis_number"):
        query = query.where(VehicleDetails.chassis_number ==filters.get("chassis_number"))
    if filters.get("car_model"):
        query = query.where(VehicleDetails.car_model ==filters.get("car_model"))
    if filters.get("shape"):
        query = query.where(VehicleDetails.shape ==filters.get("shape"))
    if filters.get("origin_country"):
        query = query.where(VehicleDetails.origin_country ==filters.get("origin_country"))
    if filters.get("from_date") and filters.get("to_date") and filters.get("to_date") <filters.get("from_date"):
        frappe.throw("The 'From Date' ({0}) must be before the 'To Date' ({1})".format(filters.from_filter, filters.to_filter))
    else:
        # query=query.where(VehiclePrice.posting_date[filters.get("from_date"):filters.get("to_date")])
        query=query.where(
        (VehiclePrice.posting_date <= filters.get("from_date")) and (VehiclePrice.posting_date >= filters.get("to_date"))
    )
    
    data=query.run(as_dict=True)
    return data


##for fetching the values for the column
# def get_data(filters):
#     conditions = create_conditions(filters)
#     query = frappe.db.sql("""    select
#             vd.chassis_number,vd.car_model,vd.model_year,vd.shape,vd.auction_grade,vd.package,vd.color,vd.milage,vd.cc,vd.seat_capacity,vd.origin_country,va.status,vp.sale_price,vp.grand_total,vp.customer
#         FROM
#             `tabVehicle Details` vd         
#             LEFT JOIN
#             `tabVehicle Availability` va ON vd.chassis_number = va.vehicle_chassis_no
#             LEFT JOIN
#             `tabVehicle Price` vp ON vd.chassis_number = vp.vehicle_chassis_no %s """ % (conditions), filters, as_list = 1)
#     return query