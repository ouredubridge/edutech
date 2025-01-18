from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Group, Membership, Post

# Create your views here.

# AJAX Request
def is_ajax(request):
    return request.headers.get('x-requested-with') == 'XMLHttpRequest'

def community(request):
    if is_ajax(request):
        return render(request, 'community/partials/community_content.html')
    return render(request, 'community/community.html')

@login_required
def group_list(request):
    groups = Group.objects.all()
    return render(request, 'community/group_list.html', {'groups': groups})

@login_required
def group_detail(request, group_id):
    group = get_object_or_404(Group, id=group_id)
    return render(request, 'community/group_detail.html', {'group': group})


@login_required
def join_group(request, group_id):
    group = get_object_or_404(Group, id=group_id)
    Membership.objects.get_or_create(user=request.user, group=group)
    return redirect('group_detail', group_id=group.id)