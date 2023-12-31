**Программа**
______________
Включает в себя два класса:

    -AverageGenerator
        Создает рандомный список, принимая три параметра - размер списка, нижний и верхний
        диапазоны элементов и рассчитывает среднее арифметическое. Также включает в себя 
        методы проверки генерируемого списка на количество элементов списка и соответсвие
        типов. Содержит метод, который проводит комплексную проверку. При обращении к 
        экземпляру возвращает строковое значение, которое содержит список и среднее 
        арифметическое списка.

    -AverageComparator
        Содержит статический метод, который производит сравнение средних арифметических,
        которые передаются в качестве аргументов. Возвращает результат сравнения в виде
        строки 'First average is gross than second', 'First average is less than second'
        и 'Averages are equal'.
        
**Тесты**
______________
Покрытие сценариев:

>юнит-тесты:
  >- Соответствие типу list.
  >- Тест на пустой список.
  >- Тест на количество элементов (менее двух).
  >- Параметризованный тест на сравнение с предустановленными параметрами.

>интеграционный тест:
  >- Комплексный тест на создание экземпляра и всех методов проверки класса.

>сквозной тест:
  >- Создание двух списков и сравнение их средних арифметических.

______________

Таким образом было обеспечено максимальное покрытие строк кода программы.
