from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    parent= models.ForeignKey(
        'self', null=True, blank=True,
        related_name='subcategories', on_delete=models.CASCADE
    )
    icon = models.CharField(max_length=50, blank=True)

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name


class Listing(models.Model):
    class Status(models.TextChoices):
        ACTIVE = 'active', 'Active'
        SOLD = 'sold', 'Sold'
        PENDING = 'pending', 'Pending Review'
        REMOVED = 'removed', 'Removed'

    seller = models.ForeignKey('users.User', on_delete=models.CASCADE, related_name='listings')
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, related_name='listings')
    title = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    location = models.CharField(max_length=100, null=True, blank=True)
    status = models.CharField(max_length=10, choices=Status.choices, default=Status.ACTIVE)
    views_count = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.title

class ListingImage(models.Model):
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='listing_images/')
    is_primary = models.BooleanField(default=False)
    order = models.PositiveSmallIntegerField(default=0)

    def __str__(self):
        return f"Image for {self.listing.title}"