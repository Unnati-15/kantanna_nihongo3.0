"""
URL configuration for my_nihongo_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
from chatbot.views import indexchatbot,textspeech,speechtext,imgrecog
from django.urls import path,include
from my_nihongo_project import views



urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/',include('django.contrib.auth.urls')),
    path('login',views.login),
    path('logout',views.logout),
    path('register',views.register),
    path('home',views.homepage),
    path('phrases',views.phrases),
    path('hiragana',views.hiragana),
    path('hiraganaquiz/<int:h_id>',views.hiraganaquiz),
    path('submitanswer/<int:h_id>/<int:q_id>',views.submitanswer),
    path('katakana',views.katakana),
    path('katakanaquiz/<int:k_id>',views.katakanaquiz),
    path('submitanswerk/<int:k_id>/<int:q2_id>',views.submitanswerk),
    path('translation',views.translate),
    path('kanji',views.kanji),
    path('examdetails',views.examdetails),
    path('resources',views.resources),
    path('contact',views.contact),
    path('aboutus',views.aboutus),
    path('result',views.result),
    path('flashcard', views.flashcard),
    path('update_flashcard/<id>', views.update_flashcard),
    path('delete_flashcard/<id>', views.delete_flashcard),
    path('chatbot',indexchatbot),
    path('chatbotts',textspeech),
    path('chatbotst',speechtext),
    path('imgtotxt',imgrecog),
]

urlpatterns = urlpatterns + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
urlpatterns = urlpatterns + static(settings.MODULE_URL,document_root=settings.MODULE_ROOT)