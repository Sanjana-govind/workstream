from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # Landing page
    path('signup/', views.signup, name='signup'),  # Signup page
    path('login/', views.login_view, name='login'),  # Login page
    path('logout/', views.logout_view, name='logout'),  # Logout functionality
    path('dashboard/', views.dashboard, name='dashboard'),  # Placeholder after login
    path('add-task/', views.add_task, name='add_task'),
    path('edit-task/<int:task_id>/', views.edit_task, name='edit_task'),
    path('delete-task/<int:task_id>/', views.delete_task, name='delete_task'),
    path('move-task/<int:task_id>/<str:new_status>/', views.move_task, name='move_task'),

    path('urgent-tasks/', views.urgent_tasks, name='urgent_tasks'),
    path('add-urgent-task/', views.add_urgent_task, name='add_urgent_task'),
    path('edit-urgent-task/<int:task_id>/', views.edit_urgent_task, name='edit_urgent_task'),
    path('delete-urgent-task/<int:task_id>/', views.delete_urgent_task, name='delete_urgent_task'),

    path("task-details/<int:task_id>/", views.task_detail, name="task_detail"),
]