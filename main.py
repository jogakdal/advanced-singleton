import time

from advanced_python_singleton.singleton import Singleton
from advanced_python_singleton.ttlsingleton import TtlSingleton

if __name__ == '__main__':
    # Singleton 테스트
    class SingletonWithParamExample(metaclass=Singleton):
        def __init__(self, name):
            self.name = name
            print(f'{self.name}({self}) is created')


    class SingletonWithoutParamExample(metaclass=Singleton, use_class_name_only=True):
        def __init__(self, name):
            self.name = name
            print(f'{self.name}({self}) is created')


    a = SingletonWithParamExample('a')
    b = SingletonWithParamExample('b')
    c = SingletonWithParamExample('a')
    assert a != b
    assert a == c
    assert b == SingletonWithParamExample('b')

    a = SingletonWithoutParamExample('a')
    b = SingletonWithoutParamExample('b')
    assert a == b
    assert a == SingletonWithoutParamExample('c')

    # TtlSingleton 테스트
    class TtlSingletonExample(metaclass=TtlSingleton, ttl=2):
        def __init__(self, name):
            self.name = name
            print(f'    {self.name} is created')


    class SingletonTest():
        def test(self, p):
            return TtlSingletonExample(p)

    print('a creating')
    a = TtlSingletonExample('a')
    assert a.name == 'a'

    print('b creating')
    b = TtlSingletonExample('b')
    assert b.name == 'b'

    print('sleep 1 sec')
    time.sleep(1)

    print('a creating')
    c = TtlSingletonExample('a')
    assert a == c
    assert c.name == 'a'

    print('sleep 2 sec')
    time.sleep(2)

    print('a creating')
    d = TtlSingletonExample('a')
    assert a != d  # 시간이 2초 이상 지났음으로 새로운 객체 생성

    print('a creating via SingletonTest()')
    assert d == SingletonTest().test('a')

    print('sleep 2 sec')
    time.sleep(2)

    print('a creating via SingletonTest()')
    e = SingletonTest().test('a')
    assert d != e

    print('a creating')
    assert e == TtlSingletonExample('a')

    # TTL이 서로 다른 클래스 테스트
    class TtlSingletonExample_5(metaclass=TtlSingleton, ttl=5):
        def __init__(self, name):
            self.name = name

    class TtlSingletonExample_8(metaclass=TtlSingleton, ttl=8):
        def __init__(self, name):
            self.name = name

    a = TtlSingletonExample_5('a')
    b = TtlSingletonExample_8('a')
    assert a != b

    time.sleep(6)

    c = TtlSingletonExample_5('a')
    d = TtlSingletonExample_8('a')
    assert a != c
    assert b == d

    time.sleep(3)

    assert c == TtlSingletonExample_5('a')
    assert d != TtlSingletonExample_8('a')


    # use_class_name_only=True 테스트
    class SingletonClassNameOnly(metaclass=TtlSingleton, ttl=60, use_class_name_only=True):
        def __init__(self, name, value):
            self.name = name
            self.value = value

    instance1 = SingletonClassNameOnly('test', 123)
    instance2 = SingletonClassNameOnly('test', 456)

    assert instance1 == instance2
    assert instance1.value == 123
    assert instance2.value == 123

    # 인자 관련 테스트
    class SomeClass(metaclass=Singleton):
        def __init__(self, user_name, user_id=0):
            self.user_name = user_name
            self.user_id = user_id


    class AnotherClass(metaclass=Singleton):
        def __init__(self, user_name, user_id=0):
            self.user_name = user_name
            self.user_id = user_id

    assert SomeClass('abc', 1) == SomeClass('abc', 1)  # 클래스 명과 인자가 모두 같으면 같은 인스턴스가 되어야 한다.
    assert SomeClass('abc', 1) != AnotherClass('abc', 1)  # 클래스 명이 다르면 다른 인스턴스가 되어야 한다.
    assert SomeClass('abc', user_id=1) == SomeClass('abc', 1)  # 명시적 파라미터로 전달되어도 값이 같으면 같은 인스턴스가 되어야 한다.
    assert SomeClass('abc', 1) != SomeClass('abc', 2)  # 파라미터 값이 하나라도 다르면 다른 인스턴스가 되어야 한다.
    assert SomeClass('abc', user_id=1) != SomeClass('abc', 2)  # 파라미터 값이 하나라도 다르면 다른 인스턴스가 되어야 한다.
    assert SomeClass('abc') == SomeClass('abc', 0)  # 파라미터 디폴트 값과 동일한 값으로 전달되면 같은 인스턴스가 되어야 한다.
    assert SomeClass('abc') != SomeClass('abc', 1)  # 파라미터 디폴트 값과 다른 값으로 전달되면 다른 인스턴스가 되어야 한다.
    assert SomeClass('abc') == SomeClass('abc', user_id=0)  # 파라미터 디폴트 값과 동일한 값이 명시적으로 전달되어도 같은 인스턴스가 되어야 한다.
