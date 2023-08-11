from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name="index"),
    path('sign-up', views.sign_up, name="sign-up"),
    path('login', views.login, name="login"),
    path('logout', views.logout, name="logout"),
    path('users', views.users, name="users"),
    path('add-farm-details', views.add_farm_details, name="add-farm-details"),
    path('farm-detail-view', views.farm_detail_view, name="farm-detail-view"),
    path('request-for-delete/<int:id>', views.request_for_delete, name="request-for-delete"),
    path('delete/<int:id>', views.delete, name="delete"),
    path('farm-update/<int:id>', views.farm_update, name="farm-update"),
    path('update-farm/<int:id>', views.update_farm, name="update-farm"),
    path('update-user/<int:id>', views.update_user, name="update-user"),
    path('user-update/<int:id>', views.user_update, name="user-update"),
    
    # officer and farmer section
    path('add-officer-farmer', views.add_officer_farmer, name="add-officer-farmer"),
    path('farmer-view', views.farmer_view, name="farmer-view"),
    path('officer-view', views.officer_view, name="officer-view"),
    path('add-visit/<int:id>', views.add_visit, name="add-visit"),
    path('add-visit2/<int:id>', views.add_visit2, name="add-visit"),
    path('asign-farm/<int:id>', views.asign_form, name="asign-farm"),
    path('asign-farm2/<int:id>', views.asign_form2, name="asign-farm2"),
    path('request-for-delete2/<int:id>', views.request_for_delete2, name="request-for-delete2"),
    path('request-for-delete3/<int:id>', views.request_for_delete3, name="request-for-delete3"),
    path('delete2/<int:id>', views.delete2, name="delete2"),
    path('delete3/<int:id>', views.delete3, name="delete3"),

    # History
    path('history', views.visit_history, name="history"),
    
]