# Copyright (c) 2023, Mahin Abrar and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class VehicleDetails(Document):
        def on_submit(self):
            self.status_indicator()
        def status_indicator(self):
            doc = frappe.get_doc('Vehicle Details', self.chassis_number)
            doc.status="To Availability & Price"
            doc.save()