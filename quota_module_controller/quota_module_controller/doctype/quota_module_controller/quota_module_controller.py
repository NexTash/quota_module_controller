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
