// frappe.listview_settings['Vehicle Availabiltiy'] = {
//     get_indicator(doc){
//       let field = doc.status;
//         if (field) {
// 			return [__(field), "cyan"];
//         }
//   }
// };
frappe.listview_settings['Vehicle Availability']={
    get_indicator(doc){
        let tempor=doc.status;
          if (tempor) {
              return [__(tempor), "grey"];
          }
    }
}