frappe.ui.form.on('Material Request', {


});

frappe.ui.form.on('Material Request Item', {
    rate:function(frm,cdt,cdn){
        amount_child(frm, cdt, cdn)
        updateTotalAmount(frm) 
    },
    qty:function(frm,cdt,cdn){
        amount_child(frm, cdt, cdn)
        updateTotalAmount(frm) 
    }
})





function amount_child(frm, cdt, cdn) {
    let item = locals[cdt][cdn];
    let qty = item.qty || 0;
    let rate = item.rate || 0;
    let amount = qty*rate;

    frappe.model.set_value(cdt, cdn, 'amount', amount);
}


function updateTotalAmount(frm) {
    let totalAmount = 0;
	let totalQuantity = 0;
    frm.doc.items.forEach(function (row) {
        totalAmount += row.amount;
		totalQuantity += row.qty;
    });
    frm.set_value('total_quantity', totalQuantity);
	frm.set_value('sum_amount',totalAmount);
}