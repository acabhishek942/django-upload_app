# -*- coding: utf-8 -*-
from django import forms


class PDFDocumentForm(forms.Form):
    docfile = forms.FileField(
        label='Select a file'
    )
