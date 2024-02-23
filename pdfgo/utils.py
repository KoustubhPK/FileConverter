import os
from django.conf import settings

def get_media_files():
    media_root = settings.MEDIA_ROOT
    media_files = []

    for root, dirs, files in os.walk(media_root):
        for file in files:
            media_files.append(os.path.relpath(os.path.join(root, file), media_root))

    return media_files