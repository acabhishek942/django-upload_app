# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

from handle_upload.upload_app.models import PDFDocument
from handle_upload.upload_app.forms import PDFDocumentForm


def list(request):
    # Handle file upload
    if request.method == 'POST':
        form = PDFDocumentForm(request.POST, request.FILES)
        if form.is_valid():
            newdoc = PDFDocument(docfile=request.FILES['docfile'])
            newdoc.save()

            # Redirect to the document list after POST
            return HttpResponseRedirect(reverse('handle_upload.upload_app.views.list'))
    else:
        form = PDFDocumentForm()  # A empty, unbound form

    # Load documents for the list page
    documents = PDFDocument.objects.all()

    # Render list page with the documents and the form
    return render_to_response(
        'upload_app/base.html',
        {'documents': documents, 'form': form},
        context_instance=RequestContext(request)
    )
