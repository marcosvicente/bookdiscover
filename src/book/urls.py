from django.conf.urls import include
from django.conf.urls import url
from django.conf import settings

from django.views.generic.base import TemplateView
from django.views.generic import ListView

from .views import BookListCategory, BookListCategoryAventura, BookListCategoryRomance,BookListCategoryPoesia, BookListCategoryFiccaoCientifica, BookListCategoryTerror, BookListCategoryFantasia, BookListCategoryComedia, BookListCategoryAutoAjuda, BookListCategoryRomancePolicial


urlpatterns =[
        
    url(r'^all/', BookListCategory.as_view(), name="categoria"),
    url(r'^aventura/', BookListCategoryAventura.as_view(), name="categoria-aventura"),
    url(r'^romance/', BookListCategoryRomance.as_view(), name="categoria-romance"),
    url(r'^poesia/', BookListCategoryPoesia.as_view(), name="categoria-poesia"),
    url(r'^ficcao-cientifica/', BookListCategoryFiccaoCientifica.as_view(), name="categoria-ficcao-cientifica"),

    url(r'^terror/', BookListCategoryTerror.as_view(), name="categoria-terror"),
    url(r'^fantasia/', BookListCategoryFantasia.as_view(), name="categoria-fantasia"),
    url(r'^comedia/', BookListCategoryComedia.as_view(), name="categoria-comedia"),
    url(r'^auto-ajuda/', BookListCategoryAutoAjuda.as_view(), name="categoria-auto-ajuda"),
    url(r'^romance-policial/', BookListCategoryRomancePolicial.as_view(), name="categoria-romance-policial"),

]
