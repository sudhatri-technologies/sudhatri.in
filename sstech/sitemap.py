from django.contrib import sitemaps
from django.urls import reverse

import datetime

class StaticViewsSiteMap(sitemaps.Sitemap):
    priority=1
    lastmod=datetime.datetime(2023, 3, 5)
    
    
    def items(self):
        return ['home',
               'about',
               'web',
               'mobile',
               'dm',
               'us',
               'ds',
               'careers',
               'contact']
    def location(self,item):
        return reverse(item)