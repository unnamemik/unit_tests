import unittest

from car import Car
from motorcycle import Motorcycle


class VehicleTest(unittest.TestCase):
    def setUp(self) -> None:
        self.car = Car("Toyota", "Camry", 2022)
        self.moto = Motorcycle("Yamaha", "FZ-6N", 2007)

    # - Проверить, что экземпляр объекта Car также является экземпляром транспортного средства (используя оператор instanceof)
    def test_car_instance_check(self):
        self.assertIsInstance(self.car, Car)

    # - Проверить, что объект Car создается с 4-мя колесами.
    def test_car_wheels_check(self):
        self.assertEqual(self.car.get_num_wheels(), 4)

    # - Проверить, что объект Car создается с 2-мя колесами.
    def test_moto_wheels_check(self):
        self.assertEqual(self.moto.get_num_wheels(), 2)

    # - Проверить, что объект Car развивает скорость 60 в режиме тестового вождения (используя метод testDrive()).
    def test_car_speed_check(self):
        self.car.test_drive()
        self.assertEqual(self.car.get_speed(), 60)

    # - Проверить, что объект Moto развивает скорость 75 в режиме тестового вождения (используя метод testDrive()).
    def test_moto_speed_check(self):
        self.moto.test_drive()
        self.assertEqual(self.moto.get_speed(), 75)

    # - Проверить, что в режиме парковки (сначала testDrive, потом park) машина останавливается (speed = 0).
    def test_car_parking_check(self):
        self.car.test_drive()
        self.car.park()
        self.assertEqual(self.car.get_speed(), 0)

    # - Проверить, что в режиме парковки (сначала testDrive, потом park) moto останавливается (speed = 0).
    def test_moto_parking_check(self):
        self.moto.test_drive()
        self.moto.park()
        self.assertEqual(self.moto.get_speed(), 0)


if __name__ == "__main__":
    unittest.main()
