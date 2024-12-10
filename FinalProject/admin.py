from django.contrib import admin

from .models import (
    Researcher,
    Image,
    ImageGenerated,
    ImageWithGenerated,
    Mask,
    CorruptedImage,
)

admin.site.register(Researcher)
admin.site.register(Image)
admin.site.register(ImageGenerated)
admin.site.register(ImageWithGenerated)
admin.site.register(Mask)
admin.site.register(CorruptedImage)