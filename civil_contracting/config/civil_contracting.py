from __future__ import unicode_literals
from frappe import _

def get_data():
    return [
        {
            "label":_("Worker Section"),
            "icon": "octicon octicon-briefcase",
            "items": [
                {
                "type": "doctype",
                "name": "Worker",
                "label": _("Worker"),
                },
                {
                "type": "doctype",
                "name": "Worker Sheet",
                "label": _("Worker Sheet"),
                },
                {
                "type": "doctype",
                "name": "Wage Slip",
                "label": _("Wage Slip"),
                }
            ]
        },
        {
            "label":_("Measurement Section"),
            "icon": "octicon octicon-briefcase",
            "items": [
                {
                    "type": "doctype",
                    "name": "Measurement Sheet",
                    "label": _("Measurement Sheet"),
                },
                {
                    "type": "doctype",
                    "name": "Measurement Book",
                    "label": _("Measurement Book"),
                },
                    {
                    "type": "doctype",
                    "name": "Running Account Bill",
                    "label": _("Running Account Bill"),
                }
            ]
        },
        {
            "label":_("Settings Section"),
            "icon": "octicon octicon-briefcase",
            "items": [
                {
                "type": "doctype",
                "name": "Worker Sheet Settings",
                "label": _("Worker Sheet Settings"),
                }
            ]
        },
  ]


           