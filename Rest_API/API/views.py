from rest_framework import viewsets
from .models import Company,Employee
from .serializers import CompanySerializer,EmployeeSerializer
from rest_framework.decorators import action
from rest_framework.response import Response

# Create your views here.

class CompanyViewSet(viewsets.ModelViewSet):
     queryset = Company.objects.all()
     serializer_class = CompanySerializer
     
     @action(detail=True,methods=['get'])
     def employees(self,request,pk=None):
          try:
              company = Company.objects.get(company_id=pk) 
              emp = Employee.objects.filter(company=company)
              emp_serializer = EmployeeSerializer(emp,many=True,context={'request':request}) 
              return Response(emp_serializer.data)
          except Exception as e:
               print(e)
               return Response({
                    'message':'Company Not Found.!! Error !!'
               })
     
     
class EmployeeViewSet(viewsets.ModelViewSet):
     queryset = Employee.objects.all()
     serializer_class = EmployeeSerializer