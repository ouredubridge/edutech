from django.shortcuts import render

# Create your views here.

# AJAX Request
def is_ajax(request):
    return request.headers.get('x-requested-with') == 'XMLHttpRequest'

def community(request):
    if is_ajax(request):
        return render(request, 'community/partials/community_content.html')
    return render(request, 'community/community.html')