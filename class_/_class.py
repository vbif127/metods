metod_class = [
    """
     	      Условные обозначения наименований 	Пример
    Локальная переменная 	camelCase с необязательным подчеркиванием 	studentName

    Константа 	Прописные буквы, слова, разделенные подчеркиванием 	STUDENT_NAME

    Глобальная переменная 	Префикс с camelCase с дополнительными символами подчеркивания 	my_studentName

    Функция 	PascalCase с необязательными символами подчеркивания; действительный залог 	MystudentName

    Модуль 	Приставка с camelCase 	
    _studentname

    Класс 	Префиксный класс с Pascalcase; держать это в порядке 	class_MyStudentName

    Объект 	Префикс ob_with camelcase 	ob_studentName

    Источник: https://pythonpip.ru/osnovy/staticheskie-peremennye-i-metody-v-python
    """,

    """
    
    __pos__(self)
    Определяет поведение для унарного плюса (+some_object)

    __neg__(self)
    Определяет поведение для отрицания(-some_object)

    __abs__(self)
    Определяет поведение для встроенной функции abs().

    __invert__(self)
    Определяет поведение для инвертирования оператором ~. Для объяснения что он делает смотри статью в Википедии о бинарных операторах.

    __round__(self, n)
    Определяет поведение для встроенной функции round(). n это число знаков после запятой, до которого округлить.

    __floor__(self)
    Определяет поведение для math.floor(), то есть, округления до ближайшего меньшего целого.

    __ceil__(self)
    Определяет поведение для math.ceil(), то есть, округления до ближайшего большего целого.

    __trunc__(self)
    Определяет поведение для math.trunc(), то есть, обрезания до целого.


Обычные арифметические операторы

Теперь рассмотрим обычные бинарные операторы (и ещё пару функций): +, -, * и похожие. Они, по большей части, отлично сами себя описывают.

    __add__(self, other)
    Сложение.

    __sub__(self, other)
    Вычитание.

    __mul__(self, other)
    Умножение.

    __floordiv__(self, other)
    Целочисленное деление, оператор //.

    __div__(self, other)
    Деление, оператор /.

    __truediv__(self, other)
    Правильное деление. Заметьте, что это работает только когда используется from __future__ import division.

    __mod__(self, other)
    Остаток от деления, оператор %.

    __divmod__(self, other)
    Определяет поведение для встроенной функции divmod().

    __pow__
    Возведение в степень, оператор **.

    __lshift__(self, other)
    Двоичный сдвиг влево, оператор <<.

    __rshift__(self, other)
    Двоичный сдвиг вправо, оператор >>.

    __and__(self, other)
    Двоичное И, оператор &.

    __or__(self, other)
    Двоичное ИЛИ, оператор |.

    __xor__(self, other)
    Двоичный xor, оператор ^.

    Магия контейнеров

Без дальнейшего промедления, вот магические методы, используемые контейнерами:

    __len__(self)
    Возвращает количество элементов в контейнере. Часть протоколов для изменяемого и неизменяемого контейнеров.

    __getitem__(self, key)
    Определяет поведение при доступе к элементу, используя синтаксис self[key]. Тоже относится и к протоколу изменяемых и к протоколу неизменяемых контейнеров. Должен выбрасывать соответствующие исключения: TypeError если неправильный тип ключа и KeyError если ключу не соответствует никакого значения.

    __setitem__(self, key, value)
    Определяет поведение при присваивании значения элементу, используя синтаксис self[nkey] = value. Часть протокола изменяемого контейнера. Опять же, вы должны выбрасывать KeyError и TypeError в соответсвующих случаях.

    __delitem__(self, key)
    Определяет поведение при удалении элемента (то есть del self[key]). Это часть только протокола для изменяемого контейнера. Вы должны выбрасывать соответствующее исключение, если ключ некорректен.

    __iter__(self)
    Должен вернуть итератор для контейнера. Итераторы возвращаются в множестве ситуаций, главным образом для встроенной функции iter() и в случае перебора элементов контейнера выражением for x in container:. Итераторы сами по себе объекты и они тоже должны определять метод __iter__, который возвращает self.

    __reversed__(self)
    Вызывается чтобы определить поведения для встроенной функции reversed(). Должен вернуть обратную версию последовательности. Реализуйте метод только если класс упорядоченный, как список или кортеж.

    __contains__(self, item)
    __contains__ предназначен для проверки принадлежности элемента с помощью in и not in. Вы спросите, почему же это не часть протокола последовательности? Потому что когда __contains__ не определён, Питон просто перебирает всю последовательность элемент за элементом и возвращает True если находит нужный.

    __missing__(self, key)
    __missing__ используется при наследовании от dict. Определяет поведение для для каждого случая, когда пытаются получить элемент по несуществующему ключу (так, например, если у меня есть словарь d и я пишу d["george"] когда "george" не является ключом в словаре, вызывается d.__missing__("george")).

    Отражение

Вы можете контролировать и отражение, использующее встроенные функции isinstance() и issubclass(), определив некоторые магические методы. Вот они:

    __instancecheck__(self, instance)
    Проверяет, является ли экземлпяр членом вашего класса (isinstance(instance, class), например.

    __subclasscheck__(self, subclass)
    Проверяет, является наследуется ли класс от вашего класса (issubclass(subclass, class)).

Вызываемые объекты

Как вы наверное уже знаете, в Питоне функции являются объектами первого класса. Это означает, что они могут быть переданы в функции или методы так же, как любые другие объекты. Это невероятно мощная особенность.

Специальный магический метод позволяет экземплярам вашего класса вести себя так, как будто они функции, тоесть вы сможете «вызывать» их, передавать их в функции, которые принимают функции в качестве аргументов и так далее. Это другая удобная особенность, которая делает программирование на Питоне таким приятным.

    __call__(self, [args...])
    Позволяет любому экземпляру вашего класса быть вызванным как-будто он функция. Главным образом это означает, что x() означает то же, что и x.__call__(). Заметьте, __call__ принимает произвольное число аргументов; то есть, вы можете определить __call__ так же как любую другую функцию, принимающую столько аргументов, сколько вам нужно.

    __enter__(self)
    Определяет, что должен сделать менеджер контекста в начале блока, созданного оператором with. Заметьте, что возвращаемое __enter__ значение и есть то значение, с которым производится работа внутри with.

    __exit__(self, exception_type, exception_value, traceback)
    Определяет действия менеджера контекста после того, как блок будет выполнен (или прерван во время работы). Может использоваться для контроллирования исключений, чистки, любых действий которые должны быть выполнены незамедлительно после блока внутри with. Если блок выполнен успешно, exception_type, exception_value, и traceback будут установлены в None. В другом случае вы сами выбираете, перехватывать ли исключение или предоставить это пользователю; если вы решили перехватить исключение, убедитесь, что __exit__ возвращает True после того как всё сказано и сделано. Если вы не хотите, чтобы исключение было перехвачено менеджером контекста, просто позвольте ему случиться.


    Построение дескрипторов

Дескрипторы это такие классы, с помощью которых можно добавить свою логику к событиям доступа (получение, изменение, удаление) к атрибутам других объектов. Дескрипторы не подразумевается использовать сами по себе; скорее, предполагается, что ими будут владеть какие-нибудь связанные с ними классы. Дескрипторы могут быть полезны для построения объектно-ориентированных баз данных или классов, чьи атрибуты зависят друг от друга. В частности, дескрипторы полезны при представлении атрибутов в нескольких системах исчисления или каких-либо вычисляемых атрибутов (как расстояние от начальной точки до представленной атрибутом точки на сетке).

Чтобы класс стал дескриптором, он должен реализовать по крайней мере один метод из __get__, __set__ или __delete__. Давайте рассмотрим эти магические методы:

    __get__(self, instance, instance_class)
    Определяет поведение при возвращении значения из дескриптора. instance это объект, для чьего атрибута-дескриптора вызывается метод. owner это тип (класс) объекта.

    __set__(self, instance, value)
    Определяет поведение при изменении значения из дескриптора. instance это объект, для чьего атрибута-дескриптора вызывается метод. value это значение для установки в дескриптор.

    __delete__(self, instance)
    Определяет поведение для удаления значения из дескриптора. instance это объект, владеющий дескриптором.

    Копирование

В Питоне оператор присваивания не копирует объекты, а только добавляет ещё одну ссылку. Но для коллекций, содержащих изменяемые элементы, иногда необходимо полноценное копирование, чтобы можно было менять элементы одной последовательности, не затрагивая другую. Здесь в игру и вступает copy. К счастью, модули в Питоне не обладают разумом, поэтому мы можем не беспокоиться что они вдруг начнут бесконтрольно копировать сами себя и вскоре линуксовые роботы заполонят всю планету, но мы должны сказать Питону как правильно копировать.

    __copy__(self)
    Определяет поведение copy.copy() для экземпляра вашего класса. copy.copy() возвращает поверхностную копию вашего объекта — это означает, что хоть сам объект и создан заново, все его данные ссылаются на данные оригинального объекта. И при изменении данных нового объекта, изменения будут происходить и в оригинальном.

    __deepcopy__(self, memodict={})
    Определяет поведение copy.deepcopy() для экземпляров вашего класса. copy.deepcopy() возвращает глубокую копию вашего объекта — копируются и объект и его данные. memodict это кэш предыдущих скопированных объектов, он предназначен для оптимизации копирования и предотвращения бесконечной рекурсии, когда копируются рекурсивные структуры данных. Когда вы хотите полностью скопировать какой-нибудь конкретный атрибут, вызовите на нём copy.deepcopy() с первым параметром memodict.


Когда использовать эти магические методы? Как обычно — в любом случае, когда вам необходимо больше, чем стандартное поведение. Например, если вы пытаетесь скопировать объект, который содержит кэш как словарь (возможно, очень большой словарь), то может быть вам и не нужно копировать весь кэш, а обойтись всего одним в общей памяти объектов.


    Сериализация собственных объектов.

    Модуль pickle не только для встроенных типов. Он может использоваться с каждым классом, реализующим его протокол. Этот протокол содержит четыре необязательных метода, позволяющих настроить то, как pickle будет с ними обращаться (есть некоторые различия для расширений на C, но это за рамками нашего руководства):

    __getinitargs__(self)
    Если вы хотите, чтобы после десериализации вашего класса был вызыван __init__, вы можете определить __getinitargs__, который должен вернуть кортеж аргументов, который будет отправлен в __init__. Заметьте, что этот метод работает только с классами старого стиля.

    __getnewargs__(self)
    Для классов нового стиля вы можете определить, какие параметры будут переданы в __new__ во время десериализации. Этот метод так же должен вернуть кортеж аргументов, которые будут отправлены в __new__.

    __getstate__(self)
    Вместо стандартного атрибута __dict__, где хранятся атрибуты класса, вы можете вернуть произвольные данные для сериализации. Эти данные будут переданы в __setstate__ во время десериализации.

    __setstate__(self, state)
    Если во время десериализации определён __setstate__, то данные объекта будут переданы сюда, вместо того чтобы просто записать всё в __dict__. Это парный метод для __getstate__: когда оба определены, вы можете представлять состояние вашего объекта так, как вы только захотите.

    __reduce__(self)
    Если вы определили свой тип (с помощью Python's C API), вы должны сообщить Питону как его сериализовать, если вы хотите, чтобы он его сериализовал. __reduce__() вызывается когда сериализуется объект, в котором этот метод был определён. Он должен вернуть или строку, содержащую имя глобальной переменной, содержимое которой сериализуется как обычно, или кортеж. Кортеж может содержать от 2 до 5 элементов: вызываемый объект, который будет вызван, чтобы создать десериализованный объект, кортеж аргументов для этого вызываемого объекта, данные, которые будут переданы в __setstate__ (опционально), итератор списка элементов для сериализации (опционально) и итератор словаря элементов для сериализации (опционально).

    __reduce_ex__(self, protocol)
    Иногда полезно знать версию протокола, реализуя __reduce__. И этого можно добиться, реализовав вместо него __reduce_ex__. Если __reduce_ex__ реализован, то предпочтение при вызове отдаётся ему (вы всё-равно должны реализовать __reduce__ для обратной совместимости).

    
Дополнение 1: Как вызывать магические методы

Некоторые из магических методов напрямую связаны со встроенными функциями; в этом случае совершенно очевидно как их вызывать. Однако, так бывает не всегда. Это дополнение посвящено тому, чтобы раскрыть неочевидный синтаксис, приводящий к вызову магических методов.
Магический метод 	Когда он вызывается (пример) 	Объяснение

__new__(cls [,...]) 	instance = MyClass(arg1, arg2) 	__new__ вызывается при создании экземпляра

__init__(self [,...]) 	instance = MyClass(arg1, arg2) 	__init__ вызывается при создании экземпляра

__cmp__(self, other) 	self == other, self > other, etc. 	Вызывается для любого сравнения

__pos__(self) 	+self 	Унарный знак плюса

__neg__(self) 	-self 	Унарный знак минуса

__invert__(self) 	~self 	Побитовая инверсия

__index__(self) 	x[self] 	Преобразование, когда объект используется как индекс

__nonzero__(self) 	bool(self), if self: 	Булевое значение объекта

__getattr__(self, name) 	self.name # name не определено 	Пытаются получить несуществующий атрибут

__setattr__(self, name, val) 	self.name = val 	Присвоение любому атрибуту

__delattr__(self, name) 	del self.name 	Удаление атрибута

__getattribute__(self, name) 	self.name 	Получить любой атрибут

__getitem__(self, key) 	self[key] 	Получение элемента через индекс

__setitem__(self, key, val) 	self[key] = val 	Присвоение элементу через индекс

__delitem__(self, key) 	del self[key] 	Удаление элемента через индекс

__iter__(self) 	for x in self 	Итерация

__contains__(self, value) 	value in self, value not in self 	Проверка принадлежности с помощью in

__call__(self [,...]) 	self(args) 	«Вызов» экземпляра

__enter__(self) 	with self as x: 	with оператор менеджеров контекста

__exit__(self, exc, val, trace) 	with self as x: 	with оператор менеджеров контекста

__getstate__(self) 	pickle.dump(pkl_file, self) 	Сериализация

__setstate__(self) 	data = pickle.load(pkl_file) 	Сериализация



    Дополнение 2: Изменения в Питоне 3

Опишем несколько главных случаев, когда Питон 3 отличается от 2.x в терминах его объектной модели:

    Так как в Питоне 3 различий между строкой и юникодом больше нет, __unicode__ исчез, а появился __bytes__ (который ведёт себя так же как __str__ и __unicode__ в 2.7) для новых встроенных функций построения байтовых массивов.
    Так как деление в Питоне 3 теперь по-умолчанию «правильное деление», __div__ больше нет.
    __coerce__ больше нет, из-за избыточности и странного поведения.
    __cmp__ больше нет, из-за избыточности.
    __nonzero__ было переименовано в __bool__.
    next у итераторов был переименован в __next__.



    """

]

# print(metod_class[1])
