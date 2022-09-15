from django.urls import path
from wishlist.views import show_wishlist, show_xml, show_json, show_JSON_by_id, show_XML_by_id

app_name = 'wishlist'

urlpatterns = [
    path('', show_wishlist, name='show_wishlist'), 
    path('xml/', show_xml, name='show_xml'),
    path('json/', show_json, name='show_json'),
    path('json/<int:id>', show_JSON_by_id, name='show_JSON_by_id'),
    path('xml/<int:id>', show_XML_by_id, name='show_XML_by_id')
]