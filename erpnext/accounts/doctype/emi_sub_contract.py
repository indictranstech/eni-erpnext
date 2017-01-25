from __future__ import unicode_literals
import frappe, json
from frappe.utils import cstr, flt, fmt_money, formatdate
from frappe import msgprint, _, scrub
from frappe.utils import flt, getdate, add_to_date

def get_sub_contract_entry(doc, method):
	if doc.purpose=="Subcontract":
		se = frappe.new_doc("Stock Entry")
		se.update({
			"purpose": "Material Receipt",
			"company": doc.company,
			"posting_date": doc.posting_date,
			"to_warehouse":doc.to_warehouse
		})
		se.flags.ignore_mandatory = True		
		bom_no = frappe.db.get_value("BOM", doc.bom_no, "item_name")
		for i in doc.items:
			qty = i.qty
		se.append("items", {
		"item_code": bom_no,
		"qty": qty,
		"uom":"Nos"
		})
		se.docstatus=1
		se.save()
