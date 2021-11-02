from rest_framework import generics, serializers
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from products.models import Product
from rest_framework.filters import OrderingFilter
from django_filters import rest_framework as filters
from .serializers import ProdutcSerializer
from .filter import ProductFilter


class ProductsApiView(generics.ListAPIView):

    queryset = Product.objects.all()
    serializer_class = ProdutcSerializer
    filter_backends = (filters.DjangoFilterBackend, OrderingFilter)
    filterset_class = ProductFilter
    ordering_fields = ['name', 'price', 'status']


    def post(self, request, *args, **kwargs):
        '''Cria um produto'''
        product = {
            'name': request.data.get('name'),
            'description': request.data.get('description'),
            'price': request.data.get('price'),
            'status': request.data.get('status'),
            'image': request.data.get('image'),
        }

        serializer = ProdutcSerializer(data=product)

        if(serializer.is_valid()):
            product_saved = serializer.save()
            return Response({"success:" "Produto '{}' criado com sucesso !!".format(product_saved.name)}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ProductEditDeleteApiView(APIView):

    def delete(self, request, product_id, *args, **kwargs):
        '''Deleta um produto'''
        product_instance = Product.objects.filter(id=product_id)

        if not product_instance:
            return Response(
                {"res": "Produto com esse id não existe !!"}, status=status.HTTP_404_NOT_FOUND
            )

        product_instance.delete()
        return Response({"success:" "Produto deletado com sucesso !!"}, status=status.HTTP_202_ACCEPTED)

    def put(self, request, product_id, *args, **kwargs):
        '''Edita um produto'''

        product_instance = Product.objects.filter(id=product_id).first()

        if not product_instance:
            return Response(
                {"res": "Produto com esse id não existe !!"}, status=status.HTTP_404_NOT_FOUND)

        product = {}

        name = request.data.get('name')
        description = request.data.get('description')
        price = request.data.get('price')
        status_product = request.data.get('status')
        image = request.data.get('image')

        if name:
            product['name'] = name

        if description:
            product['description'] = description

        if price:
            product['price'] = price

        if status_product:
            product['status'] = status_product

        if image:
            product['image'] = image

        serializer = ProdutcSerializer(
            instance=product_instance, data=product, partial=True)

        if(serializer.is_valid()):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
