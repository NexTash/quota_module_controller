import frappe
from frappe import request, _
from frappe.utils import get_site_name
from urllib.parse import urlparse

@frappe.whitelist(allow_guest=True)
def verify_license(license_key=None, domain= None):
    if not license_key or not domain:
        return

    sites = frappe.get_all("Quota Module Controller", {"license_key": license_key}, ["site_url", "name"])
    url = sites[0].site_url if len(sites) else "https://example.com"

    url = get_site_name(urlparse(url).hostname)
    
    if url != domain:
        frappe.local.response.http_status_code = 403
        return _(f"This License key doesn't exists or the your site url not registered for it")
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
