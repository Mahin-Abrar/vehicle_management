# Copyright (c) 2023, Mahin Abrar and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

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