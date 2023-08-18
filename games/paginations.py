from rest_framework.pagination import PageNumberPagination


class GenrePagination(PageNumberPagination):
    page_size = 2