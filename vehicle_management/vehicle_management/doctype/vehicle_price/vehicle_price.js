// Copyright (c) 2023, Mahin Abrar and contributors
// For license information, please see license.txt
frappe.ui.form.on('Vehicle Price', {
    company_price: function (frm) {
        calculatePrices(frm);
    },
    customer_price: function (frm) {
        calculatePrices(frm);
    },
	
});
//calculation for the chil table
frappe.ui.form.on('Other Vehicle Items', {
    quantity: function(frm, cdt, cdn) {
        amount_child(frm, cdt, cdn);
    },
    rate: function(frm, cdt, cdn) {
        amount_child(frm, cdt, cdn);
    },
	item: function(frm, cdt, cdn) {
		$.each(locals[cdt][cdn].other_vehicle_items, function(row) {
			if (row.item === cdt.item) {
				frappe.throw('console')
				frappe.model.delete_doc(cdt, cdn);
				frm.refresh_field('other_vehicle_items');
				return false;
			}
		});
	}
});


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
    let amount = qty * rate;

    frappe.model.set_value(cdt, cdn, 'amount', amount);
    frm.refresh_field('other_vehicle_items');
}