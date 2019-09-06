from . import volume_distributions


def test_fashion_mnist_distributions():
    # Prepare
    expected_sum = 54_000

    # Execute
    dists = volume_distributions.fashion_mnist_100p()

    # Assert
    assert len(dists) == 10
    for dist in dists:
        assert sum(dist[1]) == expected_sum


def test_cifar_10_distributions():
    # Prepare
    expected_sum = 45_000

    # Execute
    dists = volume_distributions.cifar_10_100p()

    # Assert
    assert len(dists) == 10
    for dist in dists:
        assert sum(dist[1]) == expected_sum