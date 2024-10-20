from django.contrib import admin

from element.models import Element, Product


@admin.action(description="Сбросить задолженность перед поставщиком")
def reset_debt(modeladmin, request, queryset):
    queryset.update(debt=0.00)
    modeladmin.message_user(request, "Задолженности успешно сброшены.")


@admin.register(Element)
class ElementAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "email",
        "country",
        "city",
        "street",
        "number_house",
        "network_level",
        "shipper",
        "debt",
        "created_at",
    )
    search_fields = ("name", "email")
    list_filter = (
        "network_level",
        "created_at",
        "country",
        "city",
    )
    actions = [reset_debt]
    list_display_links = ["shipper", "name"]


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = (
        "shipper",
        "name",
        "product_model",
        "release_date",
    )
    search_fields = ("name", "shipper__name")
    list_filter = (
        "release_date",
        "shipper",
    )
    list_display_links = ["shipper", "name"]
