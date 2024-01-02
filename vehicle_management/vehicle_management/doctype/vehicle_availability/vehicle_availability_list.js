frappe.listview_settings['Vehicle Availability']={
    get_indicator(doc){
        if (doc.docstatus==1 && doc.status=="To Price") {
            return [__("To Price"), "purple", "status,=,To Price"];
          }
        else if (doc.docstatus==1 && doc.status=="Completed") {
            return [__("Completed"), "green", "status,=,Completed"];
          }
    }
}