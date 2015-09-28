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

    area = schema.TextLine(
        title=u"Area",
        required=False,
        default=u'',
    )

    issueType = schema.TextLine(
        title=u"Issue Type",
        required=False,
        default=u'',
    )

    severity = schema.TextLine(
        title=u"Severity",
        required=False,
        default=u'',
    )

    dueDate = schema.TextLine(
        title=u"Required Due Date",
        required=False,
        default=u'',
    )

    targetRelease = schema.TextLine(
        title=u"Target Release",
        required=False,
        default=u'',
    )

    responsible = schema.TextLine(
        title=u"Responsible",
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
    return annotations.setdefault(KEY, PersistentDict())
