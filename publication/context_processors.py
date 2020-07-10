from .models import Series

def seria(request):
    return {'series':Series.objects.all()}