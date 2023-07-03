from django.http import HttpResponse

# class CorsMiddleware:
#     def __init__(self, get_response):
#         self.get_response = get_response

#     def __call__(self, request):
#         response = self.get_response(request)
#         self.process_response(request, response)
#         return response

#     def process_response(self, request, response):
#         response["Access-Control-Allow-Origin"] = "http://localhost:3000"  # Replace with your frontend URL
#         response["Access-Control-Allow-Methods"] = "GET, POST, PUT, PATCH, DELETE, OPTIONS"
#         response["Access-Control-Allow-Headers"] = "Content-Type, X-CSRFToken"  # Add any other required headers

#         return response

class CustomCorsMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)

        response["Access-Control-Allow-Origin"] = "http://localhost:3000"
        response["Access-Control-Allow-Methods"] = "GET, POST, PUT, PATCH, DELETE, OPTIONS"
        response["Access-Control-Allow-Headers"] = "Content-Type, X-CSRFToken"
        response.status_code = 200
        return response

