# Copyright (c) 2023, Mahin Abrar and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class VehicleAvailability(Document):
    def on_submit(doc):
            doc.status="To Price"
            doc.save()
            vd = frappe.get_doc('Vehicle Details', doc.vehicle_chassis_no)
            vd.status="To Price"
            vd.save()
    # def on_submit(self):
    #         vd = frappe.get_doc('Vehicle Details', self.vehicle_chassis_no)
    #         vd.status="To Price"
    #         vd.save()
           
    # def get_indicator(self):
    #         p_key=frappe.db.get_list('Vehicle Availability',filters={'vehicle_chassis_no':self.vehicle_chassis_no},pluck='name')
    #         doc2= frappe.get_doc('Vehicle Availability',p_key)
    #         doc2.status="To Price"
    #         doc2.save()