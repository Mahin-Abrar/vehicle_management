// Copyright (c) 2023, Mahin Abrar and contributors
// For license information, please see license.txt

frappe.ui.form.on('Vehicle Price', {
    company_price: function (frm) {
        calculatePrices(frm);
        updateTotalAmount(frm);
        grandTotal (frm);
    },
    is_sold: function (frm) {
        frm.set_value({'customer':''});
    },
    customer_price: function (frm) {
        calculatePrices(frm);
        updateTotalAmount(frm);
        grandTotal (frm);
    },
    sale_price: function (frm) {
        grandTotal (frm);
    },
    before_save: function (frm){
        checkValue (frm);
    },
    onload:function(frm){
        filtering (frm);
    },
    vehicle_chassis_no: function(frm) {
        var chassisNo = frm.doc.vehicle_chassis_no;

        // Check if chassis number exists in Vehicle Availability doctype
        frappe.call({
            method: 'vehicle_management.vehicle_management.doctype.vehicle_price.vehicle_price.check_vehicle_availability',
            args: {
                chassis_no: chassisNo
            },
            callback: function(response) {
                if (!response.message==1){
                    frm.set_value({'vehicle_chassis_no':''})
                    frappe.throw("Duplicate found in Vehicle Availability or Not available in Vehicle Availability");
                }
            }
        });
    }
});

//calculation for the child table
frappe.ui.form.on('Other Vehicle Items',{
    quantity: function(frm, cdt, cdn) {
        amount_child(frm, cdt, cdn);
        updateTotalAmount(frm);
        grandTotal (frm);
    },
    rate: function(frm, cdt, cdn) {
        amount_child(frm, cdt, cdn);
        updateTotalAmount(frm);
        grandTotal (frm);
    },
    item: function (frm, cdt, cdn) {
		amount_child(frm, cdt, cdn);
        duplicateFinder(frm,cdt,cdn);
        updateTotalAmount(frm);
        grandTotal (frm);
    },
    other_vehicle_items_remove: function (frm) {
        updateTotalAmount(frm);
        grandTotal (frm);
    }
});

// functions
//functoin for query
function filtering(frm) {
    frm.set_query("vehicle_chassis_no", function() {

        return {
            "filters": {
                is_sold:false,
            }
        };
    });
}
//value check
function checkValue(frm){
    let grandValue=frm.doc.grand_total
    if(grandValue==0.00){
        frappe.throw("Invalid grand total value")
    }
}
// calculation for the sale price
function calculatePrices(frm) {
    let companyPrice = frm.doc.company_price || 0;
    let customerPrice = frm.doc.customer_price || 0;
    let salePrice = companyPrice + customerPrice;
    frm.set_value('sale_price', salePrice);
}

// calculation for the child tabel price calculation
function amount_child(frm, cdt, cdn) {
    let item = locals[cdt][cdn];
    let qty = item.quantity || 0;
    let rate = item.rate || 0;
    let amount = qty*rate;

    frappe.model.set_value(cdt, cdn, 'amount', amount);
    frm.refresh_field('other_vehicle_items');
}
//duplicate
function duplicateFinder (frm,cdt, cdn){
    var existingValues = [];
    var currentRow = locals[cdt][cdn];

    // Iterate through the child table rows
    frm.doc.other_vehicle_items.forEach(function (row) {
        let fieldValue = row.item;

        if (existingValues.indexOf(fieldValue) !== -1) {
            // Clear the field value if a duplicate is found
            frappe.model.set_value(currentRow.doctype, currentRow.name, 'item', '');
            frappe.throw(__('Duplicate value in child table: {0}. Field cleared.', [fieldValue]));
        } 
        existingValues.push(fieldValue);
        
    });
}
//total calculation
function updateTotalAmount(frm) {
    let totalAmount = 0;
	let totalQuantity = 0;
    frm.doc.other_vehicle_items.forEach(function (row) {
        totalAmount += row.amount;
		totalQuantity += row.quantity;
    });
    frm.set_value('item_amount', totalAmount);
	frm.set_value('total_quantity', totalQuantity);
}
/// Grand total
function grandTotal (frm) {
    let salePrice = frm.doc.sale_price || 0;
    let otherTotal = frm.doc.item_amount || 0;
    let grand = salePrice + otherTotal;
    frm.set_value('grand_total', grand);
}