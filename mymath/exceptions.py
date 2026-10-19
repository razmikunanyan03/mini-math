class MathLibError(Exception):
    pass

# === Base module errors ===

class NegativeValueError(MathLibError, ValueError):
    pass

class NonPrimeError(MathLibError, ValueError):
    pass

# === Statistic module errors ===

class EmptyDataError(MathLibError, ValueError):
    pass

class InsufficientDataError(MathLibError, ValueError):
    pass


# === Geometric module errors ===

class GeometricError(MathLibError):
    pass

class InvalidShapeError(GeometricError, ValueError):
    pass

class DegenerateShapeError(GeometricError, ValueError):
    pass
