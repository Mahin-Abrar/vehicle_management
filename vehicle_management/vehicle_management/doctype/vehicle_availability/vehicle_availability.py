# Copyright (c) 2023, Mahin Abrar and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class VehicleAvailability(Document):
    def on_submit(self):
            self.set_details_value()
    def on_cancel(self):
            self.rmv_details_value()
            
            
            
    def set_details_value(self):
            self.status="To Price"
            self.save()
            vd = frappe.get_doc('Vehicle Details', self.vehicle_chassis_no)
            vd.status="To Price"
            vd.save()
            
    def rmv_details_value(self):
            self.status=''
            self.save()
            vdc=frappe.get_doc('Vehicle Details', self.vehicle_chassis_no)
            vdc.status='To Availability & Price'
            vdc.save()