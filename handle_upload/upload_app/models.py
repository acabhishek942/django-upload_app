# -*- coding: utf-8 -*-
from django.db import models


class PDFDocument(models.Model):
    docfile = models.FileField(upload_to='documents/%Y/%m/%d')
