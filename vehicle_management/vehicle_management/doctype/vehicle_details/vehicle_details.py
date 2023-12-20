# Copyright (c) 2023, Mahin Abrar and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class VehicleDetails(Document):
	def validate(self):
            if frappe.db.exists("Vehicle Details",self.chassis_number):    
                  frappe.throw('ase already kana')