def is_owner(request, obj):
    return request.user == obj.user
