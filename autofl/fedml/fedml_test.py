import numpy as np
import pytest

from autofl.fedml import fedml


def test_Participant_x_y_shape_valid():
    # Prepare
    m = None
    x = np.zeros((5, 32, 32, 3), dtype=np.uint8)
    y = np.zeros((5), dtype=np.uint8)
    # Execute
    _ = fedml.Participant(m, x, y)
    # pass


def test_Participant_x_y_shape_invalid():
    # Prepare
    m = None
    x = np.zeros((3, 32, 32, 3), dtype=np.uint8)
    y = np.zeros((4), dtype=np.uint8)
    # Execute & assert
    try:
        _ = fedml.Participant(m, x, y)
        pytest.fail("No AssertionError raised")
    except AssertionError:
        pass


def test_federated_averaging():  # pylint: disable=too-many-locals
    # Prepare:
    # - Three weight updates (u0, u1, u2)
    # - Two layers in the model
    # - Two weight tensors in the second layer (e.g. weights + bias)

    u0_l0 = []  # No weights in first layer
    u0_l1_w0 = np.array([[1.0, 2.0, 3.0], [4.0, 5.0, 6.0]])
    u0_l1_w1 = np.ones((2))
    u0_l1 = [u0_l1_w0, u0_l1_w1]
    u0 = [u0_l0, u0_l1]

    u1_l0 = []  # No weights in first layer
    u1_l1_w0 = np.array([[2.0, 3.0, 1.0], [4.0, 5.0, 6.0]])
    u1_l1_w1 = np.ones((2))
    u1_l1 = [u1_l1_w0, u1_l1_w1]
    u1 = [u1_l0, u1_l1]

    u2_l0 = []  # No weights in first layer
    u2_l1_w0 = np.array([[3.0, 1.0, 2.0], [4.0, 5.0, 6.0]])
    u2_l1_w1 = np.ones((2))
    u2_l1 = [u2_l1_w0, u2_l1_w1]
    u2 = [u2_l0, u2_l1]

    thetas = [u0, u1, u2]
    theta_expected = [
        [],
        [np.array([[2.0, 2.0, 2.0], [4.0, 5.0, 6.0]]), np.array([1.0, 1.0])],
    ]

    # Execute
    theta_actual = fedml.federated_averaging(thetas)

    # Assert
    assert len(theta_actual) == len(theta_expected)
    for layer_index, layer in enumerate(theta_actual):
        for weights_index, _ in enumerate(layer):
            w_actual = theta_actual[layer_index][weights_index]
            w_expected = theta_expected[layer_index][weights_index]
            np.testing.assert_array_equal(w_actual, w_expected)
