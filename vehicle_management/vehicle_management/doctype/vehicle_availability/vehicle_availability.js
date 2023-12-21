// Copyright (c) 2023, Mahin Abrar and contributors
// For license information, please see license.txt

frappe.ui.form.on('Vehicle Availability', {
		status: function(frm){
                frm.set_value({'ship_details':'','in_house_address':'','port_location':'','shed_number':'','workshop_address':'','other':''});
		},
		onload:function(frm){
			frm.set_query("vehicle_chassis_no", function() {
				return {
					"filters": {
						is_sold:false
					}
				};
			});
		}
});