@frappe.whitelist()
def get_quotation_templlat(name):

    try:
        doc = frappe.get_doc('Quotation Item Template', name)
    except Exception as e:
        doc = None
    return doc
    
