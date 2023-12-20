// Copyright (c) 2023, Mahin Abrar and contributors
// For license information, please see license.txt

frappe.ui.form.on('Vehicle Availability', {
		status: function(frm){
                frm.set_value({'ship_details':'','in_house_address':'','port_location':'','shed_number':'','workshop_address':'','other':''});
		},
		vehicle_chassis_no:function(frm){
			cur_frm.vehicle_chassis_no['Vehicle Details'].get_query = function(frm) {
				return {
					filters: {
						'is_sold':'false'
					}
				}
			}
			// frm.set_query('vehicle_chassis_no', () => {
			// 	return {
			// 		filters: {
						
			// 		}
			// 	}
			// })	
		}
});