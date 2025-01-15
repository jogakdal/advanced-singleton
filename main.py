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
