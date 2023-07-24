from django.http import HttpResponse, JsonResponse
def home_page(request):
    print("home page requested")
    friends = [
        'umesh',
        'chetan',
        'jayesh',
        'prahci'
    ]
    return JsonResponse(friends, safe=False)
