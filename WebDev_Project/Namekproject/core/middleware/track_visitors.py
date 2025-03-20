#This middleware captures each unique visitor's IP once per day
from datetime import datetime
from core.models import Visitor
from django.utils.deprecation import MiddlewareMixin

class TrackVisitorMiddleware(MiddlewareMixin):
    def process_request(self, request):
        ip = request.META.get('REMOTE_ADDR')
        today = datetime.now().date()

        # Check if the visitor's IP was recorded today
        if ip and not Visitor.objects.filter(ip_address=ip, timestamp__date=today).exists():
            Visitor.objects.create(ip_address=ip)  # No need to manually set timestamp