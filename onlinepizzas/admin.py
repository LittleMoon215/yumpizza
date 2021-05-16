from django.contrib import admin

import onlinepizzas.models as model


@admin.register(model.Pizza)
class PizzaAdmin(admin.ModelAdmin):
    pass


@admin.register(model.Drink)
class UserAdmin(admin.ModelAdmin):
    pass


@admin.register(model.Snack)
class UserAdmin(admin.ModelAdmin):
    pass


@admin.register(model.User)
class UserAdmin(admin.ModelAdmin):
    pass


@admin.register(model.Position)
class PositionAdmin(admin.ModelAdmin):
    pass


@admin.register(model.Workers)
class WorkersAdmin(admin.ModelAdmin):
    pass


@admin.register(model.FeedBack)
class PositionAdmin(admin.ModelAdmin):
    pass


@admin.register(model.Product)
class PositionAdmin(admin.ModelAdmin):
    pass


@admin.register(model.Recipe)
class PositionAdmin(admin.ModelAdmin):
    pass


@admin.register(model.DecommissionedProduct)
class PositionAdmin(admin.ModelAdmin):
    pass


@admin.register(model.Distributor)
class PositionAdmin(admin.ModelAdmin):
    pass


@admin.register(model.DistributorOrder)
class PositionAdmin(admin.ModelAdmin):
    pass


@admin.register(model.Order)
class PositionAdmin(admin.ModelAdmin):
    pass
