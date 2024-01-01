// // green, cyan, blue, orange, yellow, gray, grey, red, pink, darkgrey, purple, light-blue
frappe.listview_settings['Vehicle Details'] = {
    get_indicator(doc){
      let field = doc.status;
        if (doc.status=="Completed") {
			return [__(field), "cyan", "status,=,Completed"];
        }
  }
};

// p_key=frappe.db.get_list('Vehicle Availability',filters={
//   docstatus:1,
//   },pluck='name')
// doc2=frappe.get_doc('Vehicle Availability',p_key)
// console.log(doc2.docstatus)
// doc2.save()