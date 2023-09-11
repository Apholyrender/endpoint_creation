from django.shortcuts import render

# Create your views here.
from django.http import JsonResponse
from django.utils import timezone

def endpoint_view(request):
    slack_name = request.GET.get('slack_name', 'apholyrender')
    track = request.GET.get('track', 'backend')
    current_day = timezone.now().strftime('%A')
    utc_time = timezone.now().strftime('%Y-%m-%dT%H:%M:%SZ')

    # Replace with your GitHub file and repository URLs
    github_file_url = 'https://github.com/Apholyrender/endpoint_creation/blob/main/endpoint_creation/endpoint_task/apps.py'
    github_repo_url = 'https://github.com/Apholyrender/endpoint_creation'

    response_data = {
        "slack_name": slack_name,
        "current_day": current_day,
        "utc_time": utc_time,
        "track": track,
        "github_file_url": github_file_url,
        "github_repo_url": github_repo_url,
        "status_code": 200
    }

    return JsonResponse(response_data)
