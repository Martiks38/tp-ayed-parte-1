"""
  Valida que la fecha esté en formato estándar segun ISO 86011
"""

import re


def validate_date(date):
    patron = r"^\d{4}-\d{2}-\d{2}$"
    return re.match(patron, date)
