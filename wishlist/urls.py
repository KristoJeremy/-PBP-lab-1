from django.urls import path
from wishlist.views import show_wishlist, show_xml, show_json, show_JSON_by_id, show_XML_by_id
from wishlist.views import register, login_user, logout_user, show_ajax, create_wishlist

app_name = 'wishlist'

urlpatterns = [
    path('', show_wishlist, name='show_wishlist'), 
    path('xml/', show_xml, name='show_xml'),
    path('json/', show_json, name='show_json'),
    path('json/<int:id>', show_JSON_by_id, name='show_JSON_by_id'),
    path('xml/<int:id>', show_XML_by_id, name='show_XML_by_id'),
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('ajax/', show_ajax, name='show_ajax'),
    path('ajax/submit', create_wishlist, name='create_wishlist'),
]