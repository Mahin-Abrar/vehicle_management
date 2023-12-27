import frappe
from erpnext.stock.doctype.material_request.material_request import MaterialRequest

class MaterialRequestController(MaterialRequest):
    def validate(slef):
        print (">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")