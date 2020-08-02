from rest_framework.response import Response
from rest_framework.decorators import api_view
from collections import Counter


@api_view(['POST'])
def lambda_function(request):
    list_of_numbers = request.data['question']
    sorted_numbers = sort_numbers(list_of_numbers)

    solution = {'solution': sorted_numbers}

    return Response(solution)


def sort_numbers(list_of_numbers):
    return [
        item for items, c in Counter(list_of_numbers).most_common()
        for item in [items] * c
    ]
