// // green, cyan, blue, orange, yellow, gray, grey, red, pink, darkgrey, purple, light-blue
frappe.listview_settings['Vehicle Details'] = {
    get_indicator(doc){
      if (doc.status=="To Availability & Price") {
        return [__("To Availability & Price"), "yellow", "status,=,To Availability & Price"];
      }
      else if (doc.status=="To Price") {
        return [__("To Price"), "purple", "status,=,To Price"];
      }
      else if (doc.status=="Completed") {
        return [__("Completed"), "green", "status,=,Completed"];
      }else if (doc.status==""){
        return [__("Cancelled"), "red", "status,=,Cancelled"];
      }
  }
};