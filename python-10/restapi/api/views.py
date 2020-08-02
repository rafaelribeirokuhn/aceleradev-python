from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import LambdaRequestSerializer
from collections import Counter


@api_view(['POST'])
def lambda_function(request):
    list_of_numbers = request.data['question']
    sorted_numbers = LambdaAPIView.sort_numbers(list_of_numbers)

    solution = {'solution': sorted_numbers}

    return Response(solution)


class LambdaAPIView(APIView):
    def post(self, request):
        serialized_request = LambdaRequestSerializer(data=request.data)

        if not serialized_request.is_valid():
            return Response(serialized_request.errors)

        list_of_numbers = serialized_request.data['question']
        sorted_numbers = self.sort_numbers(list_of_numbers)

        solution = {'solution': sorted_numbers}

        return Response(solution)

    @staticmethod
    def sort_numbers(list_of_numbers):
        return [
            item for items, c in Counter(list_of_numbers).most_common()
            for item in [items] * c
        ]
