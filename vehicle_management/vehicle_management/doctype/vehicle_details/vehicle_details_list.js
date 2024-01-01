// // green, cyan, blue, orange, yellow, gray, grey, red, pink, darkgrey, purple, light-blue
frappe.listview_settings['Vehicle Details'] = {
    get_indicator(doc){
      if (doc.docstatus==1 && doc.status=="To Availability & Price") {
        return [__("To Availability & Price"), "cyan", "status,=,To Availability & Price"];
      }
      else if (doc.docstatus==1 && doc.status=="To Price") {
        return [__("To Price"), "purple", "status,=,To Price"];
      }
      else if (doc.docstatus==1 && doc.status=="Completed") {
        return [__("Completed"), "green", "status,=,Completed"];
      }
  }
};

// p_key=frappe.db.get_list('Vehicle Availability',filters={
//   docstatus:1,
//   },pluck='name')
// doc2=frappe.get_doc('Vehicle Availability',p_key)
// console.log(doc2.docstatus)
// doc2.save()
// if (doc.status=="To Availability & Price") {
//   return [__(field), "cyan", "status,=,To Availability & Price"];
// }
// else if (doc.status=="To Price") {
//   return [__(field), "purple", "status,=,To Price"];
// }
// if (doc.status=="Completed") {
//   return [__(field), "green", "status,=,Completed"];
//         }