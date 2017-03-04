from django.db.models.signals import post_save, post_delete
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


@receiver(post_save, sender=Place)
def place_post_save_image_cleanup(sender, **kwargs):

    place = kwargs['instance']
    print(place)
    print(kwargs)

    # How to know
    #logger.info('post save. delete old photo')
