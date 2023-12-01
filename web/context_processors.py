# Assuming your models.py file contains a Service model
from .models import Services

def main_context(request):
    services = Services.objects.all()

    context = {
        'service_list': services,
    }

    return context
