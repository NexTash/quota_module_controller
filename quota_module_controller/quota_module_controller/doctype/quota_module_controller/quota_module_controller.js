// Copyright (c) 2023, NexTash and contributors
// For license information, please see license.txt

frappe.ui.form.on('Quota Module Controller', {
	refresh: function(frm) {
		if (!frm.is_dirty()) {
			let label = __('Trigger Changes');
			frm.add_custom_button(label, () =>
				frm.call('deploy')
			);
		}
	}
});
