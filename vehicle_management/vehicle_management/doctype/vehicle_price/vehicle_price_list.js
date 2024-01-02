// // green, cyan, blue, orange, yellow, gray, grey, red, pink, darkgrey, purple, light-blue
frappe.listview_settings['Vehicle Price']={
    get_indicator(doc){
        if (doc.docstatus==1 && doc.status=="Sold"){
            return [__("Sold"), "cyan","status,=,Sold"];
          }else if (doc.status=="Un Sold"){
            return [__("Un Sold"), "orange","status,=,Un Sold"];
        }
    }
}