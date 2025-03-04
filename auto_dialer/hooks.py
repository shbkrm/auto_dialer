app_name = "auto_dialer"
app_title = "Auto Dialer"
app_publisher = "Your Name"
app_description = "Auto Dialer for ERPNext using Tata Smartflo"
app_email = "your_email@example.com"
app_license = "MIT"

# Includes in <head>
app_include_js = "/assets/auto_dialer/js/auto_dialer.js"
app_include_css = "/assets/auto_dialer/css/auto_dialer.css"

# Scheduled Tasks (if needed)
scheduler_events = {
    "all": ["auto_dialer.api.start_dialing"]
}

# Webhooks for Tata Smartflo call updates
webhooks = [
    {
        "webhook_doctype": "Lead",
        "webhook_docevent": "on_update",
        "webhook_url": "/api/method/auto_dialer.webhooks.call_status_update",
        "request_method": "POST",
        "headers": {"Content-Type": "application/json"},
    }
]
