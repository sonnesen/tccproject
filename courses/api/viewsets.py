from _collections import OrderedDict

from django.db.models.functions.text import Lower
from django.db.models.query_utils import Q
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from courses.api.serializers import DocumentSerializer, CourseSerializer, \
    VideoSerializer, ExamSerializer, UnitSerializer, QuestionSerializer, \
    InstructorSerializer, AlternativeSerializer, CategorySerializer
from courses.models import Document, Course, Video, Exam, Unit, Question, \
    Instructor, Alternative, Category


class DocumentViewSet(ModelViewSet):
    queryset = Document.objects.all()
    serializer_class = DocumentSerializer


class CourseViewSet(ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
#     permission_classes = (IsAuthenticated,)
#     authentication_classes = (TokenAuthentication,)

    error = ''
    recordTotal = 0
    recordsFiltered = 0
    
    def get_queryset(self):
        # requirido pelo datatables.js
        self.draw_page = int(self.request.query_params.get('draw', 0))
        
        queryset = Course.objects.all()
        self.recordsTotal = queryset.count()
        self.recordsFiltered = self.recordsTotal
 
        search_value = self.request.query_params.get('search[value]')
        if search_value:
            queryset = queryset.filter(
                Q(name__icontains=search_value) | 
                Q(category__name__icontains=search_value) | 
                Q(instructor__name__icontains=search_value) | 
                Q(description__icontains=search_value)
            )
            self.recordsFiltered = queryset.count()
 
        if self.request.query_params.get('order[0][column]'):
            query_order_by = self.request.query_params.get(
                'columns[{}][data]'.format(
                    self.request.query_params.get('order[0][column]'))
                )
        else:
            query_order_by = 'name'
            
        query_order_by = query_order_by.replace('.', '__')    
    
        if self.request.query_params.get('order[0][dir]') == 'desc':
            queryset = queryset.order_by(Lower(query_order_by).desc())
        else:
            queryset = queryset.order_by(Lower(query_order_by))

        return queryset
        
    def list(self, request, *args, **kwargs):
        if request.query_params.get('length'):
            # listagem utilizando paginação do datatables.js
            registers_per_page = int(request.query_params.get('length'))
            first_record_in_page = int(request.query_params.get('start', 0))
            request.query_params._mutable = True       
            request.query_params['page'] = int(
                first_record_in_page / registers_per_page) + 1
            request.query_params._mutable = False
        
        self.pagination_class = PageNumberPagination             
        queryset = self.filter_queryset(self.get_queryset())
        paginator = PageNumberPagination()
        paginator.page_size_query_param = 'length'
        courses_page = paginator.paginate_queryset(queryset, request)
        
        if courses_page is not None:
            serializer = self.get_serializer(courses_page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
    
    def get_paginated_response(self, data):
        return Response(OrderedDict([
                ('draw', self.draw_page),
                ('recordsTotal', self.recordsTotal),
                ('recordsFiltered', self.recordsFiltered),
                ('data', data),
                ('error', self.error)                
            ]))

    
class VideoViewSet(ModelViewSet):
    queryset = Video.objects.all()
    serializer_class = VideoSerializer  

    
class ExamViewSet(ModelViewSet):
    queryset = Exam.objects.all()
    serializer_class = ExamSerializer

    
class UnitViewSet(ModelViewSet):
    queryset = Unit.objects.all()
    serializer_class = UnitSerializer  

    
class QuestionViewSet(ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer

    
class InstructorViewSet(ModelViewSet):
    queryset = Instructor.objects.all()
    serializer_class = InstructorSerializer
#     permission_classes = (IsAuthenticated,)
#     authentication_classes = (TokenAuthentication,)

    error = ''
    recordTotal = 0
    recordsFiltered = 0
    
    def get_queryset(self):
        # requirido pelo datatables.js
        self.draw_page = int(self.request.query_params.get('draw', 0))
        
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
 
        if self.request.query_params.get('order[0][column]'):
            query_order_by = self.request.query_params.get(
                'columns[{}][data]'.format(
                    self.request.query_params.get('order[0][column]'))
                )
        else:
            query_order_by = 'name'
    
        if self.request.query_params.get('order[0][dir]') == 'desc':
            queryset = queryset.order_by(Lower(query_order_by).desc())
        else:
            queryset = queryset.order_by(Lower(query_order_by))

        return queryset
        
    def list(self, request, *args, **kwargs):
        if request.query_params.get('length'):
            # listagem utilizando paginação do datatables.js
            registers_per_page = int(request.query_params.get('length'))
            first_record_in_page = int(request.query_params.get('start', 0))
            request.query_params._mutable = True       
            request.query_params['page'] = int(
                first_record_in_page / registers_per_page) + 1
            request.query_params._mutable = False
        
        self.pagination_class = PageNumberPagination             
        queryset = self.filter_queryset(self.get_queryset())
        paginator = PageNumberPagination()
        paginator.page_size_query_param = 'length'
        instructors_page = paginator.paginate_queryset(queryset, request)
        
        if instructors_page is not None:
            serializer = self.get_serializer(instructors_page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
    
    def get_paginated_response(self, data):
        return Response(OrderedDict([
                ('draw', self.draw_page),
                ('recordsTotal', self.recordsTotal),
                ('recordsFiltered', self.recordsFiltered),
                ('data', data),
                ('error', self.error)                
            ]))   

        
class AlternativeViewSet(ModelViewSet):
    """
    Classe responsável pela visualização de um objeto do tipo Alternative
    """

    queryset = Alternative.objects.all()
    serializer_class = AlternativeSerializer     

    
class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
#     permission_classes = (IsAuthenticated,)
#     authentication_classes = (TokenAuthentication,)

    error = ''
    recordTotal = 0
    recordsFiltered = 0
    
    def get_queryset(self):
        # requirido pelo datatables.js
        self.draw_page = int(self.request.query_params.get('draw', 0))
        
        queryset = Category.objects.all()
        self.recordsTotal = queryset.count()
        self.recordsFiltered = self.recordsTotal
 
        search_value = self.request.query_params.get('search[value]')
        if search_value:
            queryset = queryset.filter(
                Q(name__icontains=search_value) | 
                Q(contact__icontains=search_value)
            )
            self.recordsFiltered = queryset.count()
 
        if self.request.query_params.get('order[0][column]'):
            query_order_by = self.request.query_params.get(
                'columns[{}][data]'.format(
                    self.request.query_params.get('order[0][column]'))
                )
        else:
            query_order_by = 'name'
    
        if self.request.query_params.get('order[0][dir]') == 'desc':
            queryset = queryset.order_by(Lower(query_order_by).desc())
        else:
            queryset = queryset.order_by(Lower(query_order_by))

        return queryset
        
    def list(self, request, *args, **kwargs):
        if request.query_params.get('length'):
            # listagem utilizando paginação do datatables.js
            registers_per_page = int(request.query_params.get('length'))
            first_record_in_page = int(request.query_params.get('start', 0))
            request.query_params._mutable = True       
            request.query_params['page'] = int(
                first_record_in_page / registers_per_page) + 1
            request.query_params._mutable = False
        
        self.pagination_class = PageNumberPagination             
        queryset = self.filter_queryset(self.get_queryset())
        paginator = PageNumberPagination()
        paginator.page_size_query_param = 'length'
        categories_page = paginator.paginate_queryset(queryset, request)
        
        if categories_page is not None:
            serializer = self.get_serializer(categories_page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
    
    def get_paginated_response(self, data):
        return Response(OrderedDict([
                ('draw', self.draw_page),
                ('recordsTotal', self.recordsTotal),
                ('recordsFiltered', self.recordsFiltered),
                ('data', data),
                ('error', self.error)                
            ]))        
