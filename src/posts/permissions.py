from rest_framework import permissions

class IsAuthorOrReadonly(permissions.BasePermission):
    def has_permission(self, request, view):
        #user has to be authenticated first to view any view detailed/list
        if request.user.is_authenticated:
            return True
        return False

    def has_object_permission(self, request, view, obj):
        #if user is authenticated,he can view any object but not edit/delete
        if request.method in permissions.SAFE_METHODS:
            return True

        # Write permissions are only allowed to the author of a post here
        return obj.author == request.user

    