from django.shortcuts import render

def index_view(request):
    context = {
        "project_name": "SmartStock API",
        "description": "REST API backend of the service that allows for efficient warehouse product management, inventory control, order processing, delivery, and analytics.",
        "author": "Jamoliddin, 2025-yil",
        "github_url": "https://github.com/xterraname/smart-stock",
        "swagger_url": "/api/docs/",
    }
    return render(request, "index.html", context)
