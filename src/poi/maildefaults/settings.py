from persistent.dict import PersistentDict
from zope import schema
from zope import interface
from zope.annotation.interfaces import IAnnotations
from z3c.form import form, field, button
from plone.z3cform import layout

from Products.Poi import PoiMessageFactory as _
from Products.Poi.content.tracker import possibleAreas
from Products.Poi.content.tracker import possibleIssueTypes
from Products.Poi.content.tracker import possibleSeverities
from Products.Poi.content.tracker import possibleTargetReleases
from Products.Poi.content.tracker import possibleAssignees

KEY = 'poi.maildefaults'


class ISettings(interface.Interface):
    """ Define settings data structure """

    title = schema.TextLine(
        title=u"Title",
        required=False,
        default=u'',
    )

    area = schema.Choice(
        title=_(u'Poi_label_issue_area', default=u'Area'),
        description=_(u'Poi_help_issue_area',
                      default=u"Select the area this issue is relevant to."),
        source=possibleAreas,
        required=False
    )

    issue_type = schema.Choice(
        title=_(u'Poi_label_issue_type', default=u'Issue Type'),
        description=_(u'Poi_help_issue_type',
                      default=u"Select the type of issue."),
        source=possibleIssueTypes,
        required=False
    )

    severity = schema.Choice(
        title=_(u'Poi_label_issue_severity', default=u'Severity'),
        description=_(u'Poi_help_issue_severity',
                      default=u"Select the severity of this issue."),
        source=possibleSeverities,
        required=False
    )

    target_release = schema.Choice(
        title=_(u'Poi_label_issue_target_release', default=u'Target Release'),
        description=_(u'Poi_help_issue_target_release',
                      default=u"Release this issue is targetted to be fixed in"),
        source=possibleTargetReleases,
        required=False,
    )

    assignee = schema.Choice(
        title=_(u'Poi_label_issue_assignee', default=u'Assignee'),
        description=_(u'Poi_help_issue_assignee',
                      default=u"Select which person, if any, is assigned to "
                      u"this issue."),
        source=possibleAssignees,
        required=False,
    )


class SettingsEditForm(form.EditForm):
    """
    Define form logic
    """
    fields = field.Fields(ISettings)
    label = u"Poi Mail-in Defaults"

    def getContent(self):
        area = self.fields.get('area')
        area.field.vocabulary = possibleAreas(self.context)
        issue_type = self.fields.get('issue_type')
        issue_type.field.vocabulary = possibleIssueTypes(self.context)
        severity = self.fields.get('severity')
        severity.field.vocabulary = possibleSeverities(self.context)
        target_release = self.fields.get('target_release')
        target_release.field.vocabulary = possibleTargetReleases(self.context)
        assignee = self.fields.get('assignee')
        assignee.field.vocabulary = possibleAssignees(self.context)
        return dict(ISettings(self.context))

    @button.buttonAndHandler(u'Save', name='save')
    def handle_save(self, action):
        data, errors = self.extractData()
        if errors:
            self.status = self.formErrorsMessage
            return
        ISettings(self.context).update(data)
        self.status = self.successMessage
        self.context._p_changed = True


SettingsView = layout.wrap_form(SettingsEditForm)


def mailin_settings(context):
    """ Adapter to store mailin defaults as annotations on a tracker
    """
    # Get all Annotations on the tracker
    annotations = IAnnotations(context)
    # return just our dictionary
    issue_defaults = annotations.setdefault(KEY, PersistentDict())
    return issue_defaults
