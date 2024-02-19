// Copyright (c) 2023, Mahin Abrar and contributors
// For license information, please see license.txt

frappe.ui.form.on('Vehicle Availability', {
    vehicle_status: function (frm) {
        frm.set_value({'ship_details': '', 'in_house_address': '', 'port_location': '', 'shed_number': '', 'workshop_address': '', 'other': ''});
    },
    onload: function (frm) {
        settingQuery(frm);
    },
    refresh: function (frm) {
        if (frm.doc.docstatus == 1) {
            frm.add_custom_button(__('Vehicle Price'),
                () => make_vehicle_price(frm),
                __("Create"));
            cur_frm.page.set_inner_btn_group_as_primary(__("Create"));
        };
        if (frm.doc.docstatus == 0) {
            frm.add_custom_button(__('Vehicle Details'), () => {
                clearField(frm);
                setTimeout(() => make_vehicle_availability(frm), 250);
            }, __("Get Items From"));
        }
    }
});

let make_vehicle_availability = (frm) => {
    
    erpnext.utils.map_current_doc({
        method: "vehicle_management.vehicle_management.doctype.vehicle_details.vehicle_details.make_vehicle_availability",
        source_doctype: "Vehicle Details",
        target: frm,
        setters: {
        //    "chassis_number": cur_frm.doc.vehicle_chassis_no
        },
        get_query_filters: {
            docstatus: 1,
            status:"To Availability & Price",
            is_sold: 0,
        },
    });
}


let clearField=(frm)=>{
    frm.set_value({'vehicle_chassis_no':""});
}

 



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