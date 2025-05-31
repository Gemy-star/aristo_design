# -*- coding: utf-8 -*-

"""
Custom context processors
"""
from main.models import Announcement , AboutPage

def portal_data(request):
    """Define common context variables to be used in views/templates"""
    announcements = Announcement.objects.all().order_by('-date')[:3]
    about = AboutPage.get_instance()
    ctx = {"announcements": announcements , 'about': about}
    return ctx
