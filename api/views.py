from rest_framework import status
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from rest_framework import generics
from store.models import *
from .serializers import *


class StoreAPI(generics.ListAPIView):
    queryset = Store.objects.all()
    serializer_class = StoreSerializer

class ProductAPI(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class StoreDetailAPI(generics.ListAPIView):
    serializer_class = StoreDetailSerializer
    
    def get_queryset(self):
        item = self.kwargs['pk']
        queryset = StoreContent.objects.filter(Store = item)
        return queryset

@csrf_exempt
@api_view(['GET','POST'])
def StoreAddAPI(request,pk):
    data = request.data
    if request.method == 'POST':  
        data['Store'] = pk 
        store = Store.objects.get(id = data['Store'])
        product = Product.objects.get(id = data['Product']) 
        count = data['Count']
        print('This is POST.data '+ str(data)) 
        if StoreContent.objects.filter(Store = store, Product = product).exists():
            serializer = StoreDetailAddSerializer(data=data)
            if serializer.is_valid():
                content = StoreContent.objects.get(Store = store, Product = product)
                content.Count += int(count)
                content.save() 
                serializer.save()    
                return Response(serializer.data, status=201)
            return Response(serializer.errors, status=400)
        else:
            serializer = StoreDetailAddSerializer(data=data)
            if serializer.is_valid():
                content = StoreContent(Store = store, Product = product, Count = count)
                content.save() 
                serializer.save()    
                return Response(serializer.data, status=201)
            return Response(serializer.errors, status=400)
    else :
        example = {"example of request":"{'Product:4','Count: 100'}"}
        print('This is request.data '+ str(data))
        return Response(example)

@csrf_exempt
@api_view(['GET','POST'])
def StoreBuyAPI(request,pk):
    data = request.data
    if request.method == 'POST':
        data['Store'] = pk 
        store = Store.objects.get(id = data['Store'])
        product = Product.objects.get(id = data['Product']) 
        count = data['Count']
        print('This is POST.data '+ str(data)) 
        if StoreContent.objects.filter(Store = store, Product = product).exists():
            content = StoreContent.objects.get(Store = store, Product = product)
            if content.Count > count:
                serializer = StoreDetailBuySerializer(data=data)
                if serializer.is_valid():
                    content.Count -= int(count)
                    content.save() 
                    serializer.save()    
                    return Response(serializer.data, status=201)
                return Response(serializer.errors, status=400)
            elif content.Count == count:
                serializer = StoreDetailBuySerializer(data=data)
                if serializer.is_valid():
                    StoreContent.objects.filter(Store = store, Product = product).delete()
                    serializer.save()    
                    return Response(serializer.data, status=201)
                return Response(serializer.errors, status=400) 
            else:
                return Response(status=400)
    else :
        example = {"example of request":"{'Product:4','Count: 100'}"}
        print('This is request.data '+ str(data))
        return Response(example)


@api_view(['GET'])
def APIOverview(request):
    APIList = {
    'List of Stores':'api/',
    'List of registered Products':'api/product',
    'Store Product List':'api/<int:pk>/', 
    'Add product to Store':'api/<int:pk>/add/  example of request: [{"Product": 4,"Count": 100}]' ,
    'Buy product from Store':'api/<int:pk>/buy/ example of request: [{"Product": 4,"Count": 21}]',
    }
    return Response(APIList)
