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
def make_vehicle_availability(source_name, target_doc=None, args=None):
	doclist = get_mapped_doc(
		"Vehicle Details",
		source_name,
		{
			"Vehicle Details": {
				"doctype": "Vehicle Availability",
				# "validation": {"status": ["=", "To Availability & Price"]},
				"field_map":[
     				["chassis_number","vehicle_chassis_no"],
				]
			},
   	},
  target_doc
	)
	
	return doclist