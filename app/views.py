from .models import Price
from .serializers import PriceSerializer
from finantial_indicators.tasks import async_calculate_synthetic_index
from finantial_indicators.synthetic_index import get_synthetic_index
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework import viewsets, status, mixins
import pandas as pd


class PriceViewSet(ModelViewSet):
    """
    Allows individual access, creation and modification to Price object
    """
    model = Price
    serializer_class = PriceSerializer
    queryset = model.objects.all()


class StorePrices( mixins.CreateModelMixin, viewsets.GenericViewSet):
    """
    View set for bulk Prices data
    """
    model = Price
    serializer_class = PriceSerializer
    queryset = model.objects.all()

    def create(self, request):
        """
        Create a list of prices  given by a .csv file
        """
        # Read data from file and normalized Data
        file = request.data['file']
        df = pd.read_csv(file, sep=';')
        validated_data = df.to_dict('records')

        # Normalized and insert and bulk data DB
        for item in validated_data:
            data_serializer = self.serializer_class(data=item)
            if data_serializer.is_valid():
                data_serializer.save()
            else:
                return Response("Wrong data format for entry {}".format(item),
                                status=status.HTTP_400_BAD_REQUEST)

        # TEST without async
        # price_series = get_synthetic_index(self.queryset)
        price_series = async_calculate_synthetic_index(self.queryset)

        return Response(price_series,status=status.HTTP_200_OK)


class SyntheticIndex(mixins.ListModelMixin, viewsets.GenericViewSet):
    """
    View set for bulk Prices data
    """
    model = Price
    serializer_class = PriceSerializer
    queryset = model.objects.all()

    def list(self, request):
        price_series = get_synthetic_index(self.queryset)
        return Response(price_series,status=status.HTTP_200_OK)
