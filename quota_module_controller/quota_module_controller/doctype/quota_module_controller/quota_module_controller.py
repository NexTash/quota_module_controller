# Copyright (c) 2023, NexTash and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
import uuid
import requests


class QuotaModuleController(Document):
    def validate(self):
        # Generate a random UUID
        unique_id = uuid.uuid4()
        # Format the UUID to create the license key
        license_key = str(unique_id).replace("-", "")[:16]

        if not self.license_key: 
            self.license_key = license_key
    
    @frappe.whitelist()
    def deploy(self):
        
        # Set the API endpoint URL
        url = f"{self.site_url}/api/method/quota_module_client.api.verify_license"
        data = {"license_key": self.license_key}
        # Make the API request and store the response in a variable
        response = requests.get(url, data=data)

        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            # Print the response content
            frappe.msgprint("Triggerd!")
        else:
            # Print an error message if the request failed
            frappe.throw(f"Error {response.status_code}: {response.json()}")
        return 0
