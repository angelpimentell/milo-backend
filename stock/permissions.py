from rest_framework import permissions


class ProductPermissions(permissions.BasePermission):

    def has_permission(self, request, view):
        if request.method == "POST":
            return request.user.has_perm('stock.add_product')
        elif request.method == "PUT":
            return request.user.has_perm('stock.change_product')
        elif request.method == "DELETE":
            return request.user.has_perm('stock.delete_product')
        else:
            return True
