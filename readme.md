
# Singleton 및 TtlSingleton 메타클래스

이 프로젝트는 Python에서 싱글톤 클래스를 생성하기 위한 `Singleton` 및 `TtlSingleton` 메타클래스를 제공합니다. `TtlSingleton` 메타클래스는 `Singleton` 기능을 확장하여 지정된 시간이 지나면 인스턴스가 만료되는 TTL(Time-To-Live) 기능을 추가합니다.

## 기능

- **Singleton**: <b>클래스 이름과 초기화 매개변수가 동일한 경우</b> 하나의 인스턴스만 생성되도록 보장합니다.
- **TtlSingleton**: `Singleton`을 확장하여 TTL을 지원하며, <b>지정된 시간이 지나면 인스턴스가 만료</b>되고 새로 생성됩니다.
- 두 클래스 모두 `use_class_name_only` 매개변수를 true로 지정하면 초기화 매개변수와 관계없이 클래스 이름만으로 싱글톤을 생성할 수 있습니다. (전통적인 싱글톤과 동일)
## 설치

이 프로젝트를 사용하려면 저장소를 클론하고 필요한 종속성을 설치하십시오:

```sh
git clone https://github.com/jogakdal/advanced-singleton.git
cd <repository-directory>
pip install -r requirements.txt
```

## 사용법

### Singleton
- 싱글톤 클래스를 생성하려면 `Singleton` 메타 클래스로 지정해 주면 됩니다.
- `use_class_name_only` 매개변수를 true로 지정하면 초기화 매개변수와 관계없이 클래스 이름만으로 싱글톤을 생성합니다. (전통적인 싱글톤과 동일, defaault는 false)
```python
class SomeClass(metaclass=Singleton):
    def __init__(self, name):
        self.name = name
```

### TtlSingleton
- TTL 기반 싱글톤 클래스를 생성하려면 `TtlSingleton` 메타클래스를 사용하고 `ttl` 매개변수를 지정해 주세요.
- ttl 매개변수는 인스턴스가 만료되기까지의 시간(초)을 나타냅니다. default는 60초입니다.
- `use_class_name_only` 매개변수를 true로 지정하면 초기화 매개변수와 관계없이 클래스 이름만으로 싱글톤을 생성합니다. (전통적인 싱글톤과 동일, defaault는 false)
```python
class SomeClass(metaclass=TtlSingleton, ttl=60):
    def __init__(self, name):
        self.name = name
```

### 예제

다음은 `TtlSingleton` 사용법을 보여주는 예제입니다:

```python
import time

class TtlSingletonTest(metaclass=TtlSingleton, ttl=2):
    def __init__(self, name):
        self.name = name
        print(f'{self.name} is created')

# 인스턴스 생성
a = TtlSingletonTest('a')
b = TtlSingletonTest('b')

# TTL이 만료될 때까지 대기
time.sleep(2)

# TTL 만료 후 새 인스턴스 생성
c = TtlSingletonTest('a')
```

## 테스트
다음은 여러 케이스에 대한 테스트 코드입니다.
    
```python
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
```
테스트를 실행하려면 다음 명령어를 실행하십시오:

```sh
python -m unittest discover tests
```

## 라이선스
이 라이브러리는 누구나 사용할 수 있는 프리 소프트웨어입니다. 다만 코드를 수정할 경우 변경된 내용을 원작성자에게 통보해 주시면 감사하겠습니다.

## 작성자
황용호(jogakdal@gmail.com)
```
