from rest_framework import generics
from rest_framework.response import Response

from .models import Table
from .serializers import TableSerializer
from .service import PaginationTable


class TableAPIView(generics.ListCreateAPIView):
    queryset = Table.objects.all()
    serializer_class = TableSerializer
    pagination_class = PaginationTable

    def list(self, request, *args, **kwargs):
        filter_column = request.query_params.get('filter_column', None)
        filter_condition = request.query_params.get('filter_condition', None)
        value = request.query_params.get('value', None)  # Value for filter
        sort_column = request.query_params.get('sort_column', None)
        sort_condition = request.query_params.get('sort_condition', None)

        filter_conditions = {
            'equals': '',
            'contains': '__icontains',
            'more': '__gt',
            'less': '__lt',
        }

        if sort_condition == 'decrease':
            sort_column = '-' + sort_column

        if filter_column is not None:
            filter_type = {filter_column + filter_conditions[filter_condition]: value}
            queryset = self.get_queryset().filter(**filter_type).order_by(sort_column)
        else:
            queryset = self.get_queryset()

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
