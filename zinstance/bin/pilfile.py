#!/home/cryo/Plone/Python-2.7/bin/python
#
# The Python Imaging Library.
# $Id$
#
# a utility to identify image files
#
# this script identifies image files, extracting size and
# pixel mode information for known file formats.  Note that
# you don't need the PIL C extension to use this module.
#
# History:
# 0.0 1995-09-01 fl   Created
# 0.1 1996-05-18 fl   Modified options, added debugging mode
# 0.2 1996-12-29 fl   Added verify mode
# 0.3 1999-06-05 fl   Don't mess up on class exceptions (1.5.2 and later)
# 0.4 2003-09-30 fl   Expand wildcards on Windows; robustness tweaks
#

from __future__ import print_function



import sys
sys.path[0:0] = [
  '/home/cryo/Plone/buildout-cache/eggs/Plone-4.3.3-py2.7.egg',
  '/home/cryo/Plone/buildout-cache/eggs/Pillow-2.3.0-py2.7-linux-i686.egg',
  '/home/cryo/Plone/buildout-cache/eggs/Products.PloneFormGen-1.7.14-py2.7.egg',
  '/home/cryo/Plone/buildout-cache/eggs/collective.js.jqueryui-1.10.3-py2.7.egg',
  '/home/cryo/Plone/buildout-cache/eggs/plone.app.jquerytools-1.5.7-py2.7.egg',
  '/home/cryo/Plone/buildout-cache/eggs/Products.PythonField-1.1.3-py2.7.egg',
  '/home/cryo/Plone/buildout-cache/eggs/Products.TemplateFields-1.2.5-py2.7.egg',
  '/home/cryo/Plone/buildout-cache/eggs/Products.TALESField-1.1.3-py2.7.egg',
  '/home/cryo/Plone/buildout-cache/eggs/Products.CMFPlone-4.3.3-py2.7.egg',
  '/home/cryo/Plone/buildout-cache/eggs/Products.Archetypes-1.9.7-py2.7.egg',
  '/home/cryo/Plone/buildout-cache/eggs/setuptools-0.7.2-py2.7.egg',
  '/home/cryo/Plone/buildout-cache/eggs/wicked-1.1.10-py2.7.egg',
  '/home/cryo/Plone/buildout-cache/eggs/plone.app.theming-1.1.1-py2.7.egg',
  '/home/cryo/Plone/buildout-cache/eggs/plone.app.openid-2.0.2-py2.7.egg',
  '/home/cryo/Plone/buildout-cache/eggs/plone.app.iterate-2.1.12-py2.7.egg',
  '/home/cryo/Plone/buildout-cache/eggs/plone.app.dexterity-2.0.11-py2.7.egg',
  '/home/cryo/Plone/buildout-cache/eggs/plone.app.caching-1.1.8-py2.7.egg',
  '/home/cryo/Plone/buildout-cache/eggs/Products.CMFPlacefulWorkflow-1.5.10-py2.7.egg',
  '/home/cryo/Plone/buildout-cache/eggs/plone.app.jquery-1.7.2-py2.7.egg',
  '/home/cryo/Plone/buildout-cache/eggs/Zope2-2.13.22-py2.7.egg',
  '/home/cryo/Plone/buildout-cache/eggs/Products.GenericSetup-1.7.4-py2.7.egg',
  '/home/cryo/Plone/buildout-cache/eggs/Products.CMFCore-2.2.7-py2.7.egg',
  '/home/cryo/Plone/buildout-cache/eggs/zope.component-3.9.5-py2.7.egg',
  '/home/cryo/Plone/buildout-cache/eggs/zope.traversing-3.13.2-py2.7.egg',
  '/home/cryo/Plone/buildout-cache/eggs/zope.tales-3.5.3-py2.7.egg',
  '/home/cryo/Plone/buildout-cache/eggs/zope.tal-3.5.2-py2.7.egg',
  '/home/cryo/Plone/buildout-cache/eggs/zope.structuredtext-3.5.1-py2.7.egg',
  '/home/cryo/Plone/buildout-cache/eggs/zope.site-3.9.2-py2.7.egg',
  '/home/cryo/Plone/buildout-cache/eggs/zope.publisher-3.12.6-py2.7.egg',
  '/home/cryo/Plone/buildout-cache/eggs/zope.pagetemplate-3.6.3-py2.7.egg',
  '/home/cryo/Plone/buildout-cache/eggs/zope.location-3.9.1-py2.7.egg',
  '/home/cryo/Plone/buildout-cache/eggs/zope.interface-3.6.7-py2.7-linux-i686.egg',
  '/home/cryo/Plone/buildout-cache/eggs/zope.i18nmessageid-3.5.3-py2.7-linux-i686.egg',
  '/home/cryo/Plone/buildout-cache/eggs/zope.i18n-3.7.4-py2.7.egg',
  '/home/cryo/Plone/buildout-cache/eggs/zope.event-3.5.2-py2.7.egg',
  '/home/cryo/Plone/buildout-cache/eggs/zope.dottedname-3.4.6-py2.7.egg',
  '/home/cryo/Plone/buildout-cache/eggs/zope.deprecation-3.4.1-py2.7.egg',
  '/home/cryo/Plone/buildout-cache/eggs/zope.deferredimport-3.5.3-py2.7.egg',
  '/home/cryo/Plone/buildout-cache/eggs/zope.container-3.11.2-py2.7-linux-i686.egg',
  '/home/cryo/Plone/buildout-cache/eggs/zope.app.locales-3.6.2-py2.7.egg',
  '/home/cryo/Plone/buildout-cache/eggs/z3c.autoinclude-0.3.5-py2.7.egg',
  '/home/cryo/Plone/buildout-cache/eggs/transaction-1.1.1-py2.7.egg',
  '/home/cryo/Plone/buildout-cache/eggs/plonetheme.sunburst-1.4.6-py2.7.egg',
  '/home/cryo/Plone/buildout-cache/eggs/plonetheme.classic-1.3.3-py2.7.egg',
  '/home/cryo/Plone/buildout-cache/eggs/plone.theme-2.1.1-py2.7.egg',
  '/home/cryo/Plone/buildout-cache/eggs/plone.session-3.5.3-py2.7.egg',
  '/home/cryo/Plone/buildout-cache/eggs/plone.registry-1.0.1-py2.7.egg',
  '/home/cryo/Plone/buildout-cache/eggs/plone.protect-2.0.2-py2.7.egg',
  '/home/cryo/Plone/buildout-cache/eggs/plone.portlets-2.2-py2.7.egg',
  '/home/cryo/Plone/buildout-cache/eggs/plone.portlet.static-2.0.2-py2.7.egg',
  '/home/cryo/Plone/buildout-cache/eggs/plone.portlet.collection-2.1.5-py2.7.egg',
  '/home/cryo/Plone/buildout-cache/eggs/plone.memoize-1.1.1-py2.7.egg',
  '/home/cryo/Plone/buildout-cache/eggs/plone.locking-2.0.4-py2.7.egg',
  '/home/cryo/Plone/buildout-cache/eggs/plone.intelligenttext-2.0.2-py2.7.egg',
  '/home/cryo/Plone/buildout-cache/eggs/plone.indexer-1.0.2-py2.7.egg',
  '/home/cryo/Plone/buildout-cache/eggs/plone.i18n-2.0.9-py2.7.egg',
  '/home/cryo/Plone/buildout-cache/eggs/plone.fieldsets-2.0.2-py2.7.egg',
  '/home/cryo/Plone/buildout-cache/eggs/plone.contentrules-2.0.4-py2.7.egg',
  '/home/cryo/Plone/buildout-cache/eggs/plone.browserlayer-2.1.3-py2.7.egg',
  '/home/cryo/Plone/buildout-cache/eggs/plone.batching-1.0.1-py2.7.egg',
  '/home/cryo/Plone/buildout-cache/eggs/plone.app.workflow-2.1.7-py2.7.egg',
  '/home/cryo/Plone/buildout-cache/eggs/plone.app.vocabularies-2.1.14-py2.7.egg',
  '/home/cryo/Plone/buildout-cache/eggs/plone.app.viewletmanager-2.0.5-py2.7.egg',
  '/home/cryo/Plone/buildout-cache/eggs/plone.app.uuid-1.1-py2.7.egg',
  '/home/cryo/Plone/buildout-cache/eggs/plone.app.users-1.2-py2.7.egg',
  '/home/cryo/Plone/buildout-cache/eggs/plone.app.upgrade-1.3.6-py2.7.egg',
  '/home/cryo/Plone/buildout-cache/eggs/plone.app.search-1.1.7-py2.7.egg',
  '/home/cryo/Plone/buildout-cache/eggs/plone.app.registry-1.2.3-py2.7.egg',
  '/home/cryo/Plone/buildout-cache/eggs/plone.app.redirector-1.2-py2.7.egg',
  '/home/cryo/Plone/buildout-cache/eggs/plone.app.portlets-2.4.8-py2.7.egg',
  '/home/cryo/Plone/buildout-cache/eggs/plone.app.locales-4.3.3-py2.7.egg',
  '/home/cryo/Plone/buildout-cache/eggs/plone.app.linkintegrity-1.5.4-py2.7.egg',
  '/home/cryo/Plone/buildout-cache/eggs/plone.app.layout-2.3.11-py2.7.egg',
  '/home/cryo/Plone/buildout-cache/eggs/plone.app.i18n-2.0.2-py2.7.egg',
  '/home/cryo/Plone/buildout-cache/eggs/plone.app.form-2.2.4-py2.7.egg',
  '/home/cryo/Plone/buildout-cache/eggs/plone.app.folder-1.0.6-py2.7.egg',
  '/home/cryo/Plone/buildout-cache/eggs/plone.app.discussion-2.2.12-py2.7.egg',
  '/home/cryo/Plone/buildout-cache/eggs/plone.app.customerize-1.2.2-py2.7.egg',
  '/home/cryo/Plone/buildout-cache/eggs/plone.app.controlpanel-2.3.8-py2.7.egg',
  '/home/cryo/Plone/buildout-cache/eggs/plone.app.contentrules-3.0.6-py2.7.egg',
  '/home/cryo/Plone/buildout-cache/eggs/plone.app.contentmenu-2.0.10-py2.7.egg',
  '/home/cryo/Plone/buildout-cache/eggs/plone.app.contentlisting-1.0.5-py2.7.egg',
  '/home/cryo/Plone/buildout-cache/eggs/plone.app.content-2.1.4-py2.7.egg',
  '/home/cryo/Plone/buildout-cache/eggs/plone.app.collection-1.0.11-py2.7.egg',
  '/home/cryo/Plone/buildout-cache/eggs/plone.app.blob-1.5.9-py2.7.egg',
  '/home/cryo/Plone/buildout-cache/eggs/five.localsitemanager-2.0.5-py2.7.egg',
  '/home/cryo/Plone/buildout-cache/eggs/five.customerize-1.1-py2.7.egg',
  '/home/cryo/Plone/buildout-cache/eggs/borg.localrole-3.0.2-py2.7.egg',
  '/home/cryo/Plone/buildout-cache/eggs/archetypes.referencebrowserwidget-2.4.20-py2.7.egg',
  '/home/cryo/Plone/buildout-cache/eggs/archetypes.querywidget-1.0.10-py2.7.egg',
  '/home/cryo/Plone/buildout-cache/eggs/ZODB3-3.10.5-py2.7-linux-i686.egg',
  '/home/cryo/Plone/buildout-cache/eggs/Products.statusmessages-4.0-py2.7.egg',
  '/home/cryo/Plone/buildout-cache/eggs/Products.TinyMCE-1.3.6-py2.7.egg',
  '/home/cryo/Plone/buildout-cache/eggs/Products.ResourceRegistries-2.2.10-py2.7.egg',
  '/home/cryo/Plone/buildout-cache/eggs/Products.PortalTransforms-2.1.3-py2.7.egg',
  '/home/cryo/Plone/buildout-cache/eggs/Products.PluginRegistry-1.3-py2.7.egg',
  '/home/cryo/Plone/buildout-cache/eggs/Products.PluggableAuthService-1.10.0-py2.7.egg',
  '/home/cryo/Plone/buildout-cache/eggs/Products.PlonePAS-4.1.3-py2.7.egg',
  '/home/cryo/Plone/buildout-cache/eggs/Products.PloneLanguageTool-3.2.7-py2.7.egg',
  '/home/cryo/Plone/buildout-cache/eggs/Products.PlacelessTranslationService-2.0.4-py2.7.egg',
  '/home/cryo/Plone/buildout-cache/eggs/Products.PasswordResetTool-2.0.16-py2.7.egg',
  '/home/cryo/Plone/buildout-cache/eggs/Products.MimetypesRegistry-2.0.5-py2.7.egg',
  '/home/cryo/Plone/buildout-cache/eggs/Products.ExternalEditor-1.1.0-py2.7.egg',
  '/home/cryo/Plone/buildout-cache/eggs/Products.ExtendedPathIndex-3.1-py2.7.egg',
  '/home/cryo/Plone/buildout-cache/eggs/Products.DCWorkflow-2.2.4-py2.7.egg',
  '/home/cryo/Plone/buildout-cache/eggs/Products.CMFUid-2.2.1-py2.7.egg',
  '/home/cryo/Plone/buildout-cache/eggs/Products.CMFQuickInstallerTool-3.0.6-py2.7.egg',
  '/home/cryo/Plone/buildout-cache/eggs/Products.CMFFormController-3.0.3-py2.7.egg',
  '/home/cryo/Plone/buildout-cache/eggs/Products.CMFEditions-2.2.9-py2.7.egg',
  '/home/cryo/Plone/buildout-cache/eggs/Products.CMFDynamicViewFTI-4.0.5-py2.7.egg',
  '/home/cryo/Plone/buildout-cache/eggs/Products.CMFDiffTool-2.1-py2.7.egg',
  '/home/cryo/Plone/buildout-cache/eggs/Products.CMFDefault-2.2.4-py2.7.egg',
  '/home/cryo/Plone/buildout-cache/eggs/Products.CMFCalendar-2.2.3-py2.7.egg',
  '/home/cryo/Plone/buildout-cache/eggs/Products.CMFActionIcons-2.1.3-py2.7.egg',
  '/home/cryo/Plone/buildout-cache/eggs/Products.ATContentTypes-2.1.14-py2.7.egg',
  '/home/cryo/Plone/buildout-cache/eggs/ExtensionClass-2.13.2-py2.7-linux-i686.egg',
  '/home/cryo/Plone/buildout-cache/eggs/DateTime-3.0.3-py2.7.egg',
  '/home/cryo/Plone/buildout-cache/eggs/Acquisition-2.13.8-py2.7-linux-i686.egg',
  '/home/cryo/Plone/buildout-cache/eggs/plone.uuid-1.0.3-py2.7.egg',
  '/home/cryo/Plone/buildout-cache/eggs/plone.folder-1.0.5-py2.7.egg',
  '/home/cryo/Plone/buildout-cache/eggs/Products.validation-2.0-py2.7.egg',
  '/home/cryo/Plone/buildout-cache/eggs/Products.ZSQLMethods-2.13.4-py2.7.egg',
  '/home/cryo/Plone/buildout-cache/eggs/Products.Marshall-2.1.2-py2.7.egg',
  '/home/cryo/Plone/buildout-cache/eggs/zope.viewlet-3.7.2-py2.7.egg',
  '/home/cryo/Plone/buildout-cache/eggs/zope.schema-4.2.2-py2.7.egg',
  '/home/cryo/Plone/buildout-cache/eggs/zope.lifecycleevent-3.6.2-py2.7.egg',
  '/home/cryo/Plone/buildout-cache/eggs/zope.datetime-3.4.1-py2.7.egg',
  '/home/cryo/Plone/buildout-cache/eggs/zope.contenttype-3.5.5-py2.7.egg',
  '/home/cryo/Plone/buildout-cache/eggs/five.globalrequest-1.0-py2.7.egg',
  '/home/cryo/Plone/buildout-cache/eggs/repoze.xmliter-0.5-py2.7.egg',
  '/home/cryo/Plone/buildout-cache/eggs/plone.resourceeditor-1.0-py2.7.egg',
  '/home/cryo/Plone/buildout-cache/eggs/plone.resource-1.0.2-py2.7.egg',
  '/home/cryo/Plone/buildout-cache/eggs/plone.transformchain-1.0.3-py2.7.egg',
  '/home/cryo/Plone/buildout-cache/eggs/plone.subrequest-1.6.8-py2.7.egg',
  '/home/cryo/Plone/buildout-cache/eggs/lxml-2.3.6-py2.7-linux-i686.egg',
  '/home/cryo/Plone/buildout-cache/eggs/roman-1.4.0-py2.7.egg',
  '/home/cryo/Plone/buildout-cache/eggs/docutils-0.9.1-py2.7.egg',
  '/home/cryo/Plone/buildout-cache/eggs/diazo-1.0.5-py2.7.egg',
  '/home/cryo/Plone/buildout-cache/eggs/plone.openid-2.0.2-py2.7.egg',
  '/home/cryo/Plone/buildout-cache/eggs/zope.annotation-3.5.0-py2.7.egg',
  '/home/cryo/Plone/buildout-cache/eggs/z3c.form-3.1.1-py2.7.egg',
  '/home/cryo/Plone/buildout-cache/eggs/zope.browserpage-3.12.2-py2.7.egg',
  '/home/cryo/Plone/buildout-cache/eggs/plone.z3cform-0.8.0-py2.7.egg',
  '/home/cryo/Plone/buildout-cache/eggs/plone.supermodel-1.2.4-py2.7.egg',
  '/home/cryo/Plone/buildout-cache/eggs/plone.autoform-1.6-py2.7.egg',
  '/home/cryo/Plone/buildout-cache/eggs/plone.app.z3cform-0.7.6-py2.7.egg',
  '/home/cryo/Plone/buildout-cache/eggs/plone.schemaeditor-1.3.7-py2.7.egg',
  '/home/cryo/Plone/buildout-cache/eggs/plone.rfc822-1.1-py2.7.egg',
  '/home/cryo/Plone/buildout-cache/eggs/plone.namedfile-2.0.5-py2.7.egg',
  '/home/cryo/Plone/buildout-cache/eggs/plone.formwidget.namedfile-1.0.9-py2.7.egg',
  '/home/cryo/Plone/buildout-cache/eggs/plone.dexterity-2.2.1-py2.7.egg',
  '/home/cryo/Plone/buildout-cache/eggs/plone.behavior-1.0.2-py2.7.egg',
  '/home/cryo/Plone/buildout-cache/eggs/plone.app.textfield-1.2.3-py2.7.egg',
  '/home/cryo/Plone/buildout-cache/eggs/collective.z3cform.datetimewidget-1.2.6-py2.7.egg',
  '/home/cryo/Plone/buildout-cache/eggs/z3c.zcmlhook-1.0b1-py2.7.egg',
  '/home/cryo/Plone/buildout-cache/eggs/zope.browserresource-3.10.3-py2.7.egg',
  '/home/cryo/Plone/buildout-cache/eggs/plone.cachepurging-1.0.5-py2.7.egg',
  '/home/cryo/Plone/buildout-cache/eggs/plone.caching-1.0-py2.7.egg',
  '/home/cryo/Plone/buildout-cache/eggs/python_dateutil-1.5-py2.7.egg',
  '/home/cryo/Plone/buildout-cache/eggs/Products.StandardCacheManagers-2.13.0-py2.7.egg',
  '/home/cryo/Plone/buildout-cache/eggs/Products.PythonScripts-2.13.2-py2.7.egg',
  '/home/cryo/Plone/buildout-cache/eggs/Products.MIMETools-2.13.0-py2.7.egg',
  '/home/cryo/Plone/buildout-cache/eggs/Products.MailHost-2.13.1-py2.7.egg',
  '/home/cryo/Plone/buildout-cache/eggs/Products.ExternalMethod-2.13.0-py2.7.egg',
  '/home/cryo/Plone/buildout-cache/eggs/Products.BTreeFolder2-2.13.3-py2.7.egg',
  '/home/cryo/Plone/buildout-cache/eggs/zope.testing-3.9.7-py2.7.egg',
  '/home/cryo/Plone/buildout-cache/eggs/zope.testbrowser-3.11.1-py2.7.egg',
  '/home/cryo/Plone/buildout-cache/eggs/zope.size-3.4.1-py2.7.egg',
  '/home/cryo/Plone/buildout-cache/eggs/zope.sequencesort-3.4.0-py2.7.egg',
  '/home/cryo/Plone/buildout-cache/eggs/zope.sendmail-3.7.5-py2.7.egg',
  '/home/cryo/Plone/buildout-cache/eggs/zope.security-3.7.4-py2.7-linux-i686.egg',
  '/home/cryo/Plone/buildout-cache/eggs/zope.ptresource-3.9.0-py2.7.egg',
  '/home/cryo/Plone/buildout-cache/eggs/zope.proxy-3.6.1-py2.7-linux-i686.egg',
  '/home/cryo/Plone/buildout-cache/eggs/zope.processlifetime-1.0-py2.7.egg',
  '/home/cryo/Plone/buildout-cache/eggs/zope.exceptions-3.6.2-py2.7.egg',
  '/home/cryo/Plone/buildout-cache/eggs/zope.contentprovider-3.7.2-py2.7.egg',
  '/home/cryo/Plone/buildout-cache/eggs/zope.configuration-3.7.4-py2.7.egg',
  '/home/cryo/Plone/buildout-cache/eggs/zope.browsermenu-3.9.1-py2.7.egg',
  '/home/cryo/Plone/buildout-cache/eggs/zope.browser-1.3-py2.7.egg',
  '/home/cryo/Plone/buildout-cache/eggs/zLOG-2.11.1-py2.7.egg',
  '/home/cryo/Plone/buildout-cache/eggs/zExceptions-2.13.0-py2.7.egg',
  '/home/cryo/Plone/buildout-cache/eggs/zdaemon-2.0.7-py2.7.egg',
  '/home/cryo/Plone/buildout-cache/eggs/tempstorage-2.12.2-py2.7.egg',
  '/home/cryo/Plone/buildout-cache/eggs/pytz-2013b-py2.7.egg',
  '/home/cryo/Plone/buildout-cache/eggs/initgroups-2.13.0-py2.7-linux-i686.egg',
  '/home/cryo/Plone/buildout-cache/eggs/ZopeUndo-2.12.0-py2.7.egg',
  '/home/cryo/Plone/buildout-cache/eggs/ZConfig-2.9.1-py2.7.egg',
  '/home/cryo/Plone/buildout-cache/eggs/RestrictedPython-3.6.0-py2.7.egg',
  '/home/cryo/Plone/buildout-cache/eggs/Record-2.13.0-py2.7-linux-i686.egg',
  '/home/cryo/Plone/buildout-cache/eggs/Products.ZCTextIndex-2.13.5-py2.7-linux-i686.egg',
  '/home/cryo/Plone/buildout-cache/eggs/Products.ZCatalog-2.13.27-py2.7.egg',
  '/home/cryo/Plone/buildout-cache/eggs/Products.OFSP-2.13.2-py2.7.egg',
  '/home/cryo/Plone/buildout-cache/eggs/Persistence-2.13.2-py2.7-linux-i686.egg',
  '/home/cryo/Plone/buildout-cache/eggs/MultiMapping-2.13.0-py2.7-linux-i686.egg',
  '/home/cryo/Plone/buildout-cache/eggs/Missing-2.13.1-py2.7-linux-i686.egg',
  '/home/cryo/Plone/buildout-cache/eggs/DocumentTemplate-2.13.2-py2.7-linux-i686.egg',
  '/home/cryo/Plone/buildout-cache/eggs/AccessControl-3.0.8-py2.7-linux-i686.egg',
  '/home/cryo/Plone/buildout-cache/eggs/zope.formlib-4.0.6-py2.7.egg',
  '/home/cryo/Plone/buildout-cache/eggs/zope.app.publication-3.12.0-py2.7.egg',
  '/home/cryo/Plone/buildout-cache/eggs/zope.broken-3.6.0-py2.7.egg',
  '/home/cryo/Plone/buildout-cache/eggs/zope.filerepresentation-3.6.1-py2.7.egg',
  '/home/cryo/Plone/buildout-cache/eggs/zc.buildout-2.2.1-py2.7.egg',
  '/home/cryo/Plone/buildout-cache/eggs/plone.keyring-2.0.1-py2.7.egg',
  '/home/cryo/Plone/buildout-cache/eggs/zope.ramcache-1.0-py2.7.egg',
  '/home/cryo/Plone/buildout-cache/eggs/Unidecode-0.04.1-py2.7.egg',
  '/home/cryo/Plone/buildout-cache/eggs/five.formlib-1.0.4-py2.7.egg',
  '/home/cryo/Plone/buildout-cache/eggs/zope.componentvocabulary-1.0.1-py2.7.egg',
  '/home/cryo/Plone/buildout-cache/eggs/plone.app.querystring-1.1.1-py2.7.egg',
  '/home/cryo/Plone/buildout-cache/eggs/Products.SecureMailHost-1.1.2-py2.7.egg',
  '/home/cryo/Plone/buildout-cache/eggs/Products.contentmigration-2.1.7-py2.7.egg',
  '/home/cryo/Plone/buildout-cache/eggs/feedparser-5.0.1-py2.7.egg',
  '/home/cryo/Plone/buildout-cache/eggs/collective.monkeypatcher-1.0.1-py2.7.egg',
  '/home/cryo/Plone/buildout-cache/eggs/zope.cachedescriptors-3.5.1-py2.7.egg',
  '/home/cryo/Plone/buildout-cache/eggs/plone.stringinterp-1.0.11-py2.7.egg',
  '/home/cryo/Plone/buildout-cache/eggs/plone.scale-1.3.3-py2.7.egg',
  '/home/cryo/Plone/buildout-cache/eggs/plone.app.imaging-1.0.10-py2.7.egg',
  '/home/cryo/Plone/buildout-cache/eggs/archetypes.schemaextender-2.1.3-py2.7.egg',
  '/home/cryo/Plone/buildout-cache/eggs/zc.lockfile-1.0.2-py2.7.egg',
  '/home/cryo/Plone/buildout-cache/eggs/zope.app.content-3.5.1-py2.7.egg',
  '/home/cryo/Plone/buildout-cache/eggs/plone.outputfilters-1.12-py2.7.egg',
  '/home/cryo/Plone/buildout-cache/eggs/Markdown-2.0.3-py2.7.egg',
  '/home/cryo/Plone/buildout-cache/eggs/python_gettext-1.2-py2.7.egg',
  '/home/cryo/Plone/buildout-cache/eggs/Products.ZopeVersionControl-1.1.3-py2.7.egg',
  '/home/cryo/Plone/buildout-cache/eggs/zope.copy-3.5.0-py2.7.egg',
  '/home/cryo/Plone/buildout-cache/eggs/zope.app.form-4.0.2-py2.7.egg',
  '/home/cryo/Plone/buildout-cache/eggs/Products.ATReferenceBrowserWidget-3.0-py2.7.egg',
  '/home/cryo/Plone/buildout-cache/eggs/zope.globalrequest-1.0-py2.7.egg',
  '/home/cryo/Plone/buildout-cache/eggs/z3c.caching-2.0a1-py2.7.egg',
  '/home/cryo/Plone/buildout-cache/eggs/experimental.cssselect-0.3-py2.7.egg',
  '/home/cryo/Plone/buildout-cache/eggs/python_openid-2.2.5-py2.7.egg',
  '/home/cryo/Plone/buildout-cache/eggs/six-1.2.0-py2.7.egg',
  '/home/cryo/Plone/buildout-cache/eggs/z3c.formwidget.query-0.10-py2.7.egg',
  '/home/cryo/Plone/buildout-cache/eggs/plone.synchronize-1.0.1-py2.7.egg',
  '/home/cryo/Plone/buildout-cache/eggs/plone.alterego-1.0-py2.7.egg',
  '/home/cryo/Plone/buildout-cache/eggs/mechanize-0.2.5-py2.7.egg',
  '/home/cryo/Plone/buildout-cache/eggs/zope.error-3.7.4-py2.7.egg',
  '/home/cryo/Plone/buildout-cache/eggs/zope.authentication-3.7.1-py2.7.egg',
  '/home/cryo/Plone/buildout-cache/eggs/unittest2-0.5.1-py2.7.egg',
  ]


import site
import getopt, glob, sys

from PIL import Image

if len(sys.argv) == 1:
    print("PIL File 0.4/2003-09-30 -- identify image files")
    print("Usage: pilfile [option] files...")
    print("Options:")
    print("  -f  list supported file formats")
    print("  -i  show associated info and tile data")
    print("  -v  verify file headers")
    print("  -q  quiet, don't warn for unidentified/missing/broken files")
    sys.exit(1)

try:
    opt, args = getopt.getopt(sys.argv[1:], "fqivD")
except getopt.error as v:
    print(v)
    sys.exit(1)

verbose = quiet = verify = 0

for o, a in opt:
    if o == "-f":
        Image.init()
        id = sorted(Image.ID)
        print("Supported formats:")
        for i in id:
            print(i, end=' ')
        sys.exit(1)
    elif o == "-i":
        verbose = 1
    elif o == "-q":
        quiet = 1
    elif o == "-v":
        verify = 1
    elif o == "-D":
        Image.DEBUG = Image.DEBUG + 1

def globfix(files):
    # expand wildcards where necessary
    if sys.platform == "win32":
        out = []
        for file in files:
            if glob.has_magic(file):
                out.extend(glob.glob(file))
            else:
                out.append(file)
        return out
    return files

for file in globfix(args):
    try:
        im = Image.open(file)
        print("%s:" % file, im.format, "%dx%d" % im.size, im.mode, end=' ')
        if verbose:
            print(im.info, im.tile, end=' ')
        print()
        if verify:
            try:
                im.verify()
            except:
                if not quiet:
                    print("failed to verify image", end=' ')
                    print("(%s:%s)" % (sys.exc_info()[0], sys.exc_info()[1]))
    except IOError as v:
        if not quiet:
            print(file, "failed:", v)
    except:
        import traceback
        if not quiet:
            print(file, "failed:", "unexpected error")
            traceback.print_exc(file=sys.stdout)