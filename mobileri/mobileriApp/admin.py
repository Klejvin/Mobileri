from django.contrib import admin
from .models import*

# Register your models here.

# Kjo klasë thotë: "Merr fushat e klasës Fotot dhe bëji gati për t'u plotësuar"
class FototInline(admin.TabularInline):
    model = Fotot
    extra = 10  # Kjo të nxjerr 10 rreshta bosh menjëherë

@admin.register(Produkti)
class ProduktiAdmin(admin.ModelAdmin):
    list_display = ['emri', 'kategoria', 'cmimi']
    # KJO është pika ku bashkohen dy klasat në një faqe të vetme
    inlines = [FototInline]


admin.site.register(Kategoria)
admin.site.register(Fotot)

