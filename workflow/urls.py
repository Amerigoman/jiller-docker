from django.conf.urls import url
from . import views

app_name = 'workflow'
urlpatterns = [

    url(r'^$', views.index, name='index'),

    url(r'^project/(?P<pk>\d+)/activesprint/$',
        views.ActiveSprintViewtypeView.as_view(), name='active_sprint'),

    url(r'^project/(?P<pk>\d+)/sprint/create/$',
        views.SprintCreate.as_view(), name='sprint_create'),

    #url for delete sprint. Hidden until create field is_active in Sprint model
    #url(r'^project/(?P<pk>\d+)/sprint/delete/$',
    #views.SprintDelete.as_view(), name='sprint_delete'),

    url(r'^issue/(?P<pk>\d+)/$',
        views.SprintCreate.as_view(), name='sprint_create'),

    url(r'^login/$', views.login_form, name='login'),
    url(r'^registration/$', views.registration_form, name='registration'),

    url(r'^profile/$', views.profile, name='profile'),
    url(r'^project/$', views.ProjectListView.as_view(), name='projects'),
    url(r'^project/create/$', views.ProjectCreate.as_view(),
        name='project_create'),

    url(r'^project/(?P<pk>\d+)/$', views.ProjectDetail.as_view(),
        name='project_detail'),

    url(r'^project/update/(?P<pk>\d+)/$', views.ProjectUpdate.as_view(),
        name='project_update'),
    url(r'^project/delete/(?P<pk>\d+)/$', views.ProjectDelete.as_view(),
        name='project_delete'),

    url(r'^project/(?P<project_id>\d+)/backlog/$', views.backlog,
        name='backlog'),
    url(r'^project/(?P<project_id>\d+)/issue/create/$',
        views.create_issue, name='create_issue'),
    url(r'^project/(?P<project_id>\d+)/issue/(?P<issue_id>\d+)/$',
        views.issue, name='issue'),
    url(r'^project/(?P<project_id>\d+)/issue/(?P<issue_id>\d+)/edit/$',
        views.edit_issue, name='edit_issue'),
    url(r'^project/(?P<project_id>\d+)/team/$', views.team, name='team'),
    url(r'^project/(?P<project_id>\d+)/sprint/$',
        views.sprints_list, name='sprints_list'),
    url(r'^project/(?P<project_id>\d+)/sprint/(?P<sprint_id>\d+)/$',
        views.SprintView.as_view(), name='sprint'),

    url(r'^employee/$', views.employee_index_view, name='employee-index'),
    url(r'^employee/(?P<employee_id>\d+)/$', views.employee_detail_view,
        name='employee-detail'),

]
