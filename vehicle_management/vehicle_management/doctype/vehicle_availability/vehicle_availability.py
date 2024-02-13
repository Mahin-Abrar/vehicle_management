# Copyright (c) 2023, Mahin Abrar and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
from frappe.model.mapper import get_mapped_doc

class VehicleAvailability(Document):
    def on_submit(self):
            self.set_details_value()
    def on_cancel(self):
            self.rmv_details_value()
            
            
            
            
    def set_details_value(self):
            self.status="To Price"
            self.save()
            vehecle_details = frappe.get_doc('Vehicle Details', self.vehicle_chassis_no)
            vehecle_details.status="To Price"
            vehecle_details.save()
            
    def rmv_details_value(self):  
            cancel_vehecle_details=frappe.get_doc('Vehicle Details', self.vehicle_chassis_no)
            cancel_vehecle_details.status='To Availability & Price'
            self.status=''
            cancel_vehecle_details.save()
            
            
@frappe.whitelist()
def make_vehicle_price(source_name, target_doc=None):
    doc = get_mapped_doc(
        "Vehicle Availability",
        source_name,
        {
            "Vehicle Availability": {
                "doctype": "Vehicle Price",
                "field_map": {
                    "vehicle_chassis_no": "vehicle_chassis_no",
                },
                "validation": {
                    "docstatus": ["=", 1]
                }
            }
        }, target_doc)

    return doc            