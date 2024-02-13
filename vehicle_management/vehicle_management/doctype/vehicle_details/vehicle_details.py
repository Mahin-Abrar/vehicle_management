# Copyright (c) 2023, Mahin Abrar and contributors
# For license information, please see license.txt
from frappe import _
import frappe
from frappe.model.document import Document
from frappe.model.mapper import get_mapped_doc

class VehicleDetails(Document):
        def on_submit(self):
            self.status_indicator()
        def on_cancel(self):
            self.status="Cancelled"
        def status_indicator(self):
            self.status="To Availability & Price"
            self.save()
        def status_cancel(self):
            self.status=""
            self.save()


@frappe.whitelist()
def make_vehicle_availability(source_name, target_doc=None):
    doc = get_mapped_doc(
        "Vehicle Details",
        source_name,
        {
            "Vehicle Details": {
                "doctype": "Vehicle Availability",
                "field_map": {
                    "name": "vehicle_chassis_no",
                },
                "validation": {
                    "docstatus": ["=", 1]
                }
            }
        }, target_doc)

    return doc
# @frappe.whitelist()
# def make_vehicle_availability(source_name, target_doc=None):
# 	target_doc = frappe.model.mapper.get_mapped_doc("Vehicle Details", source_name,
# 		{"Vehicle Details": {
# 			"doctype": "Vehicle Availability",
# 			"field_map": {
# 				"name": "vehicle_chassis_no",
# 			}
# 		}}, target_doc)

# 	return target_doc
