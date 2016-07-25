===================
django-random-image
===================

django-random-image is a simple django app for using an image randomly from a user-defined set of ``django-filer``
images in a django template. Every image is only active during a time range set for it.

Requires ``django-filer``.

Quick start
-----------
1. Install with your favorite tool
2. Add ``'random_image'`` to ``INSTALLED_APPS``.
3. Migrate your database.
4. You can now add images in the admin under ``Random images``.
5. Add ``{% load random_image %}`` to your template of choice and use ``{% random_image as image %}`` to load a randomly selected image into the ``image`` template variable.
