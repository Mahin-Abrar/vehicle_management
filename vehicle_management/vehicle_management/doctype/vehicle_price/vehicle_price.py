# Copyright (c) 2023, Mahin Abrar and contributors
# For license information, please see license.txt

import frappe
from frappe.query_builder import DocType
from frappe import _
from frappe.model.document import Document
from frappe import get_all, get_doc
from deep_translator import GoogleTranslator


class VehiclePrice(Document):
    def validate(self):
        self.total_calculations()
        translated = GoogleTranslator(source='auto', target='ar').translate("Mahin")  # output -> Weiter so, du bist großartig
        print(translated)
        print(">>>>>>>>>>>>>>>")
        
                
    def on_submit(self):
        self.add_vehicle_details()
        self.sold_unsold()
        self.add_vehicle_availability()
         
    def on_cancel(self):
            self.rmv_vehicle_details()
            self.rmv_vehicle_availability()
            self.status=''
            
#####functions####      


#     def amended_validation(self):
#             key=frappe.db.get_list('Vehicle Availability',filters={'vehicle_chassis_no':self.vehicle_chassis_no},pluck='name')
#             docVA= frappe.get_doc('Vehicle Availability',key)
#             va_chassis=docVA.vehicle_chassis_no
#             my_chassis=self.vehicle_chassis_no
#             vehicle_availbility=frappe.qb.DocType('Vehicle Availability')
#             query=(
#                     frappe.qb.from_(vehicle_availbility)
#                     .select(vehicle_availbility.amended_from)
#                     .where(vehicle_availbility.vehicle_chassis_no==my_chassis)
#             ).run(as_dict=True)
#             print (query)
            
    
    
    def add_vehicle_details(self):
         vehicle_details_doc = frappe.get_doc('Vehicle Details', self.vehicle_chassis_no)
         vehicle_details_doc.customer = self.customer
         vehicle_details_doc.status="Completed"
         vehicle_details_doc.is_sold=self.is_sold
         vehicle_details_doc.save()
         
    def sold_unsold(self):
        if self.is_sold==True:
                self.status = "Sold"
        elif self.is_sold==False:
                self.status = "Un Sold"
        self.save()
         
    def add_vehicle_availability(self):
            primary_key=frappe.db.get_list('Vehicle Availability',filters={'vehicle_chassis_no':self.vehicle_chassis_no},pluck='name')
            vehecle_availability_doc= frappe.get_doc('Vehicle Availability',primary_key)
            vehecle_availability_doc.customer = self.customer
            vehecle_availability_doc.status="Completed"
            vehecle_availability_doc.is_sold = self.is_sold
            vehecle_availability_doc.save()
        
    def rmv_vehicle_details(self):
            vehecle_details_rmv = frappe.get_doc('Vehicle Details', self.vehicle_chassis_no)
            vehecle_details_rmv.customer=''
            vehecle_details_rmv.is_sold = False
            vehecle_details_rmv.status='To Price'
            vehecle_details_rmv.save()
        
    def rmv_vehicle_availability(self):
            primary_key=frappe.db.get_list('Vehicle Availability',filters={
                    'vehicle_chassis_no':self.vehicle_chassis_no
                    },pluck='name')
            vehicle_availability_rmv=frappe.get_doc('Vehicle Availability',primary_key)
            vehicle_availability_rmv.customer=''
            vehicle_availability_rmv.is_sold=False
            vehicle_availability_rmv.status='To Price'
            vehicle_availability_rmv.save()
            
    def total_calculations(self):
            self.sale_price = self.customer_price+self.company_price
            for row in self.get('other_vehicle_items'):
              row.amount=row.quantity*row.rate
              self.item_amount += row.amount
            self.grand_total=self.item_amount +self.sale_price    
              


@frappe.whitelist()
def check_vehicle_availability(chassis_no):
        print("ssssssssssssssssssssssssssssssssssssssssssssssssssssssssssss")
        print(chassis_no)
        ##Check if chassis number exists in Vehicle Availability doctype
        primary_key=frappe.db.get_list('Vehicle Availability',filters={'vehicle_chassis_no':chassis_no},pluck='name')
        vehecle_availability_status= frappe.get_doc('Vehicle Availability',primary_key)
        exists=vehecle_availability_status.docstatus
        return exists