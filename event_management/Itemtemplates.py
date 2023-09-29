@frappe.whitelist()
def get_quotation_template(name):

    try:
        doc = frappe.get_doc('Quotation Item Template', name)
    except Exception as e:
        doc = None
    return doc
    
@frappe.whitelist()
def get_salesorder_template(name):

    try:
        doc = frappe.get_doc('Sales order template', name)
    except Exception as e:
        doc = None
    return doc 
