// Copyright (c) 2023, Mahin Abrar and contributors
// For license information, please see license.txt
frappe.ui.form.on('Vehicle Price', {
    company_price: function (frm) {
        calculatePrices(frm);
    },
    customer_price: function (frm) {
        calculatePrices(frm);
    }
});

function calculatePrices(frm) {
    let companyPrice = frm.doc.company_price || 0;
    let customerPrice = frm.doc.customer_price || 0;
    let salePrice = companyPrice + customerPrice;
    frm.set_value('sale_price', salePrice);
}