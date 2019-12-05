from django.contrib import admin
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from catone import views
from django.conf.urls import url
from django.urls import include


from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api/quiz-questions/', views.quiz.as_view()),
    url(r'^$',views.home),
    url(r'^page404/',views.privacypolicy),

]+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
urlpatterns = format_suffix_patterns(urlpatterns)