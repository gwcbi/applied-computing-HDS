"""patientkit -- a minimal example package for Week 7's packaging + debugging exercise.

Deliberately tiny: one function, one planted bug. The point of this package
isn't the code, it's practicing (1) an editable install of a real package and
(2) finding a bug with your IDE's debugger instead of scattered print
statements.
"""

from .stats import summarize_by_site

__all__ = ["summarize_by_site"]
