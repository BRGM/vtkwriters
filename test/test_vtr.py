import numpy as np
import vtkwriters as vtkw

vtkw.write_vtr(
    vtkw.vtr_doc(
        (np.arange(4), np.logspace(0, 1, 5), (0, 0.2, 1, 3, 4)),
        ofmt="ascii",
    ),
    "rectilinear_grid",
)
