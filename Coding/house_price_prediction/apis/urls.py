from django.conf.urls import url 
from apis import views 
 
urlpatterns = [ 
    url(r'^api/localitydescription$', views.localityDescription_list),
    url(r'^api/localitydescription/(?P<pk>[0-9]+)$', views.localityDescription_detail),
    url(r'^api/localitydescription/published$', views.localityDescription_list_published),
    url(r'^api/housingconditions$', views.housingConditions_list),
    url(r'^api/housingconditions/(?P<pk>[0-9]+)$', views.housingConditions_detail),
    url(r'^api/housingconditions/published$', views.housingConditions_list_published),
    url(r'^api/exteriorfeatures$', views.exteriorFeatures_list),
    url(r'^api/exteriorfeatures/(?P<pk>[0-9]+)$', views.exteriorFeatures_detail),
    url(r'^api/exteriorfeatures/published$', views.exteriorFeatures_list_published),
    url(r'^api/interiorfeatures$', views.interiorFeatures_list),
    url(r'^api/interiorfeatures/(?P<pk>[0-9]+)$', views.interiorFeatures_detail),
    url(r'^api/interiorfeatures/published$', views.interiorFeatures_list_published),
    url(r'^api/pricePrediction$', views.house_predictions)
]