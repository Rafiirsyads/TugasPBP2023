from django.urls import path
from main.views import add_item_ajax, create_item_flutter, delete_item_ajax, get_item_by_id, get_item_json, show_main
from main.views import show_main, create_item, show_xml, show_json, show_xml_by_id, show_json_by_id 
from main.views import register, login_user, logout_user
from main.views import increase_amount, decrease_amount, delete_item, edit_item_ajax

app_name = 'main'

urlpatterns = [
    path('', show_main, name='show_main'),
    path('create-item', create_item, name='create_item'),
    path('xml/', show_xml, name='show_xml'), 
    path('json/', show_json, name='show_json'), 
    path('xml/<int:id>/', show_xml_by_id, name='show_xml_by_id'),
    path('json/<int:id>/', show_json_by_id, name='show_json_by_id'),
    path('register/', register, name='register'), 
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('increase_amount/<int:item_id>/', increase_amount, name='increase_amount'),
    path('decrease_amount/<int:item_id>/', decrease_amount, name='decrease_amount'),
    path('delete-item/<int:item_id>/', delete_item, name='delete_item'),
    path('edit-item-ajax/<int:id>', edit_item_ajax, name='edit_item_ajax'),
    path('get-item/', get_item_json, name='get_item_json'),
    path('create-item-ajax/', add_item_ajax, name='add_item_ajax'),
    path('delete-item-ajax/<int:item_id>/', delete_item_ajax, name='delete_item_ajax'),
    path('get-item/<int:item_id>/', get_item_by_id, name='get_item_by_id'),
    path('create-flutter/', create_item_flutter, name='create_item_flutter'),
]