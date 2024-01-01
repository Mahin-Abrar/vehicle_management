frappe.listview_settings['Vehicle Price']={
    get_indicator(doc){
        if (doc.is_sold==1){
            return [__("Sold"), "purple"];
          }
        // else if (doc.docstatus==1 && doc.is_sold== 1) {
        //     return [__("Sold"), "green", "status,=,Sold"];
        //   }
    }
}