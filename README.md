# python_design_pattern
python design pattern 

chapter01 : Python Design 패턴 시작!
- 상속, 추상화, Composition


chapter02 : Python Design 패턴 Singleton 시작!
- __init__
- __new__ 
- __call__
- metaclass

chapter03 : Python Design Factory! 
- abstract , inherit, create 

chapter04 : 퍼사드 패턴 (구조)
- 인터페이스 안에 객체 및 기능을 추가하여, 인터페이스만으로 기능을 사용

chapter05 : Proxy 패턴 (구조)
- 프록시와 퍼사드와 비교 필요(행위를 직접 요청 vs 서브시스템을 하나의 인터페이스로 구조화)
- The purpose of the Proxy is to add behavior while The purpose of the Facade is to simplify, which may actually involve removing behavior.
Proxy object represents a singly object while Facade object represents a subsystem of object.
The client object cannot access target object directly while client object does have ability to access subsystem object.
Proxy object provides access control to the single target object while Facade object provides simplified higher level interface to a subsystem of objects/components
-> https://www.mysoftkey.com/design-pattern/design-pattern-proxy-versus-facade/


chapter06 
#Observer Pattern pull or push method example
#subject와 observer 객체를 연결 
 -> subject 변경시에 연결되어 있는 observer 객체 method를 실행하여 데이터를 전달


chapter07
#Command Pattern 
#주식 트레이등 관련 매수 매도 주문시에 주문에 대한 순서를 queue에 담아서 메서드를 순차적으로 실행
#Receiver, ConcreateCommand , Agent 등 구조를 만들어서 수행하는 행위 패턴

chpater08
#Templete Pattern
#추상화 클래스에 공통으로 사용할 메서드를 정의
#추상화 클래스에 정의된 메서드 수행 내용을 작성
#템플릿 메서드를 수행하여 공통 서브 클래스 수행

chapter09
#컴파운드 패턴 두 가지 이상의 패턴을 활용하여 문제를 해결하는 패턴
#MVC 패턴으로 Front 와 Back 부분을 구분하여 구현, Front 수정시에 Back 부분 영향 없음

chapter10
#상태 디자인 패턴 (행위패턴) 
#TV를 켜고 끄는 상태를 서브 클래스로 구현하고, 서브클래스를 상속 받아서 실행