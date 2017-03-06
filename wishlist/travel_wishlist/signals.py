from django.db.models.signals import pre_save, post_save, post_delete
from django.dispatch import receiver
from travel_wishlist.models import Place

from django.core.files.storage import default_storage

@receiver(post_delete, sender=Place)
def place_post_delete_image_cleanup(sender, **kwargs):

    place = kwargs['instance']
    # instance is the Place object.
    # The Place object has been deleted from the DB,
    # but still has data in its fields.
    if place.photo:
        if default_storage.exists(place.photo):
            default_storage.delete(place.photo)


@receiver(pre_save, sender=Place)
def place_pre_save_image_cleanup(sender, **kwargs):

    # instance is the Place object, about to be updated
    new_place = kwargs['instance']
    # Can use this to get pk and query DB for previous values
    # Filter by pk and take first item
    old_place = Place.objects.filter(pk=new_place.pk).first()
    # If there's already a place with this pk - so this save is for an update - then
    # check to see if there is a photo, and if so, delete it
    if old_place and old_place.photo:
        if default_storage.exists(old_place.photo):
            print('delete', old_place.photo)
            default_storage.delete(old_place.photo)
