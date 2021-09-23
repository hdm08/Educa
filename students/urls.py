from	django.urls	import	path
from	.	import	views
from	django.views.decorators.cache	import	cache_page
from django.contrib.auth import views as auth_views

urlpatterns	=	[
    path('register/',
         views.StudentRegistrationView.as_view(),
         name='student_registration'),
    path('enroll-course/',
         views.StudentEnrollCourseView.as_view(),
         name='student_enroll_course'),
    path('courses/',
         views.StudentCourseListView.as_view(),
         name='student_course_list'),
    path('course/<pk>/',
         views.StudentCourseDetailView.as_view(),
         name='student_course_detail'),
    path('course/<pk>/<module_id>/',
         views.StudentCourseDetailView.as_view(),
         name='student_course_detail_module'),
    # path('course/<pk>/',
    #      cache_page(60 * 15)(views.StudentCourseDetailView.as_view()),
    #      name='student_course_detail'),
    # path('course/<pk>/<module_id>/',
    #      cache_page(60 * 15)(views.StudentCourseDetailView.as_view()),
    #      name='student_course_detail_module'),







path('password-reset/',
         auth_views.PasswordResetView.as_view(
             template_name='reset/password_reset.html',
             subject_template_name='reset/password_reset_subject.txt',
             email_template_name='reset/password_reset_email.html',
             success_url='done'
         ),name='password_reset'),

    path('password-reset/done/',
         auth_views.PasswordResetDoneView.as_view(
             template_name='reset/password_reset_done.html'
         ),name='password_reset_done'),

    path('password-reset-confirm/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(
             template_name='reset/password_reset_confirm.html'
         ),name='password_reset_confirm'),

    path('password-reset-complete/',
         auth_views.PasswordResetCompleteView.as_view(
             template_name='reset/password_reset_complete.html'
         ),name='password_reset_complete'),
]