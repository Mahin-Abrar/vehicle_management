# Status Work-Flow

1.Create a dropdown “Status” field in all the 3 Doctypes.
Vehicle Details contains - To Availability & Price , To Price, Completed
Vehicle Availability contains - To Price, Completed
Vehicle Price contains - Sold, Unsold

2.Keep the status Field hidden & allow on submit.

3.In Vehicle Details “on_submit” change the status for the Vehicle Details “ Status “ field to “To Availability & Price”.

4.In Vehicle Availability “on_submit” change the status field to “To Price” and using backend code change the status for the Vehicle Details “Status” field to “To Price”.

5.In Vehicle Price if is_sold==1 “on_submit” change the status field to “Sold” else “UnSold” and change the field “Status” for Vehicle Details and Vehicle Availability to completed.

6.For cancellation in any doctype, reverse the “Status” to their previous “Status” according to the flow.

7.In the vehicle_details_list.js , vehicle_availability_list.js and vehicle_price_list.js
using the “get_indicator” function to customise the indicator and implement the filter.

## get_incicator function for vehicle details list

E.g for the vehicle_details_list doctype the code is illustrated below .

frappe.listview_settings['Vehicle Details'] = {

get_indicator(doc){

if (doc.status=="To Availability & Price") {

return [__("To Availability & Price"), "yellow", "status,=,To Availability & Price"];

}
else if (doc.status=="To Price") {

return [__("To Price"), "purple", "status,=,To Price"];
}
}
}
