from django.db.models.functions.base import Lower
from django.db.models.query_utils import Q
from rest_framework.viewsets import ModelViewSet

from instructors.api.serializers import InstructorSerializer
from instructors.models import Instructor
from django.core.paginator import Paginator


class InstructorViewSet(ModelViewSet):
    queryset = Instructor.objects.all()
    serializer_class = InstructorSerializer
#     permission_classes = (IsAuthenticated,)
#     authentication_classes = (TokenAuthentication,)

    draw_page = 0
    register_per_page = 0
    first_record_in_page = 0
    page = 0
    error = ''
    recordTotal = 0
    recordsFiltered = 0
    
    def get_queryset(self):
        self.draw_page = int(self.request.query_params.get('draw'))
        self.registers_per_page = int(self.request.query_params.get('length'))
        self.first_record_in_page = int(self.request.query_params.get('start'))
        self.page = int(self.first_record_in_page / self.registers_per_page) + 1
        self.error = ''
 
        queryset = Instructor.objects.all()
        self.recordsTotal = queryset.count()
        self.recordsFiltered = self.recordsTotal
 
        search_value = self.request.query_params.get('search[value]')
        if search_value:
            queryset = queryset.filter(
                Q(name__icontains=search_value) |
                Q(contact__icontains=search_value)
            )
            self.recordsFiltered = queryset.count()
 
        if self.request.query_params.get('order[0][column]') == '1':
            query_order_by = 'contact'
        elif self.request.query_params.get('order[0][column]') == '2':
            query_order_by = 'about'
        else:
            query_order_by = 'name'
    
        if self.request.query_params.get('order[0][dir]') == 'desc':
            queryset = queryset.order_by(Lower(query_order_by).desc())
        else:
            queryset = queryset.order_by(Lower(query_order_by))
 
#             paginator = Paginator(queryset, registers_per_page)
#             instructors_page = paginator.get_page(page)
#             instructors_list = list(instructors_page.object_list.values())
#  
#             json = {
#                 'draw': draw_page,
#                 'recordsTotal': recordsTotal,
#                 'recordsFiltered': recordsFiltered,
#                 'data': instructors_list,
#                 'error': error
#             }
#  
#             return JsonResponse(json)

        return queryset
        
    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        self.paginator = Paginator(queryset, self.registers_per_page)
        
        #instructors_page = paginator.get_page(self.page)
        #instructors_list = list(instructors_page.object_list.values())
        
        return super().list(request, *args, **kwargs) 
    
    def get_paginated_response(self, data):
        return ModelViewSet.get_paginated_response(self, data)