# Copyright (c) 2023, Mahin Abrar and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class VehiclePrice(Document):
    def validate(self):
        self.sale_price = self.customer_price+self.company_price
        self.grand_total=self.other_items_total +self.sale_price
        self.other_items_total = 0
        for row in self.get('other_vehicle_items'):
            row.amount=row.quantity*row.rate
            self.other_items_total += row.amount