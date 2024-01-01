# Copyright (c) 2023, Mahin Abrar and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
from frappe import get_all, get_doc



class VehiclePrice(Document):
    def validate(self):
        self.sale_price = self.customer_price+self.company_price
        self.grand_total=self.item_amount +self.sale_price
        for row in self.get('other_vehicle_items'):
            row.amount=row.quantity*row.rate
            self.other_items_total += row.amount
                
    def on_submit(self):
        self.add_vehicle_details()
        self.add_vehicle_availability()
        self.get_indicator()
        
        
    def get_indicator(self):
            vd = frappe.get_doc('Vehicle Details', self.vehicle_chassis_no)
            vd.status="Completed"
            vd.save()
    
    def on_cancel(self):
        self.rmv_vehicle_details()
        self.rmv_vehicle_availability()
    def on_cancel(self):
            self.status=''
            vdc=frappe.get_doc('Vehicle Details', self.vehicle_chassis_no)
            vac_key=frappe.db.get_list('Vehicle Availability',filters={'vehicle_chassis_no':self.vehicle_chassis_no},pluck='name')
            vac= frappe.get_doc('Vehicle Availability',vac_key)
            vac.status='To Price'
            vdc.status='To Price'
            vdc.save()
            vac.save()
            
    def add_vehicle_details(self):
         vd_doc = frappe.get_doc('Vehicle Details', self.vehicle_chassis_no)
         vd_doc.customer = self.customer
         vd_doc.is_sold=self.is_sold
         vd_doc.save()

         
    def add_vehicle_availability(self):
            p_key=frappe.db.get_list('Vehicle Availability',filters={'vehicle_chassis_no':self.vehicle_chassis_no},pluck='name')
            doc2= frappe.get_doc('Vehicle Availability',p_key)
            doc2.customer = self.customer
            doc2.status="Completed"
            doc2.is_sold = self.is_sold
            doc2.save()
        
    def rmv_vehicle_details(self):
            doc = frappe.get_doc('Vehicle Details', self.vehicle_chassis_no)
            doc.customer=''
            doc.is_sold = False
            doc.save()
        
    def rmv_vehicle_availability(self):
            p_key=frappe.db.get_list('Vehicle Availability',filters={
                    'vehicle_chassis_no':self.vehicle_chassis_no
                    },pluck='name')
            doc2=frappe.get_doc('Vehicle Availability',p_key)
            doc2.customer=''
            doc2.is_sold=False
            doc2.save()