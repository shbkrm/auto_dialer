import frappe
import requests

@frappe.whitelist()
def get_lead_queue():
    return frappe.get_all("Lead", filters={"status": "Open"}, fields=["name as lead_name", "phone"])

@frappe.whitelist()
def start_dialing():
    leads = frappe.get_all("Lead", filters={"status": "Open"}, fields=["name", "phone"])
    
    for lead in leads:
        call_response = initiate_call(lead["phone"])
        if call_response.get("success"):
            frappe.db.set_value("Lead", lead["name"], "call_status", "Calling")
            frappe.db.commit()

    return "Auto Dialer Completed!"

def initiate_call(phone_number):
    api_url = "https://smartflo.tatateleservices.com/api/call"
    headers = {"Authorization": "Bearer YOUR_ACCESS_TOKEN"}
    payload = {"phone": phone_number, "caller_id": "YOUR_REGISTERED_NUMBER"}
    
    response = requests.post(api_url, json=payload, headers=headers)
    
    return {"success": response.status_code == 200}
