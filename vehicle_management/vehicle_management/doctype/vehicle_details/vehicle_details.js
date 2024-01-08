// Copyright (c) 2023, Mahin Abrar and contributors
// For license information, please see license.txt


frappe.ui.form.on('Vehicle Details', {
    refresh: function(frm) {
		if (frm.doc.docstatus==1){
        frm.add_custom_button(__("Create"), function() {
			let newDoc = frappe.new_doc('Vehicle Availability');
            frappe.set_route('Form', 'Vehicle Availability', newDoc.doc.name);
			let teste=frappe.db.get_value("Vehicle Availability", newDoc.doc.name,"status")
			console.log(teste);
        },__("Create")).css({'background-color': 'white', 'color': 'black'});
		}
	}
});