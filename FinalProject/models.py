
from django.db import models
from django.contrib.auth.models import User
from django.utils.safestring import mark_safe
from django.utils import timezone
from django.urls import reverse

# Model for Researcher
class Researcher(models.Model):
    """
    Represents a researcher with basic details like name, email, and associated university.
    This model is related to the User model to extend user functionality.
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="researcher_profile")
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    university = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.user.username})"

# Model for Mask
class Mask(models.Model):
    """
    Represents a mask file used for image processing in research. It includes a reference to the 
    researcher who created it.
    """
    mask_file = models.ImageField(upload_to="masks/")
    researcher = models.ForeignKey(Researcher, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Mask {self.pk}"

# Model for CorruptedImage
class CorruptedImage(models.Model):
    """
    Represents a corrupted image used in the research. It includes a reference to the researcher
    who uploaded the corrupted image.
    """
    corrupted_file = models.ImageField(upload_to="corrupted_images/")
    researcher = models.ForeignKey(Researcher, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Corrupted Image {self.pk}"

# Model for Image
class Image(models.Model):
    """
    Represents a regular image uploaded by a researcher. This can be used as an original image or 
    part of research in conjunction with masks or corrupted images.
    """
    image_file = models.ImageField(upload_to='images/')
    researcher = models.ForeignKey('Researcher', on_delete=models.CASCADE)
    uploaded_at = models.DateTimeField(default=timezone.now)
    mask = models.ForeignKey(Mask, null=True, blank=True, related_name="masked_images", on_delete=models.SET_NULL)
    corrupted_image = models.ForeignKey(CorruptedImage, null=True, blank=True, related_name="corrupted_images", on_delete=models.SET_NULL)

    def __str__(self):
        return f"Image {self.pk} - {self.researcher.user.username}"

# Model for ImageGenerated
class ImageGenerated(models.Model):
    """
    Represents a generated image produced by applying an imputation method to a corrupted image.
    """
    image_file = models.ImageField(upload_to='images/generated/')
    imputation_method = models.CharField(max_length=200)
    ssim_value = models.FloatField(null=True, blank=True)
    psnr_value = models.FloatField(null=True, blank=True)
    researcher = models.ForeignKey(Researcher, on_delete=models.CASCADE, related_name="generated_images")
    image = models.ForeignKey(Image, on_delete=models.CASCADE)

    def __str__(self):
        return f"Generated Image {self.pk} - {self.imputation_method}"

# Model linking Original Image to Generated Image
class ImageWithGenerated(models.Model):
    """
    Links an original image to a generated image for easy tracking.
    """
    original = models.ForeignKey(Image, on_delete=models.CASCADE, related_name="generated_images")
    generated = models.ForeignKey(ImageGenerated, on_delete=models.CASCADE, related_name="original_image")

    def __str__(self):
        return f"Original {self.original.pk} -> Generated {self.generated.pk}"
