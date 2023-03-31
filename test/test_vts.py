import numpy as np
import vtkwriters as vtkw

points = np.array(
    [
        (0, 0, 0),
        (1, 1, 0),
        (2, 1, 0),
        (0, 1, 0),
        (1, 2, 0),
        (2, 2, 0),
        (0, 0, 1),
        (1, 1, 1),
        (2, 1, 1),
        (0, 1, 1),
        (1, 2, 1),
        (2, 2, 1),
    ],
    dtype=np.float32,
)

vtkw.write_vts(
    vtkw.vts_doc(
        np.reshape(points, (3, 2, 2, 3)),
        pointdata={
            "x": points[:, 0],
            "y": points[:, 1],
            "z": points[:, 2],
        },
        ofmt="ascii",
    ),
    "structured_grid",
)
