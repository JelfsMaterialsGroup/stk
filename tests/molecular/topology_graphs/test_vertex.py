import stk
import numpy as np


def test_init_vertex_data():
    data = stk.VertexData(1, 2, 3)
    assert all(data.position == [1, 2, 3])
    assert data.edges == []
    assert all(data.cell == [0, 0, 0])


def test_init_at_center():
    vertices = [stk.VertexData(1, 2, 3) for i in range(10)]
    data = stk.VertexData.init_at_center(*vertices)
    assert all(data.position == [1, 2, 3])
    assert data.edges == []
    assert all(data.cell == [0, 0, 0])

    vertices = (stk.VertexData(-1, -2, -3), stk.VertexData(1, 2, 3))
    data = stk.VertexData.init_at_center(*vertices)
    assert all(data.position == [0, 0, 0])
    assert data.edges == []
    assert all(data.cell == [0, 0, 0])


def test_init_vertex():
    vdata = stk.VertexData(1, 2, 3, np.array([10, 4, 2]))
    e1, e2, e3 = (
        stk.EdgeData(vdata), stk.EdgeData(vdata), stk.EdgeData(vdata)
    )
    e1.id = 12
    e2.id = 24
    e3.id = 36
    vertex = stk.Vertex(vdata)

    assert vertex.id is None
    assert all(vertex.get_position() == [1, 2, 3])
    assert list(vertex.get_edge_ids()) == [12, 24, 36]
    assert all(vertex.get_cell() == [10, 4, 2])

    vdata = stk.VertexData(10, 20, 30)
    e1, e2 = stk.EdgeData(vdata), stk.EdgeData(vdata)
    e1.id = 100
    e2.id = 200
    vertex = stk.Vertex(vdata)

    assert vertex.id is None
    assert all(vertex.get_position() == [10, 20, 30])
    assert list(vertex.get_edge_ids()) == [100, 200]
    assert all(vertex.get_cell() == [0, 0, 0])


def test_apply_scale(tmp_vertex):
    initial_position = tmp_vertex.get_position()
    tmp_vertex.apply_scale(2)
    assert all(tmp_vertex.get_position() == initial_position*2)

    initial_position = tmp_vertex.get_position()
    tmp_vertex.apply_scale([2, 4, 3])
    assert all(tmp_vertex.get_position() == initial_position*[2, 4, 3])


def test_clone(vertex):
    clone = vertex.clone()
    assert clone.id == vertex.id
    assert all(clone.get_position() == vertex.get_position())
    assert all(clone.get_cell() == vertex.get_cell())
    assert list(clone.get_edge_ids()) == list(vertex.get_edge_ids())

    clone = vertex.clone(True)
    assert clone.id == vertex.id
    assert all(clone.get_position() == vertex.get_position())
    assert all(clone.get_cell() == vertex.get_cell())
    assert list(clone.get_edge_ids()) != list(vertex.get_edge_ids())
    assert list(clone.get_edge_ids()) == []


def test_get_position():
    vertex = stk.Vertex(stk.VertexData(1, 2, 3))
    assert all(vertex.get_position() == [1, 2, 3])


def test_get_num_edges(vertex):
    assert vertex.get_num_edges() == 3


def test_get_edge_ids(vertex):
    assert list(vertex.get_edge_ids()) == [12, 24, 36]


def test_get_cell(vertex):
    assert all(vertex.get_cell() == [3, 4, 12])


def test_get_edge_centroid():
    assert False


def test_get_edge_plane_normal():
    assert False


def test_get_molecule_centroid():
    assert False