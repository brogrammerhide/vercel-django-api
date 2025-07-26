from django.contrib import admin
from django.urls import path, include
from django.urls import re_path
from django.conf import settings
from core.views import serve_nextjs_index
from django.views.static import serve

urlpatterns = [
    path('', serve_nextjs_index),
    path('admin/', admin.site.urls),
    path('expense/', include('expense.urls')),
]

urlpatterns += [
    re_path(r'^_next/(?P<path>.*)$', serve, {
        'document_root': settings.BASE_DIR / 'static/_next',
    }),
]

# from django.conf import settings
# from django.conf.urls.static import static
# from django.urls import path
# from django.views.generic import TemplateView
#
# urlpatterns = [
#     # Optionally, serve your Next.js index.html as a template view
#     path('', TemplateView.as_view(template_name="index.html"), name='home'),
#     # Other URL patterns...
# ]
#
# if settings.DEBUG:
#     urlpatterns += static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS[0])