from django.conf.urls.defaults import *

# a not very well namespaced django plugin class
from profiles import views as profile_views
from contact_form.views import contact_form
import frontend.views as frontend_views
import frontend.forms as frontend_forms

from django.views.generic.simple import redirect_to, direct_to_template
from frontend.models import Feature

urlpatterns = patterns('',

    # profiles
    url(r'^profiles/edit/$', profile_views.edit_profile, {'form_class': frontend_forms.UserProfileForm}, name='profiles_edit_profile'),
    url(r'^profiles/(?P<username>.*)/message/$', frontend_views.user_message, name='user_message'),
    url(r'^profiles/(?P<username>.*)/$', frontend_views.profile_detail, name='profile'),
    url(r'^dashboard/$',
      frontend_views.redirect_dashboard_to_profile,
      name='dashboard'),
    # This duplicate is provided because the standard profiles
    # plugin requires that 'profiles_profile_detail' work when
    # using reverse().
    url(r'^profiles/(?P<username>.*)/$', frontend_views.profile_detail, name='profiles_profile_detail'),
    #url(r'^profiles/', include('profiles.urls')),

    url(r'^login/$',frontend_views.login, name='login'),
    url(r'^login/confirm/$', direct_to_template, {'template': 'registration/confirm_account.html'}, name='confirm_account'),
    url(r'^about/$', direct_to_template, {'template': 'frontend/about.html'}, name='about'),
    url(r'^tour/$', redirect_to, {'url': '/about/'}, name='tour'),
    url(r'^example_data/$', direct_to_template, {'template': 'frontend/example_data.html'}, name='api'),


    url(r'^help/(?P<mode>intro|faq|tutorials|documentation|code_documentation|libraries)/(?P<language>python|php|ruby|javascript)/$','django.views.generic.simple.redirect_to', {'url': '/docs/%(language)s'},name='help'),
    url(r'^help/(?P<mode>intro|faq|tutorials|documentation|code_documentation|libraries)/$','django.views.generic.simple.redirect_to', {'url': '/docs/'}, name='help_default'),
    url(r'^help/$','django.views.generic.simple.redirect_to', {'url': '/docs/'}, name='help_default'),

    #hello world
    url(r'^hello_world.html', direct_to_template, {'template': 'frontend/hello_world.html'}, name='help_hello_world'),

    # contact form
    url(r'^contact/$', contact_form, {'form_class': frontend_forms.ScraperWikiContactForm}, name='contact_form'),
    url(r'^contact/sent/$', direct_to_template, {'template': 'contact_form/contact_form_sent.html'}, name='contact_form_sent'),

    # user's scrapers
    url(r'^stats/$', frontend_views.stats, name='stats'),

    # Example pages to scrape :)
    url(r'^examples/basic_table\.html$', direct_to_template, {'template': 'examples/basic_table.html'}, name='example_basic_table'),
    # for testing error handling
    url(r'^test_error/$',                  frontend_views.test_error, name='test_error'),

    #searching and browsing
    url(r'^search/$', frontend_views.search, name='search'),
    url(r'^search/(?P<q>.+)/$', frontend_views.search, name='search'),

    url(r'^browse/(?P<page_number>\d+)?$', frontend_views.browse, name='scraper_list'),
    url(r'^browse/(?P<wiki_type>scraper|view)s/(?P<page_number>\d+)?$', frontend_views.browse_wiki_type, name='scraper_list_wiki_type'),
    url(r'^tags/$', frontend_views.tags, name='all_tags'),
    url(r'^tags/(?P<tag>[^/]+)$', frontend_views.tag, name='single_tag'),
)
