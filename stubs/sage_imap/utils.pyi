from datetime import datetime
from pathlib import Path
from sage_imap.models.email import EmailIterator as EmailIterator, EmailMessage as EmailMessage

def convert_to_local_time(dt: datetime) -> datetime: ...
def read_eml_files_from_directory(directory_path: Path) -> EmailIterator: ...
def read_eml_files_from_zip(zip_path: Path) -> EmailIterator: ...
def is_english(s: str) -> bool: ...
