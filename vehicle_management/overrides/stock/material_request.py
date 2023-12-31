import frappe
from erpnext.stock.doctype.material_request.material_request import MaterialRequest

class MaterialRequestController(MaterialRequest):
   def validate(self):
      self.calculate()
        
   def calculate(self):
      custom_qty=0
      sum_total=0
      for row in self.get('items'):
         row.amount=row.qty*row.rate
         sum_total += row.amount
         custom_qty+=row.qty 
      self.total_quantity_amount=custom_qty
      self.total_payment_amount=sum_total
      print(self.total_payment_amount)
      print(self.total_quantity_amount)