
// Copyright (c) 2023, Mahin Abrar and contributors
// For license information, please see license.txt



frappe.ui.form.on('Vehicle Details', {
    refresh: function(frm) {
		if (frm.doc.docstatus==1){
			frm.add_custom_button(__('Vehicle Availability'), 
			() => make_vehicle_availability(frm), 
			__("Create"));
			cur_frm.page.set_inner_btn_group_as_primary(__("Create"));
		  }
		},
});

frappe.ui.form.ControlLink.link_options = function(link) {
    // if (link.df.fieldname === "car_model") {
        return [
            {
                html: "<span class='text-primary link-option'>"
                    + "<i class='fa fa-car' style='margin-right: 5px;'></i> "
                    + __("Need for pinik?")
                    + "</span>",
                label: __("Custom Link Option"),
                value: "custom__link_option",
                action: () => {
                    frappe.msgprint("pinik Happened!");
                }
            }
        ];
    
};



let make_vehicle_availability = (frm) => {
	return frappe.call({
        method: "vehicle_management.vehicle_management.doctype.vehicle_details.vehicle_details.make_vehicle_availability",
        freeze: true,
        freeze_message: __("Creating Vehicle Availability ..."),
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

// function next_doc (frm) {
// 	frappe.call({
// 		method: 'vehicle_management.vehicle_management.doctype.vehicle_details.vehicle_details.make_vehicle_availability',
// 		args: {
// 			source_name: frm.doc.chassis_no
// 		},
// 		callback: function(response) {
// 			console.log(response);
// 			frm.set_value({'vehicle_chassis_no':response.message.vehicle_chassis_no})
// 		}
// 	});
// }