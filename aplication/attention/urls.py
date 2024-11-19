from django.urls import path
from .views.Attention_hours import *
from .views.medical_appointment import *
from .views.medical_attention import *
# from .views.Requested_exam import *
from .views.Additional_services import *
from .views.quotes import * 
# from .views.care_cost import *
app_name = 'attention'  

urlpatterns = [
    # Attention Hours   
    path('attention_hours_list/', AttentionHoursListView.as_view(), name='attention_hours_list'),
    path('attention_hours/create/', AttentionHoursCreateView.as_view(), name='attention_hours_create'),
    path('attention_hours/update/<int:pk>/', AttentionHoursUpdateView.as_view(), name='attention_hours_update'),
    path('attention_hours/delete/<int:pk>/', AttentionHoursDeleteView.as_view(), name='attention_hours_delete'),
    path('attention_hours/detail/<int:pk>/', AttentionHoursDetailView.as_view(), name='attention_hours_detail'),
    
    # Medical Appointment
    path('medical_appointment/', MedicalAppointmentListView.as_view(), name='medical_appointment_list'),
    path('medical_appointment/create/', MedicalAppointmentCreateView.as_view(), name='medical_appointment_create'),
    path('medical_appointment/update/<int:pk>/', MedicalAppointmentUpdateView.as_view(), name='medical_appointment_update'),
    path('medical_appointment/delete/<int:pk>/', MedicalAppointmentDeleteView.as_view(), name='medical_appointment_delete'),
    path('medical_appointment/detail/<int:pk>/', MedicalAppointmentDetailView.as_view(), name='medical_appointment_detail'),
    
    # Requested Exam
    # path('requested_exam/', RequestedExamListView.as_view(), name='requested_exam_list'),
    # path('requested_exam/create/', RequestedExamCreateView.as_view(), name='requested_exam_create'),
    # path('requested_exam/update/<int:pk>/', RequestedExamUpdateView.as_view(), name='requested_exam_update'),
    # path('requested_exam/delete/<int:pk>/', RequestedExamDeleteView.as_view(), name='requested_exam_delete'),
    # path('requested_exam/detail/<int:pk>/', RequestedExamDetailView.as_view(), name='requested_exam_detail'),
    
    # Additional Services
    path('additional_services_list/', AdditionalServicesListView.as_view(), name='additional_services_list'),
    path('additional_services/create/', AdditionalServicesCreateView.as_view(), name='additional_services_create'),
    path('additional_services/update/<int:pk>/', AdditionalServicesUpdateView.as_view(), name='additional_services_update'),
    path('additional_services/delete/<int:pk>/', AdditionalServicesDeleteView.as_view(), name='additional_services_delete'),
    path('additional_services/detail/<int:pk>/', AdditionalServicesDetailView.as_view(), name='additional_services_detail'), 

    # Medical Attention
    path('attention_list/',AttentionListView.as_view() ,name="attention_list"),
    path('attention_create/', AttentionCreateView.as_view(),name="attention_create"),
    path('attention_update/<int:pk>/', AttentionUpdateView.as_view(),name='attention_update'),
    path('attention_detail/<int:pk>/', AttentionDetailView.as_view(),name='attention_detail'),
    
    # URLs de citas medicas
    path('quote_list/', QuoteListView.as_view(), name="quote_list"),
    path('quote_create/', QuoteCreateView.as_view(), name="quote_create"),
    path('quote_update/<int:pk>/', QuoteUpdateView.as_view(), name='quote_update'),
    path('quote_detail/<int:pk>/', QuoteDetailView.as_view(), name='quote_detail'),
    path('quote_delete/<int:pk>/', QuoteDeleteView.as_view(), name='quote_delete'),
    
    # # URLs de costo atencion
    # path('cost_list/', CostosAtencionListView.as_view(), name="cost_list"),
    # path('cost_create/', CostosAtencionCreateView.as_view(), name="cost_create"),
    # path('cost_update/<int:pk>/', CostosAtencionUpdateView.as_view(), name='cost_update'),
    # path('cost_detail/<int:pk>/', CostosAtencionDetailView.as_view(), name='cost_detail'),
    # path('cost_delete/<int:pk>/', CostosAtencionDeleteView.as_view(), name='cost_delete'),

]