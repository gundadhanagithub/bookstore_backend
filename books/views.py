from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from books.models import Books
from books.serializers import BookSerializer
import logging

logger = logging.getLogger(__name__)

@csrf_exempt
def books_list(request):
    
    try:
        if request.method == 'GET' and request.GET:
            include_out_of_stock = request.GET.get('includeOutOfStock', False)
            query_params = request.GET.copy()
            query_params.pop('includeOutOfStock', None)
            genres = query_params.getlist('genre')
            if genres.__len__() > 0:
                if include_out_of_stock == 'true':
                    books = Books.objects.filter(stock__gt=0, genre__in=genres)
                    serializer = BookSerializer(books, many=True)
                else:
                    books = Books.objects.filter(stock=0, genre__in=genres)
                    serializer = BookSerializer(books, many=True)
                return JsonResponse(serializer.data, safe=False)
            else:
                if include_out_of_stock == 'true':
                    books = Books.objects.filter()
                    serializer = BookSerializer(books, many=True)
                else:
                    books = Books.objects.filter(stock__gt=0)
                    serializer = BookSerializer(books, many=True)
                return JsonResponse(serializer.data, safe=False)

        if request.method == 'GET':
            books = Books.objects.all()
            logger.info(books)
            serializer = BookSerializer(books, many=True)
            return JsonResponse(serializer.data, safe=False)

        elif request.method == 'POST':
            data = JSONParser().parse(request)
            serializer = BookSerializer(data=data)
            if serializer.is_valid():
                serializer.save()
                return JsonResponse(serializer.data, status=201)
            return JsonResponse(serializer.errors, status=400)
    except Exception as e:
        logger.error(e)
        return JsonResponse({'error': str(e)}, status=500)
    
@csrf_exempt
def book_detais(request, pk):
    
    try:
        book = Books.objects.get(pk=pk)
    except Books.DoesNotExist:
        return HttpResponse(status=404)

    try:
        if request.method == 'GET':
            serializer = BookSerializer(book)
            return JsonResponse(serializer.data)
    
    except Exception as e:
        logger.error(e)
        return JsonResponse({'error': str(e)}, status=500)
    
    