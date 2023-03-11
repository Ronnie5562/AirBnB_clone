#!/usr/bin/python3
"""_summary_
    This module creates a storage object from the Filestore class which reloads objects to file.json
"""

from models.engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()