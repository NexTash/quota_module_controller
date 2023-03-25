import frappe
from frappe import request, _
from frappe.utils import get_site_name


@frappe.whitelist(allow_guest=True)
def verify_license(license_key=None):
    if not license_key:
        return
        
    sites = frappe.get_all("Quota Module Controller", {
                           "license_key": license_key}, ["site_url", "name"])
    url = sites[0].site_url if len(sites[0]) else "https://example.com"
    domain = request.headers.get("X-Frappe-Site-Name") or request.host

    url = get_site_name(url)
    domain = get_site_name(domain)

    if url != domain:
        frappe.local.response.http_status_code = 403
        return _("This License key doesn't exists or the your site url not registered for it")
    else:
        doc = frappe.get_doc("Quota Module Controller", sites[0].name)
        return {
            "verification": True,
            "users": doc.allowed_users,
            "company": doc.allowed_companies,
            "space": doc.allowed_storage_spacemb,
            "db_space": doc.allowed_database_spacemb,
            "valid_till": doc.site_expiry_date,
        }
