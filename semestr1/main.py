from dyn_array import DynArray


def main():
    arr = DynArray()
    print()

    print("Начальный массив: ", arr)
    print("size(): ", arr.size())
    print("capacity(): ", arr.capacity())
    print()

    arr.append(10)
    print("После append(10): ", arr)
    print()

    arr.append(20)
    print("После append(20): ", arr)
    print()

    arr.append(30)
    print("После append(30): ", arr)
    print("size(): ", arr.size())
    print("capacity(): ", arr.capacity())
    print()

    print("get(1):", arr.get(1))
    print()

    arr.set(1, 25)
    print("После set(1, 25):", arr)
    print()

    arr.insert(1, 15)
    print("После insert(1, 15):", arr)
    print()

    removed = arr.remove_at(2)
    print("remove_at(2):", removed)
    print("После remove_at(2):", arr)
    print()

    print("size():", arr.size())
    print()

    print("capacity():", arr.capacity())

if __name__ == "__main__":
    main()
