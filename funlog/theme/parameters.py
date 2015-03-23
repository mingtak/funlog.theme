from Products.Five.browser import BrowserView
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from Products.CMFPlone.utils import safe_unicode

from plone import api


class IsSystemPage(BrowserView):

    def __call__(self):
        ownerId = self.context.owner_info()["id"]
#        import pdb; pdb.set_trace()
        if 'Manager' in api.user.get_roles(username=ownerId):
            self.isSystemPage = True
        else:
            self.isSystemPage = False
        return self.isSystemPage


class GetThemeId(BrowserView):

    def __call__(self):
        ownerId = self.context.owner_info()["id"]
        if 'Manager' in api.user.get_roles(username=ownerId):
            return u'system'
        catalog = self.context.portal_catalog
        profile = catalog({"Creator":ownerId, "Type":"Profile"})
        if len(profile) == 0:
            return u'default'
        return profile[0].blogTheme


class GetContentType(BrowserView):

    def __call__(self):
        return self.context.Type()

class IsOwner(BrowserView):

    def __call__(self):
        ownerId = self.context.owner_info()["id"]
        currentUser = api.user.get_current().id
        return (ownerId == currentUser)
