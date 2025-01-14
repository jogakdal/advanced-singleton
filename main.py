import time

from src.singleton.singleton import TtlSingleton, Singleton

if __name__ == '__main__':
    class TtlSingletonTest(metaclass=TtlSingleton, ttl=2):
        def __init__(self, name):
            self.name = name
            print(f'    {self.name} is created')


    class SingletonTest():
        def test(self, p):
            return TtlSingletonTest(p)

    print('a creating')
    a = TtlSingletonTest('a')
    assert a.name == 'a'

    print('b creating')
    b = TtlSingletonTest('b')
    assert b.name == 'b'

    print('sleep 1 sec')
    time.sleep(1)

    print('a creating')
    c = TtlSingletonTest('a')
    assert a == c
    assert c.name == 'a'

    print('sleep 2 sec')
    time.sleep(2)

    print('a creating')
    d = TtlSingletonTest('a')
    assert a != d  # 시간이 2초 이상 지났음으로 새로운 객체 생성

    print('a creating via SingletonTest()')
    assert d == SingletonTest().test('a')

    print('sleep 2 sec')
    time.sleep(2)

    print('a creating via SingletonTest()')
    e = SingletonTest().test('a')
    assert d != e

    print('a creating')
    assert e == TtlSingletonTest('a')

    # use_class_name_only=True 테스트
    # class SingletonClassNameOnly(metaclass=Singleton, use_class_name_only=True):
    class SingletonClassNameOnly(metaclass=TtlSingleton, ttl=60, use_class_name_only=True):
        def __init__(self, name, value):
            self.name = name
            self.value = value

    instance1 = SingletonClassNameOnly('test', 123)
    instance2 = SingletonClassNameOnly('test', 456)

    assert instance1 == instance2
    assert instance1.value == 123
    assert instance2.value == 123
