@frappe.whitelist(allow_guest=True)
def call_status_update():
    data = frappe.request.get_json()
    phone_number = data.get("phone")
    call_status = data.get("status")

    lead = frappe.get_value("Lead", {"phone": phone_number}, "name")

    if lead:
        frappe.db.set_value("Lead", lead, "call_status", call_status)
        frappe.db.commit()

    return {"success": True}
