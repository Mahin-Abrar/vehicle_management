// green, cyan, blue, orange, yellow, gray, grey, red, pink, darkgrey, purple, light-blue
frappe.listview_settings['Vehicle Details'] = {
    // add_fields:["status"],
    get_indicator(doc){
      // console.log(doc)
        if (doc.docstatus == 1) {
			return [__("To Availability & Price"), "pink"];
  //   } else if(doc.docstatus ==0){
  //     return [__("To Price"), "pink"];
  // }else if(doc.docstatus ==-1){
  //   return [__("To Availability & Price"), "pink"];
  // }
}
}
};