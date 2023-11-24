from discord import User
from django.shortcuts import get_object_or_404, render
from myproject.myapp.models import Major, Project    


def major_list(request):
    majors = Major.objects.all()
    
    return render(request, 'major_list.html', {'majors': majors})

def user_list(request):
    users = User.objects.all()
    sort_by = request.GET.get('sort', 'name')
    project_id = request.GET.get('project')
    major_id = request.GET.get('major')

    
    if project_id:
        project = get_object_or_404(Project, pk=project_id)
        users = users.filter(u_project=project)
    if major_id:
        major = get_object_or_404(Major, pk=major_id)
        users = users.filter(u_major=major)

    if sort_by == 'name':
        users = users.order_by('name')

    searched = request.GET.get('searched', '')
    if searched:
        users = users.filter(name__icontains=searched)

    projects = Project.objects.all()
    majors = Major.objects.all()

    context = {
        'users': users,
        'projects': projects,
        'majors': majors,
        'searched': searched
    }
    return render(request, 'myapp/user_list.html', context)

# def match_users(request, user_id):
#     user_profile = UserProfile.objects.get(pk=user_id)
#     user_ = set(user_profile.interests.split(','))

#     potential_matches = UserProfile.objects.exclude(pk=user_id)
#     matches = []

#     for potential_match in potential_matches:
#         match_interests = set(potential_match.interests.split(','))
#         common_interests = user_interests.intersection(match_interests)

#         if len(common_interests) >= 2:
#             match, created = Match.objects.get_or_create(user=user_profile)
#             match.matched_users.add(potential_match)
#             matches.append(match)

#     return render(request, 'matches.html', {'matches': matches})