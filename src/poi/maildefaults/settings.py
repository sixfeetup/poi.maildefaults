from datetime import datetime
from persistent.dict import PersistentDict
from zope import schema
from zope import interface
from zope.annotation.interfaces import IAnnotations
from z3c.form import form, field, button
from plone.z3cform import layout


KEY = 'poi.maildefaults'


class ISettings(interface.Interface):
    """ Define settings data structure """

    title = schema.TextLine(
        title=u"Title",
        required=False,
        default=u'',
    )

    # TODO: Change this to select widget
    area = schema.TextLine(
        title=u"Area",
        required=False,
        default=u'',
    )

    # TODO: Change this to select widget
    issueType = schema.TextLine(
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
    targetRelease = schema.TextLine(
        title=u"Target Release",
        required=False,
        default=u'',
    )

    # TODO: Change this to select widget
    responsibleManager = schema.TextLine(
        title=u"Responsible Manager",
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
    # set a dueDate for today on a specific project
    # TODO: add settings for changing dueDate
    today = datetime.today()
    issue_defaults['dueDate'] = today.strftime('%m/%d/%Y')
    return issue_defaults
