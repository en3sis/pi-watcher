import os
import cloudinary
import cloudinary.uploader
import cloudinary.api
import emoji


def upload_file(file, CONFIG, type='video'):
  cloudinary.config(
      cloud_name=CONFIG['cloud_name'],
      api_key=CONFIG['api_key'],
      api_secret=CONFIG['api_secret']
  )

  print(emoji.emojize(":rocket: Uploading...."))
  response = cloudinary.uploader.upload(file, resource_type=type, use_filename=True,
                                        folder="/pi-watcher/", tags="pi-watcher")
  print(response)
  print(emoji.emojize(":outbox_tray:  Local file removed"))
  os.remove(file)
