# Copyright (c) 2023, Mahin Abrar and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class VehicleDetails(Document):
        def on_submit(self):
            self.get_indicator()
        def get_indicator(self):
            doc = frappe.get_doc('Vehicle Details', self.chassis_number)
            doc.status="To Availability & Price"
            doc.save()
      # pass
      # def on_submit(self):
      #       doc=frappe.get_doc("Vehicle Details",self.chassis_number)
      #       doc.level="To Availability & Price"
      #       doc.save()
	# def validate(self):
      #       if frappe.db.exists("Vehicle Details",self.chassis_number):    
      #             frappe.throw('ase already kana')
     