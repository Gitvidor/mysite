from django.urls import path

from . import views

urlpatterns = [
    path('test', views.index, name='index'),
    path('test_html', views.test_html),
    path('shell', views.shell),
    path('base_index',views.base_view),
    path('music_index',views.music_view),
    path('sport_index',views.sport_view),
    path('test_url_result', views.test_url_result, name = 'tr')

    # path('<int:fs>/<str:oper>/<int:ss>', views.indexn, name='indexn')
]