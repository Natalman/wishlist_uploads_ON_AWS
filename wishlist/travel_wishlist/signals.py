from django.db.models.signals import pre_save, post_delete
from django.dispatch import receiver
from travel_wishlist.models import Place

from django.core.files.storage import default_storage

@receiver(post_delete, sender=Place)
def place_post_delete_image_cleanup(sender, **kwargs):

    # kwargs['instance'] is the deleted Place object.
    # The Place object has been deleted from the DB,
    # but the Python Place object still exists, with data in its fields.
    place = kwargs['instance']
    if place.photo:
        if default_storage.exists(place.photo.name):
            default_storage.delete(place.photo.name)


@receiver(pre_save, sender=Place)
def place_pre_save_image_cleanup(sender, **kwargs):

    # Various scenarios:
    # 1. User is adding a new photo. No old photo
    # 2. User is deleting an existing photo (and may or may not modify other data)
    # 3. User is replacing an existing photo (and may or may not modify other data)
    # 4. User is makes other modifications but does not change the photo

    # kwargs['instance'] is the Place object, about to be updated
    new_place = kwargs['instance']
    # Can use this to get pk and query DB for previous values
    # Filter by pk and take first item  [ Not get(), which throws an exception if the item doesn't exist ]
    old_place = Place.objects.filter(pk=new_place.pk).first()
    # If there's already a place with this pk, this save is for an update.

    # Was there an old photo?
    if old_place and old_place.photo:

        # Has the photo changed? If so, delete old one.
        if old_place.photo != new_place.photo:
            if default_storage.exists(old_place.photo.name):
                default_storage.delete(old_place.photo.name)
