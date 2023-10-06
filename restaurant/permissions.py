from rest_framework import permissions

class IsManager(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.user and request.user.groups.filter(name='Manager'):
            return True
        return False

    
class IsGet(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method == 'GET':
            return True
        return False
    
class IsPost(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method == 'POST':
            return True
        return False
    

class IsPatch(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method == 'PATCH':
            return True
        return False
    
class IsDelete(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method == 'DELETE':
            return True
        return False
    
class IsPut(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method == 'PUT':
            return True
        return False