import numpy as np

import vtkwriters as vtkw

vertices = np.array(
    [
        (-1, -1, 0),
        (1, -1, 0),
        (0, 1, 0),
        (0, 0, 1),
        (0, -1, 0),
    ],
    dtype="d",
)
cells_faces = [
    [
        (0, 4, 1, 2),
        (0, 1, 3),
        (1, 2, 3),
        (2, 0, 3),
    ]
]

doc = vtkw.polyhedra_vtu_doc(
    vertices=vertices,
    cells_faces=cells_faces,
    pointdata={"y": np.ascontiguousarray(vertices[:, 1])},
    celldata={"nbfaces": np.ascontiguousarray([len(f) for f in cells_faces])},
)

vtkw.write_vtu(
    doc,
    "tet_as_polyhedron",
)

vtkw.replace_data(doc, pointdata={"x": np.ascontiguousarray(vertices[:, 1])})

vtkw.write_vtu(
    doc,
    "tet_as_polyhedron_with-x",
)

vtkw.clear_all_data(doc)

vtkw.write_vtu(
    doc,
    "tet_as_polyhedron_no_data",
)
