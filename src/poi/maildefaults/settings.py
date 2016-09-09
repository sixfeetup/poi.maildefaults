from persistent.dict import PersistentDict
from zope import schema
from zope import interface
from zope.annotation.interfaces import IAnnotations
from z3c.form import form, field, button
from plone.z3cform import layout

from Products.Poi import PoiMessageFactory as _
from Products.Poi.content.tracker import possibleAreas

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

    # TODO: Change this to select widget
    issue_type = schema.TextLine(
        title=u"Issue Type",
        required=False,
        default=u'',
    )

    # TODO: Change this to select widget
    severity = schema.TextLine(
        title=u"Severity",
        required=False,
        default=u'',
    )

    # TODO: Change this to select widget
    target_release = schema.TextLine(
        title=u"Target Release",
        required=False,
        default=u'',
    )

    # TODO: Change this to select widget
    assignee = schema.TextLine(
        title=u"Assignee",
        required=False,
        default=u'',
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
