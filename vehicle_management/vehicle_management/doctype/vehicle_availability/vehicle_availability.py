# Copyright (c) 2023, Mahin Abrar and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
from frappe.model.mapper import get_mapped_doc

class VehicleAvailability(Document):
    def on_submit(self):
            self.set_details_value()
    def on_cancel(self):
            self.rmv_details_value()
            
            
            
            
    def set_details_value(self):
            self.status="To Price"
            self.save()
            vehecle_details = frappe.get_doc('Vehicle Details', self.vehicle_chassis_no)
            vehecle_details.status="To Price"
            vehecle_details.save()
            
    def rmv_details_value(self):  
            cancel_vehecle_details=frappe.get_doc('Vehicle Details', self.vehicle_chassis_no)
            cancel_vehecle_details.status='To Availability & Price'
            self.status=''
            cancel_vehecle_details.save()
            
            
@frappe.whitelist()
def make_vehicle_price(source_name, target_doc=None):
    doc = get_mapped_doc(
        "Vehicle Availability",
        source_name,
        {
            "Vehicle Availability": {
                "doctype": "Vehicle Price",
                "field_map": {
                    "vehicle_chassis_no": "vehicle_chassis_no",
                },
                "validation": {
                    "docstatus": ["=", 1]
                }
            }
        }, target_doc)

    return doc            

@frappe.whitelist()
def make_purchase_order(source_name, target_doc=None, args=None):
	if args is None:
		args = {}
	if isinstance(args, str):
		args = json.loads(args)

	def postprocess(source, target_doc):
		if frappe.flags.args and frappe.flags.args.default_supplier:
			# items only for given default supplier
			supplier_items = []
			for d in target_doc.items:
				default_supplier = get_item_defaults(d.item_code, target_doc.company).get("default_supplier")
				if frappe.flags.args.default_supplier == default_supplier:
					supplier_items.append(d)
			target_doc.items = supplier_items

		set_missing_values(source, target_doc)

	def select_item(d):
		filtered_items = args.get("filtered_children", [])
		child_filter = d.name in filtered_items if filtered_items else True

		return d.ordered_qty < d.stock_qty and child_filter

	doclist = get_mapped_doc(
		"Material Request",
		source_name,
		{
			"Material Request": {
				"doctype": "Purchase Order",
				"validation": {"docstatus": ["=", 1], "material_request_type": ["=", "Purchase"]},
			},
			"Material Request Item": {
				"doctype": "Purchase Order Item",
				"field_map": [
					["name", "material_request_item"],
					["parent", "material_request"],
					["uom", "stock_uom"],
					["uom", "uom"],
					["sales_order", "sales_order"],
					["sales_order_item", "sales_order_item"],
					["wip_composite_asset", "wip_composite_asset"],
				],
				"postprocess": update_item,
				"condition": select_item,
			},
		},
		target_doc,
		postprocess,
	)

	return doclist