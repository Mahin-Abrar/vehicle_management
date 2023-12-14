// Copyright (c) 2023, Mahin Abrar and contributors
// For license information, please see license.txt

frappe.ui.form.on('Vehicle Price', {
	

	company_price:function(frm){
		
	let companyPrice=frm.doc.company_price;
	let customerPrice=frm.doc.customer_price;
	let salePrice=companyPrice+customerPrice;
	frm.set_value({'sale_price' :salePrice});	
	},
	customer_price:calculators(frm)
	
});
function calculators(frm){
	let companyPrice=frm.doc.company_price;
		let customerPrice=frm.doc.customer_price;
		let salePrice=companyPrice+customerPrice;
		frm.set_value({'sale_price':salePrice});	
}



