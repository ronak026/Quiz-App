from django.shortcuts import redirect

def access_required(permission):
    def decorator(view_func):
        def wrapper(request, *args, **kwargs):
            if not request.user.is_authenticated:
                return redirect("login")

            profile = request.user.userprofile

            if not getattr(profile, permission):
                return redirect("access_denied")
                
            return view_func(request, *args, **kwargs)
        
        return wrapper
    return decorator
