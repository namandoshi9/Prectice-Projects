from django.shortcuts import redirect

class StaffMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.path.startswith('/em/'):
            if not request.user.is_authenticated or not request.user.is_staff:
                return redirect('welcom')
        response = self.get_response(request)
        return response

