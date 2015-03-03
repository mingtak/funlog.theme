from Products.Five.browser import BrowserView
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from Products.CMFPlone.utils import safe_unicode


from plone import api


class GetThemeId(BrowserView):

    def __call__(self):
        ownerId = self.context.owner_info()["id"]
        catalog = self.context.portal_catalog
        profile = catalog({"Creator":ownerId, "Type":"Profile"})[0]
        return profile.blogTheme


class GetContentType(BrowserView):

    def __call__(self):
        return self.context.Type()

class IsOwner(BrowserView):

    def __call__(self):
        ownerId = self.context.owner_info()["id"]
        currentUser = api.user.get_current().id
        return (ownerId == currentUser)
