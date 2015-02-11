from Products.Five.browser import BrowserView
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from Products.CMFPlone.utils import safe_unicode


from plone import api


class GetThemeId(BrowserView):

    def __call__(self):
        owner = self.context.getOwner()
        themeId = safe_unicode(owner.getProperty('blogTheme', 'porto'))
        return themeId 
