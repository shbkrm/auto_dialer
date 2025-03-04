frappe.pages['auto-dialer'].on_page_load = function(wrapper) {
    var page = frappe.ui.make_app_page({
        parent: wrapper,
        title: 'Auto Dialer',
        single_column: true
    });

    page.add_action_item(__('Start Auto Dialer'), function() {
        frappe.call({
            method: "auto_dialer.api.start_dialing",
            callback: function(response) {
                frappe.msgprint(response.message || "Auto Dialer Started!");
            }
        });
    });

    let $table = $(`<table class="table">
                        <thead><tr><th>Lead</th><th>Phone</th><th>Status</th></tr></thead>
                        <tbody id="lead-queue"></tbody>
                    </table>`).appendTo(page.body);

    frappe.call({
        method: "auto_dialer.api.get_lead_queue",
        callback: function(response) {
            let leads = response.message;
            leads.forEach(lead => {
                $("#lead-queue").append(`<tr data-phone="${lead.phone}">
                                            <td>${lead.lead_name}</td>
                                            <td>${lead.phone}</td>
                                            <td class="call-status">Pending</td>
                                        </tr>`);
            });
        }
    });
};
