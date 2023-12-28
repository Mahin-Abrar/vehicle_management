import frappe
from erpnext.stock.doctype.material_request.material_request import MaterialRequest

class MaterialRequestController(MaterialRequest):
   def validate(self):
      self.calculate()
        
   def calculate(self):
      total_quantity=0
      sum_amount=0
      for row in self.get('items'):
         row.amount=row.qty*row.rate
         sum_amount += row.amount
         total_quantity+=row.qty 
      self.total_quantity=total_quantity
      self.sum_amount=sum_amount