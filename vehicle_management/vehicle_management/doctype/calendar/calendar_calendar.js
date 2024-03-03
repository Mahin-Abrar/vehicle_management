frappe.views.calendar['Calendar'] = {
    field_map: {
        "start": "exp_start_date",
		"end": "exp_end_date",
		"title": "subject",
		"eventColor": "color"
	},
    gantt: true,
   
	get_events_method: 'vehicle_management.vehicle_management.doctype.calendar.calendar.get_events',
}
    // field_map:  {
	// 	"start": "exp_start_date",
	// 	"end": "exp_end_date",
	// 	"id": "name",
	// 	"title": "subject",
	// 	"allDay": "allDay",
	// 	"progress": "progress"
	// },
    // gantt: true,
	// filters: [
	// 	{
	// 		"fieldtype": "Link",
	// 		"fieldname": "project",
	// 		"options": "Project",
	// 		"label": __("Project")
	// 	}
	// ],
    // get_events_method: 'vehicle_management.vehicle_management.doctype.calendar.calendar.get_events'
