from rest_framework import permissions


class IsAuthorOrCollaborator(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.author == request.user or request.user in obj.collaborators.all()
