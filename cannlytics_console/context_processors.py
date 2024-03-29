"""
General Utility Functions
Author: Keegan Skeate
Contact: <keegan@cannlytics.com>
Created: 4/26/2021
"""

from django.conf import settings


def selected_settings(request):
    """Include relevant settings in the context."""
    return {
        'APP_VERSION_NUMBER': settings.APP_VERSION_NUMBER
    }
