from django.contrib import admin

from .models import Contact, Enquiry, Services, Testimonial,Project



# Register your models here.
@admin.register(Services)
class ServicesAdmin(admin.ModelAdmin):
    list_display = ("service_name", "image", "service_description")


@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    list_display = ("name", "profile_image", "position", "testimonial_content")


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ("name", "phone", "email", "adress", "service", "message")


@admin.register(Enquiry)
class EnquiryAdmin(admin.ModelAdmin):
    list_display = ("full_name", "phone_number", "client_adress", "description")


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    pass