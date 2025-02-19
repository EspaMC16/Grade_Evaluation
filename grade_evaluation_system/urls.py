
from django.urls import path

from . import views

app_name = 'grade_evaluation_system'
urlpatterns = [
    # Home page
    path('', views.home, name='home'),
    # Page that shows the grades evaluation.
    path('grade_evaluation/', views.grade_evaluation, name='grade_evaluation'),
    # Shows the 1st semester.
    path('show_1st_semester/', views.show_1st_semester, name='show_1st_semester'),
    # Shows the 2nd semester.
    path('show_2nd_semester/', views.show_2nd_semester, name='show_2nd_semester'),
    # Shows the searched in search bar.
    path('search_grade/', views.search_grade, name='search_grade'),
]