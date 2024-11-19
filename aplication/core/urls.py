from django.urls import path
from aplication.core.views.home import *
from aplication.core.views.patient import *
from aplication.core.views.blood_type import *
from aplication.core.views.specialty import *
from aplication.core.views.employees import *
from aplication.core.views.doctor import *
from aplication.core.views.diagnosis import *
# from aplication.core.views.Category_Exam import *
# from aplication.core.views.Type_Category import *
from aplication.core.views.cargo import *
from aplication.core.views.medicamentos import * 
from aplication.core.views.tipo_med import *
from aplication.core.views.audit import * 
from aplication.core.views.brand_med import *

app_name = 'core'

urlpatterns = [
  # Home
  path('', HomeTemplateView.as_view(), name='home'),

  # Patient URLs
  path('patient_list/', PatientListView.as_view(), name="patient_list"),
  path('patient_create/', PatientCreateView.as_view(), name="patient_create"),
  path('patient_update/<int:pk>/', PatientUpdateView.as_view(), name='patient_update'),
  path('patient_delete/<int:pk>/', PatientDeleteView.as_view(), name='patient_delete'),
  path('patient_detail/<int:pk>/', PatientDetailView.as_view(), name='patient_detail'),

  # Blood Type URLs
  path('blood_type_list/', BloodTypeListView.as_view(), name="blood_type_list"),
  path('blood_type_create/', BloodTypeCreateView.as_view(), name="blood_type_create"),
  path('blood_type_update/<int:pk>/', BloodTypeUpdateView.as_view(), name='blood_type_update'),
  path('blood_type_delete/<int:pk>/', BloodTypeDeleteView.as_view(), name='blood_type_delete'),
  path('blood_type_detail/<int:pk>/', BloodTypeDetailView.as_view(), name='blood_type_detail'),

  # Specialty URLs
  path('specialty_list/', SpecialtyListView.as_view(), name="specialty_list"),
  path('specialty_create/', SpecialtyCreateView.as_view(), name="specialty_create"),
  path('specialty_update/<int:pk>/', SpecialtyUpdateView.as_view(), name='specialty_update'),
  path('specialty_delete/<int:pk>/', SpecialtyDeleteView.as_view(), name='specialty_delete'),

  # Employee URLs
  path('employee_list/', EmployeeListView.as_view(), name="employee_list"),
  path('employee_create/', EmployeeCreateView.as_view(), name="employee_create"),
  path('employee_update/<int:pk>/', EmployeeUpdateView.as_view(), name='employee_update'),
  path('employee_delete/<int:pk>/', EmployeeDeleteView.as_view(), name='employee_delete'),
  path('employee_detail/<int:pk>/', EmployeeDetailView.as_view(), name='employee_detail'),

  # Doctor URLs
  path('doctor_list/', DoctorListView.as_view(), name="doctor_list"),
  path('doctor_create/', DoctorCreateView.as_view(), name="doctor_create"),
  path('doctor_update/<int:pk>/', DoctorUpdateView.as_view(), name='doctor_update'),
  path('doctor_delete/<int:pk>/', DoctorDeleteView.as_view(), name='doctor_delete'),
  path('doctor_detail/<int:pk>/', DoctorDetailView.as_view(), name='doctor_detail'),

  # Diagnosis URLs
  path('diagnosis_list/', DiagnosisListView.as_view(), name="diagnosis_list"),
  path('diagnosis_create/', DiagnosisCreateView.as_view(), name="diagnosis_create"),
  path('diagnosis_update/<int:pk>/', DiagnosisUpdateView.as_view(), name='diagnosis_update'),
  path('diagnosis_delete/<int:pk>/', DiagnosisDeleteView.as_view(), name='diagnosis_delete'),
  path('diagnosis_detail/<int:pk>/', DiagnosisDetailView.as_view(), name='diagnosis_detail'),

  # Category Exam URLs
  #path('category_exam_list/', CategoryExamListView.as_view(), name="category_exam_list"),
  #path('category_exam_create/', CategoryExamCreateView.as_view(), name="category_exam_create"),
  #path('category_exam_update/<int:pk>/', CategoryExamUpdateView.as_view(), name='category_exam_update'),
  #path('category_exam_delete/<int:pk>/', CategoryExamDeleteView.as_view(), name='category_exam_delete'),
  #path('category_exam_detail/<int:pk>/', CategoryExamDetailView.as_view(), name='category_exam_detail'),

  # Type Category URLs
  # path('type_category_list/', TypeCategoryListView.as_view(), name="type_category_list"),
  # path('type_category_create/', TypeCategoryCreateView.as_view(), name="type_category_create"),
  # path('type_category_update/<int:pk>/', TypeCategoryUpdateView.as_view(), name='type_category_update'),
  # path('type_category_delete/<int:pk>/', TypeCategoryDeleteView.as_view(), name='type_category_delete'),
  # path('type_category_detail/<int:pk>/', TypeCategoryDetailView.as_view(), name='type_category_detail'),
  
  # Cargo URLs
    path('cargo_list/', CargoListView.as_view(), name="cargo_list"),
    path('cargo_create/', CargoCreateView.as_view(), name="cargo_create"),
    path('cargo_update/<int:pk>/', CargoUpdateView.as_view(), name="cargo_update"),
    path('cargo_delete/<int:pk>/', CargoDeleteView.as_view(), name="cargo_delete"),
    path('cargo_detail/<int:pk>/', CargoDetailView.as_view(), name='cargo_detail'),  

  # Medicamento URLs
    path('medicamento_list/', MedicamentoListView.as_view(), name="medicamento_list"),
    path('medicamento_create/', MedicamentoCreateView.as_view(), name="medicamento_create"),
    path('medicamento_update/<int:pk>/', MedicamentoUpdateView.as_view(), name="medicamento_update"),
    path('medicamento_delete/<int:pk>/', MedicamentoDeleteView.as_view(), name="medicamento_delete"),
    path('medicamento_detail/<int:pk>/', MedicamentoDetailView.as_view(), name="medicamento_detail"),
    
  # Tipo Medicamento URLs
  path('medicamento_type_list/', TipoMedicamentoListView.as_view(), name="medicamento_type_list"),
  path('medicamento_type_create/', TipoMedicamentoCreateView.as_view(), name="medicamento_type_create"),
  path('medicamento_type_update/<int:pk>/', TipoMedicamentoUpdateView.as_view(), name="medicamento_type_update"),
  path('medicamento_type_delete/<int:pk>/', TipoMedicamentoDeleteView.as_view(), name="medicamento_type_delete"),
  path('medicamento_type_detail/<int:pk>/', TipoMedicamentoDetailView.as_view(), name="medicamento_type_detail"),
  
    # Audit URLs
  path('audit_list/', AuditUserListView.as_view(), name="audit_list"),
  path('audit_detail/<int:pk>/', AuditUserDetailView.as_view(), name='audit_detail'),
  
  # Marca Medicamento
  path('marca_medicamento_list/', MarcaMedicamentoListView.as_view(), name='marca_medicamento_list'),
  path('marca_medicamento_create/', MarcaMedicamentoCreateView.as_view(), name='marca_medicamento_create'),
  path('marca_medicamento_update/<int:pk>/', MarcaMedicamentoUpdateView.as_view(), name='marca_medicamento_update'),
  path('marca_medicamento_delete/<int:pk>/', MarcaMedicamentoDeleteView.as_view(), name='marca_medicamento_delete'),
  path('marca_medicamento_detail/<int:pk>/', MarcaMedicamentoDetailView.as_view(), name='marca_medicamento_detail'),
  
]


