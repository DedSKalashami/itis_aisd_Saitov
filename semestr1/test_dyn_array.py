from dyn_array import DynArray


def test_append():
    arr = DynArray()
    arr.append(10)
    arr.append(20)
    assert arr.size() == 2
    assert arr.get(0) == 10
    assert arr.get(1) == 20


def test_get():
    arr = DynArray()
    arr.append(100)
    assert arr.get(0) == 100


def test_set():
    arr = DynArray()
    arr.append(5)
    arr.set(0, 50)
    assert arr.get(0) == 50


def test_insert():
    arr = DynArray()
    arr.append(10)
    arr.append(20)
    arr.append(30)
    arr.insert(1, 15)

    assert arr.size() == 4
    assert arr.get(0) == 10
    assert arr.get(1) == 15
    assert arr.get(2) == 20
    assert arr.get(3) == 30


def test_remove_at():
    arr = DynArray()
    arr.append(10)
    arr.append(15)
    arr.append(20)
    arr.append(30)

    removed = arr.remove_at(2)
    assert removed == 20
    assert arr.size() == 3
    assert arr.get(0) == 10
    assert arr.get(1) == 15
    assert arr.get(2) == 30


def test_size():
    arr = DynArray()
    assert arr.size() == 0
    arr.append(1)
    arr.append(2)
    assert arr.size() == 2


def test_capacity():
    arr = DynArray(2)
    assert arr.capacity() == 2
    arr.append(1)
    arr.append(2)
    arr.append(3)
    assert arr.capacity() == 4

def run_all_tests():
    test_append()
    print("test_append passed")

    test_get()
    print("test_get passed")

    test_set()
    print("test_set passed")

    test_insert()
    print("test_insert passed")

    test_remove_at()
    print("test_remove_at passed")

    test_size()
    print("test_size passed")

    test_capacity()
    print("test_capacity passed")

    print("Все тесты прошли успешно!")


if __name__ == "__main__":
    run_all_tests()
