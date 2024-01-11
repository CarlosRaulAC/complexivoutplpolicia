from django.urls import path
from .views import PersonalView, PersonalAdd, PersonalUpdate, personal_inactivate

urlpatterns = [

    #url para vehiculos
    path('policial/',PersonalView.as_view(), name='policial_list'),
    path('policial/add',PersonalAdd.as_view(), name='policial_add'),
    path('policial/update/<int:pk>',PersonalUpdate.as_view(), name='policial_update'),
    path('policial/inactivate/<int:id>',personal_inactivate, name='policial_inactivate'),

]