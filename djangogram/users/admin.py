from django.contrib import admin
from django.contrib.auth import admin as auth_admin
from django.contrib.auth import get_user_model

from djangogram.users.forms import UserChangeForm, UserCreationForm

User = get_user_model()


@admin.register(User)
class UserAdmin(auth_admin.UserAdmin):

    form = UserChangeForm
    add_form = UserCreationForm
    fieldsets = (("User", {"fields": ("name","following",)}),) + auth_admin.UserAdmin.fieldsets
    list_display = ["username", "name", "is_superuser"]
    search_fields = ["name"]




# from django.contrib import admin
# from django.contrib.auth import admin as auth_admin
# from django.contrib.auth import get_user_model
# from django.utils.translation import gettext_lazy as _

# from djangogram.users.forms import UserAdminChangeForm, UserAdminCreationForm

# User = get_user_model()


# @admin.register(User)
# class UserAdmin(auth_admin.UserAdmin):

#     form = UserAdminChangeForm
#     add_form = UserAdminCreationForm
#     fieldsets = (
#         (None, {"fields": ("username", "password")}),
#         (_("Personal info"), {"fields": ("name", "email")}),
#         (
#             _("Permissions"),
#             {
#                 "fields": (
#                     "is_active",
#                     "is_staff",
#                     "is_superuser",
#                     "groups",
#                     "user_permissions",
#                 ),
#             },
#         ),
#         (_("Important dates"), {"fields": ("last_login", "date_joined")}),
#     )
#     list_display = ["username", "name", "is_superuser"]
#     search_fields = ["name"]
