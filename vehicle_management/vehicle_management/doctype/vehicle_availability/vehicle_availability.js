// Copyright (c) 2023, Mahin Abrar and contributors
// For license information, please see license.txt

frappe.ui.form.on('Vehicle Availability', {
		vehicle_status: function(frm){
                frm.set_value({'ship_details':'','in_house_address':'','port_location':'','shed_number':'','workshop_address':'','other':''});
		},
		onload:function(frm){
			settingQuery(frm)
		},
		refresh: function(frm) {
			if (frm.doc.docstatus==1){
				frm.add_custom_button(__('Vehicle Price'), 
				() => make_vehicle_price(frm), 
				__("Create"));
				cur_frm.page.set_inner_btn_group_as_primary(__("Create"));
			  }
			if(frm.doc.docstatus==0){
				frm.add_custom_button(__('Vehicle Details'), function(){
					d.show();
				}, __("Get Items From"));
			}
		}

});

let d = new frappe.ui.Dialog({
    title: 'Enter details',
    fields: [
        {
            label: 'First Name',
            fieldname: 'first_name',
            fieldtype: 'Data'
        },
        {
            label: 'Last Name',
            fieldname: 'last_name',
            fieldtype: 'Data'
        },
        {
            label: 'Age',
            fieldname: 'age',
            fieldtype: 'Int'
        }
    ],
    size: 'small', // small, large, extra-large 
    primary_action_label: 'Submit',
    primary_action(values) {
        console.log(values);
        d.hide();
    }
});



let make_vehicle_price = (frm) => {
	return frappe.call({
        method: "vehicle_management.vehicle_management.doctype.vehicle_availability.vehicle_availability.make_vehicle_price",
        freeze: true,
        freeze_message: __("Creating Vehicle Price ..."),
        args: {
            source_name: frm.doc.name,
        },
        freeze: true,
        callback: function (r) {
            if (!r.exc) {
                frappe.model.sync(r.message);
                frappe.set_route("Form",r.message.doctype, r.message.name);
            }
        },
    });
}

function settingQuery(frm) {
	frm.set_query("vehicle_chassis_no", function() {
		return {
			"filters": {
				is_sold:false,
				docstatus:1
			}
		};
	});
}