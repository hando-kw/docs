from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from django.utils.deconstruct import deconstructible

@deconstructible
class FileSizeValidator:
    def __init__(self, max_size_mb=5):
        self.max_size_mb = max_size_mb
        self.max_size_bytes = max_size_mb * 1024 * 1024  # Convert MB to bytes

    def __call__(self, value):
        if value.size > self.max_size_bytes:
            raise ValidationError(
                _('File size cannot exceed %(max_size)s MB.'),
                params={'max_size': self.max_size_mb}
            )

    def __eq__(self, other):
        return (
            isinstance(other, FileSizeValidator) and
            self.max_size_mb == other.max_size_mb
        )