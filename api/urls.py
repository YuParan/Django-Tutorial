from django.urls import path

from api.sample import get_query_string, json_api, upload_form_data

urlpatterns = [
    # (api/)'s urlpatterns
    path('sample/get_query_string', get_query_string.GetQueryString.as_view()),
    path('sample/json_api', json_api.JsonAPI.as_view()),
    path('sample/upload_form_data', upload_form_data.UploadFormData.as_view())
]
