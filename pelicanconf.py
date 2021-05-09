#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'blackle0pard'
SITENAME = 'くろひょうのぶろぐ'
SITEURL = 'https://blackle0pard.net'
#SITEURL = 'http://127.0.0.1:8000'

PATH = 'content'
STATIC_PATHS = [
    'images', 
    'extra/robots.txt',
    'extra/security.txt',
    'extra/favicon.ico'
]
EXTRA_PATH_METADATA = {
    'extra/robots.txt': {'path': 'robots.txt'},
    'extra/security.txt': {'path': '.well-known/security.txt'},
    'extra/favicon.ico': {'path': 'favicon.ico'}
}

TIMEZONE = 'Asia/Tokyo'
DEFAULT_DATE_FORMAT = '%Y-%m-%d %H:%M'
DEFAULT_LANG = 'ja'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = 'feeds/all.rss.xml'
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

DEFAULT_PAGINATION = 25

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

ARTICLE_URL = '{slug}/'
ARTICLE_SAVE_AS = '{slug}/index.html'
TAG_URL = 'tag/{slug}/'
TAG_SAVE_AS = 'tag/{slug}/index.html'
TAGS_SAVE_AS = 'tags/index.html'
DIRECT_TEMPLATES = ('index', 'tags', 'categories', 'archives', 'sitemap')
SITEMAP_SAVE_AS = 'sitemap.xml'
ARCHIVES_SAVE_AS = 'archives.html'

THEME_STATIC_DIR = 'theme'
