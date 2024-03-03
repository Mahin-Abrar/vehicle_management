frappe.views.calendar["Task"] = {
	field_map: {
		"start": "exp_start_date",
		"end": "exp_end_date",
		"id": "name",
		"title": "subject",
		"allDay": "allDay",
		"progress": "progress",
	},
	gantt: true,
	// filters: [
	// 	{
	// 		"fieldtype": "Link",
	// 		"fieldname": "project",
	// 		"options": "Project",
	// 		"label": __("Project")
	// 	}
	// ],
    get_events_method: "vehicle_management.overrides.projects.task.calendar.get_events",
}

// frappe.views.calendar["Task"] = {
// 	field_map: {
// 		"start": "holiday_date",
// 		"end": "holiday_date",
// 		"id": "name",
// 		"title": "description",
// 		"allDay": "allDay"
// 	},
// 	order_by: `from_date`,
// 	get_events_method: "erpnext.setup.doctype.holiday_list.holiday_list.get_events",
// 	filters: [
// 		{
// 			'fieldtype': 'Link',
// 			'fieldname': 'holiday_list',
// 			'options': 'Holiday List',
// 			'label': __('Holiday List')
// 		}
// 	]
// }

// frappe.views.calendar['Task'] = {
//     field_map: {
//         "start": "exp_start_date",
// 		"end": "exp_end_date",
// 		"title": "subject",
// 		"eventColor": "color"
// 	},
//     gantt: true,
   
// 	get_events_method: 'vehicle_management.overrides.projects.task.calendar.get_events',
// }