from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("api/jobs/", include("jobs.urls")),
    path("api/filters/", include("filters.urls")),
    path("accounts/", include("accounts.urls")),
    path("api/accounts/", include("accounts.api_urls")),
    path("admin/", admin.site.urls),
    path("__debug__/", include("debug_toolbar.urls")),
]