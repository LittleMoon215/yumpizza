from django.contrib import admin

import onlinepizzas.models as model


@admin.register(model.Workers)
class WorkersAdmin(admin.ModelAdmin):
    pass


@admin.register(model.Position)
class PositionAdmin(admin.ModelAdmin):
    pass


@admin.register(model.Pizza)
class PizzaAdmin(admin.ModelAdmin):
    pass


@admin.register(model.OrderDetails)
class OrderDetailsAdmin(admin.ModelAdmin):
    pass


@admin.register(model.User)
class UserAdmin(admin.ModelAdmin):
    pass
