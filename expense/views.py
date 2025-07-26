from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from datetime import datetime

# def index(request):
#     now = datetime.now()
#     html = f'''
#     <html>
#         <body>
#             <h1>Hello from Vercel!</h1>
#             <p>The current time is { now }.</p>
#         </body>
#     </html>
#     '''
#     return HttpResponse(html)

def index(request):
    data = {"message": "Hello, world!", 'timestamp': datetime.now()}
    return JsonResponse(data)

#
# from rest_framework.response import Response
# from rest_framework.decorators import api_view
#
# @api_view(['GET'])
# def index(request):
#     return Response({"message": "Hello from DRF!"})