from dataclasses import dataclass, field
from typing import Dict, Any


@dataclass
class CSVRow:
    data: Dict[str, Any] = field(default_factory=dict)

    def __getitem__(self, key):
        return self.data[key]

    def __setitem__(self, key, value):
        self.data[key] = value

    def __getattr__(self, key):
        try:
            return self.data[key]
        except KeyError:
            raise AttributeError(key)

    """Модель строки CSV. Пока наследует dict, но может быть расширена."""
    pass
