import os
from channels.routing import ProtocolTypeRouter,URLRouter
from django.core.asgi import get_asgi_application

# Set the default settings module
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "livechat.settings")

# Create the ASGI application instance
django_asgi_app = get_asgi_application()


from channels.auth import AuthMiddlewareStack
from chatapp import routing


# Define the ASGI application with ProtocolTypeRouter
application = ProtocolTypeRouter(
    {
        "http" : get_asgi_application() , 
        "websocket" : AuthMiddlewareStack(
            URLRouter(
                routing.websocket_urlpatterns
            )    
        )
    }
)