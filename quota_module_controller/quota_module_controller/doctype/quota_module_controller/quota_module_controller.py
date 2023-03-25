# Copyright (c) 2023, NexTash and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document
import uuid


class QuotaModuleController(Document):
    def validate(self):
        # Generate a random UUID
        unique_id = uuid.uuid4()

        # Format the UUID to create the license key
        license_key = str(unique_id).replace("-", "")[:16]

        self.license_key = license_key
    
    @frappe.whitelist()
    def deploy(self):
        
        # Set the API endpoint URL
        url = f"https://{self.url}/api/method/quota_module_client.api.verify_license"

        # Make the API request and store the response in a variable
        response = requests.get(url)

        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            # Print the response content
            frappe.msgprint("Triggerd!")
        else:
            # Print an error message if the request failed
            frappe.throw(f"Error {response.status_code}: {response.json()['message']}")
        return 0
