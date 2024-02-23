from django.urls import path
from .import views
from .views import CreatePdf, PdfDetail, PdfDeleteView, PdfEditView, DownloadPdfView
from .views import CustomPasswordResetView, CustomPasswordResetDoneView, CustomPasswordResetConfirmView, CustomPasswordResetCompleteView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='home'),
    path('features/', views.features, name='features'),
    path('archive/', views.archive, name='archive'),
    path('pricing/', views.pricing, name='pricing'),
    path('about/', views.about, name='about'),
    path('user/report/', views.report, name='report'),
    path('generate-pdf-report/', views.generate_pdf_report, name='generate-pdf-report'),

    path('profile/', views.profile, name='profile'),
    path('profile/change-password/', views.change_password, name='change-password'),

    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),

    path('login_first/', views.login_first, name='login_first'),

    path('media-files/', views.media_files, name='media-files'),

    path('signup/', views.user_signup, name='signup'),
    path('account_activation/<str:uidb64>/<str:token>/', views.account_activation, name='account_activation'),
    path('forgot_password/', views.forgot_password, name='forgot_password'),

    # Custom Password Reset URLs
    path('password_reset/', CustomPasswordResetView.as_view(), name='custom_password_reset'),
    path('password_reset/done/', CustomPasswordResetDoneView.as_view(), name='custom_password_reset_done'),
    path('reset/<uidb64>/<token>/', CustomPasswordResetConfirmView.as_view(), name='custom_password_reset_confirm'),
    path('reset/done/', CustomPasswordResetCompleteView.as_view(), name='custom_password_reset_complete'),
    path('jpg-to-pdf/', views.jpgtopdf, name='jpg-to-pdf'),
    
    path('pdf-editor/', views.pdf_editor, name='pdf_editor'),
    path('edit/', views.pdf_editor, name='edit_pdf'),
    
    # Map the PdfToWordView to the root URL
    path('pdf-to-word/', views.pdftoword, name='pdf-to-word'),
    path('word-to-pdf/', views.wordtopdf, name='word-to-pdf'),

    path('pdf-to-jpg/', views.pdftojpg, name='pdf-to-jpg'),
    path('password-protect-pdf/', views.passwordprotectpdf, name='password-protect-pdf'),
    path('unlock-pdf/', views.unlockpdf, name='unlock-pdf'),


    path('create-pdf/', CreatePdf.as_view(), name='create-pdf'),
    path('pdf/<int:pk>/', PdfDetail.as_view(), name='pdf-detail'),
    path('pdf/<int:pk>/edit/', PdfEditView.as_view(), name='pdf-edit'),
    path('pdf/<int:pk>/delete/', PdfDeleteView.as_view(), name='pdf-delete'),
    path('pdf/<int:pk>/download/', DownloadPdfView.as_view(), name='pdf-download'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)