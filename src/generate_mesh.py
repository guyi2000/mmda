import gmsh
from pathlib import Path


workspace_dir = Path(__file__).parent.parent

gmsh.initialize()
gmsh.model.add("THU_mesh")
gmsh.model.occ.addRectangle(-5, -2, 0, 10, 4, tag=1)


def add_poly(pts, tag):
    p_tags = [gmsh.model.occ.addPoint(p[0], p[1], 0) for p in pts]
    l_tags = [
        gmsh.model.occ.addLine(p_tags[i], p_tags[(i + 1) % len(p_tags)])
        for i in range(len(p_tags))
    ]
    cl = gmsh.model.occ.addCurveLoop(l_tags)
    gmsh.model.occ.addPlaneSurface([cl], tag=tag)


pts_T = [
    [-3.7, 1.2],
    [-3.7, 0.75],
    [-3, 0.75],
    [-3, -1.2],
    [-2.5, -1.2],
    [-2.5, 0.75],
    [-1.8, 0.75],
    [-1.8, 1.2],
]
pts_H = [
    [-1.1, 1.2],
    [-1.1, -1.2],
    [-0.6, -1.2],
    [-0.6, -0.2],
    [0.4, -0.2],
    [0.4, -1.2],
    [0.9, -1.2],
    [0.9, 1.2],
    [0.4, 1.2],
    [0.4, 0.2],
    [-0.6, 0.2],
    [-0.6, 1.2],
]
pts_U = [
    [1.8, -1.2],
    [3.6, -1.2],
    [3.6, 1.2],
    [3.2, 1.2],
    [3.2, -0.75],
    [2.2, -0.75],
    [2.2, 1.2],
    [1.8, 1.2],
]

add_poly(pts_T, 2)
add_poly(pts_H, 3)
add_poly(pts_U, 4)

gmsh.model.occ.cut([(2, 1)], [(2, 2), (2, 3), (2, 4)])
gmsh.model.occ.synchronize()

gmsh.model.mesh.field.add("Distance", 1)
gmsh.model.mesh.field.setNumbers(
    1, "CurvesList", [c[1] for c in gmsh.model.getEntities(1)]
)
gmsh.model.mesh.field.setNumber(1, "Sampling", 100)

gmsh.model.mesh.field.add("Threshold", 2)
gmsh.model.mesh.field.setNumber(2, "InField", 1)
gmsh.model.mesh.field.setNumber(2, "SizeMin", 0.05)
gmsh.model.mesh.field.setNumber(2, "SizeMax", 0.3)
gmsh.model.mesh.field.setNumber(2, "DistMin", 0.1)
gmsh.model.mesh.field.setNumber(2, "DistMax", 0.6)

gmsh.model.mesh.field.setAsBackgroundMesh(2)
gmsh.option.setNumber("Mesh.MeshSizeExtendFromBoundary", 0)
gmsh.option.setNumber("Mesh.MeshSizeFromPoints", 0)
gmsh.option.setNumber("Mesh.MeshSizeFromCurvature", 0)
gmsh.option.setNumber("Mesh.MshFileVersion", 2.2)

gmsh.model.mesh.generate(2)
mesh_path = workspace_dir / "out" / "thu_mesh.msh"
gmsh.write(str(mesh_path))
gmsh.finalize()
