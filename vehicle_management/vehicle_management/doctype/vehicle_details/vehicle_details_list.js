frappe.listview_settings['Vehicle Details'] = {
    add_fields:["status"],
    get_indicator(doc){
        if (doc.status == "Draft") {
			return [__("Submitted"), "green", "status,=,Submitted"];
    }
  }
};