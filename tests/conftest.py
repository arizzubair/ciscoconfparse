import platform
import sys
import os
THIS_DIR = os.path.dirname(__file__)
sys.path.insert(0, os.path.join(os.path.abspath(THIS_DIR), "../ciscoconfparse/"))
sys.path.insert(0, os.path.abspath(THIS_DIR))


import pytest
from ciscoconfparse import CiscoConfParse


c01 = """policy-map QOS_1
 class GOLD
  priority percent 10
 !
 class SILVER
  bandwidth 30
  random-detect
 !
 class BRONZE
  random-detect
!
interface Serial 1/0
 encapsulation ppp
 ip address 1.1.1.1 255.255.255.252
!
interface GigabitEthernet4/1
 switchport
 switchport access vlan 100
 switchport voice vlan 150
 power inline static max 7000
!
interface GigabitEthernet4/2
 switchport
 switchport access vlan 100
 switchport voice vlan 150
 power inline static max 7000
!
interface GigabitEthernet4/3
 switchport
 switchport access vlan 100
 switchport voice vlan 150
!
interface GigabitEthernet4/4
 shutdown
!
interface GigabitEthernet4/5
 switchport
 switchport access vlan 110
!
interface GigabitEthernet4/6
 switchport
 switchport access vlan 110
!
interface GigabitEthernet4/7
 switchport
 switchport access vlan 110
!
interface GigabitEthernet4/8
 switchport
 switchport access vlan 110
!
access-list 101 deny tcp any any eq 25 log
access-list 101 permit ip any any
!
!
logging 1.1.3.5
logging 1.1.3.17
!
banner login ^C
This is a router, and you cannot have it.
Log off now while you still can type. I break the fingers
of all tresspassers.
^C
alias exec showthang show ip route vrf THANG""".splitlines()

config_c01_default_gige = """policy-map QOS_1
 class GOLD
  priority percent 10
 !
 class SILVER
  bandwidth 30
  random-detect
 !
 class BRONZE
  random-detect
!
interface Serial 1/0
 encapsulation ppp
 ip address 1.1.1.1 255.255.255.252
!
default interface GigabitEthernet4/1
interface GigabitEthernet4/1
 switchport
 switchport access vlan 100
 switchport voice vlan 150
 power inline static max 7000
!
default interface GigabitEthernet4/2
interface GigabitEthernet4/2
 switchport
 switchport access vlan 100
 switchport voice vlan 150
 power inline static max 7000
!
default interface GigabitEthernet4/3
interface GigabitEthernet4/3
 switchport
 switchport access vlan 100
 switchport voice vlan 150
!
default interface GigabitEthernet4/4
interface GigabitEthernet4/4
 shutdown
!
default interface GigabitEthernet4/5
interface GigabitEthernet4/5
 switchport
 switchport access vlan 110
!
default interface GigabitEthernet4/6
interface GigabitEthernet4/6
 switchport
 switchport access vlan 110
!
default interface GigabitEthernet4/7
interface GigabitEthernet4/7
 switchport
 switchport access vlan 110
!
default interface GigabitEthernet4/8
interface GigabitEthernet4/8
 switchport
 switchport access vlan 110
!
access-list 101 deny tcp any any eq 25 log
access-list 101 permit ip any any
!
!
logging 1.1.3.5
logging 1.1.3.17
!
banner login ^C
This is a router, and you cannot have it.
Log off now while you still can type. I break the fingers
of all tresspassers.
^C
alias exec showthang show ip route vrf THANG""".splitlines()

config_c01_insert_serial_replace = """policy-map QOS_1
 class GOLD
  priority percent 10
 !
 class SILVER
  bandwidth 30
  random-detect
 !
 class BRONZE
  random-detect
!
default interface Serial 2/0
interface Serial 2/0
 encapsulation ppp
 ip address 1.1.1.1 255.255.255.252
!
interface GigabitEthernet4/1
 switchport
 switchport access vlan 100
 switchport voice vlan 150
 power inline static max 7000
!
interface GigabitEthernet4/2
 switchport
 switchport access vlan 100
 switchport voice vlan 150
 power inline static max 7000
!
interface GigabitEthernet4/3
 switchport
 switchport access vlan 100
 switchport voice vlan 150
!
interface GigabitEthernet4/4
 shutdown
!
interface GigabitEthernet4/5
 switchport
 switchport access vlan 110
!
interface GigabitEthernet4/6
 switchport
 switchport access vlan 110
!
interface GigabitEthernet4/7
 switchport
 switchport access vlan 110
!
interface GigabitEthernet4/8
 switchport
 switchport access vlan 110
!
access-list 101 deny tcp any any eq 25 log
access-list 101 permit ip any any
!
!
logging 1.1.3.5
logging 1.1.3.17
!
banner login ^C
This is a router, and you cannot have it.
Log off now while you still can type. I break the fingers
of all tresspassers.
^C
alias exec showthang show ip route vrf THANG""".splitlines()

# A smaller version of c01...
c02 = """policy-map QOS_1
 class GOLD
  priority percent 10
 !
 class SILVER
  bandwidth 30
  random-detect
 !
 class BRONZE
  random-detect
!
interface GigabitEthernet4/1
 switchport
 switchport access vlan 100
 switchport voice vlan 150
 power inline static max 7000
!""".splitlines()

c03 = """!
service timestamps debug datetime msec localtime show-timezone
service timestamps log datetime msec localtime show-timezone
!
errdisable recovery cause bpduguard
errdisable recovery interval 400
!
aaa new-model
!
ip vrf TEST_100_001
 route-target 100:1
 rd 100:1
!
interface Serial 1/0
 description Uplink to SBC F923X2K425
 bandwidth 1500
 clock rate 1500
 delay 70
 encapsulation ppp
 ip address 1.1.1.1 255.255.255.252
!
interface Serial 1/1
 description Uplink to AT&T
 encapsulation hdlc
 ip address 1.1.1.9 255.255.255.254
 hold-queue 1000 in
 hold-queue 1000 out
 mpls mtu 1540
 ip mtu 1500
 mpls ip
!
interface GigabitEthernet4/1
 description
 switchport
 switchport access vlan 100
 switchport voice vlan 150
 power inline static max 7000
!
interface GigabitEthernet4/2
 switchport
 switchport access vlan 100
 switchport voice vlan 150
 power inline static max 7000
 speed 100
 duplex full
!
interface GigabitEthernet4/3
 mtu 9216
 switchport
 switchport access vlan 100
 switchport voice vlan 150
!
interface GigabitEthernet4/4
 shutdown
!
interface GigabitEthernet4/5
 switchport
 switchport access vlan 110
 switchport port-security
 switchport port-security maximum 3
 switchport port-security mac-address sticky
 switchport port-security mac-address 1000.2000.3000
 switchport port-security mac-address 1000.2000.3001
 switchport port-security mac-address 1000.2000.3002
 switchport port-security violation shutdown
!
interface GigabitEthernet4/6
 description Simulate a Catalyst6500 access port
 switchport
 switchport access vlan 110
 switchport mode access
 switchport nonegotiate
 switchport port-security
 switchport port-security maximum 2
 switchport port-security violation restrict
 switchport port-security aging type inactivity
 switchport port-security aging time 5
 spanning-tree portfast
 spanning-tree portfast bpduguard
 storm-control action shutdown
 storm-control broadcast level 0.40
 storm-control multicast level 0.35
!
interface GigabitEthernet4/7
 description Dot1Q trunk allowing vlans 2-4,7,10,11-19,21-4094
 switchport
 switchport trunk encapsulation dot1q
 switchport mode trunk
 switchport trunk native vlan 4094
 switchport trunk allowed vlan remove 1,5-10,20
 switchport trunk allowed vlan add 7,10
 switchport nonegotiate
!
interface GigabitEthernet4/8.120
 no switchport
 encapsulation dot1q 120
 ip vrf forwarding TEST_100_001
 ip address 1.1.2.254 255.255.255.0
!
interface ATM5/0/0
 no ip address
 no ip redirects
 no ip unreachables
 no ip proxy-arp
 load-interval 30
 carrier-delay msec 100
 no atm ilmi-keepalive
 bundle-enable
 max-reserved-bandwidth 100
 hold-queue 500 in
!
interface ATM5/0/0.32 point-to-point
 ip address 1.1.1.5 255.255.255.252
 no ip redirects
 no ip unreachables
 no ip proxy-arp
 ip accounting access-violations
 pvc 0/32
  vbr-nrt 704 704
!
interface ATM5/0/1
 shutdown
!
router ospf 100 vrf TEST_100_001
 router-id 1.1.2.254
 network 1.1.2.0 0.0.0.255 area 0
!
policy-map QOS_1
 class GOLD
  priority percent 10
 !
 class SILVER
  bandwidth 30
  random-detect
 !
 class BRONZE
  random-detect
!
access-list 101 deny tcp any any eq 25 log
access-list 101 permit ip any any
!
!
logging 1.1.3.5
logging 1.1.3.17
!
banner login ^C
This is a router, and you cannot have it.
Log off now while you still can type. I break the fingers
of all tresspassers.
^C
!
alias exec showthang show ip route vrf THANG""".splitlines()


@pytest.yield_fixture(scope='session')
def c01_default_gigethernets(request):
    yield config_c01_default_gige

@pytest.yield_fixture(scope='session')
def c01_insert_serial_replace(request):
    yield config_c01_insert_serial_replace

@pytest.yield_fixture(scope='function')
def parse_c01(request):
    """Preparsed c01"""
    parse_c01 = CiscoConfParse(c01, factory=False)
     
    yield parse_c01

@pytest.yield_fixture(scope='function')
def parse_c01_factory(request):
    """Preparsed c01 with factory option"""
    parse_c01_factory = CiscoConfParse(c01, factory=True)
     
    yield parse_c01_factory

@pytest.yield_fixture(scope='function')
def parse_c02(request):
    """Preparsed c02"""
    parse_c02 = CiscoConfParse(c02, factory=False)
     
    yield parse_c02

@pytest.yield_fixture(scope='function')
def parse_c02_factory(request):
    """Preparsed c02"""
    parse_c02 = CiscoConfParse(c02, factory=True)
     
    yield parse_c02

@pytest.yield_fixture(scope='function')
def parse_c03(request):
    """Preparsed c03"""
    parse_c03 = CiscoConfParse(c01, factory=False)
     
    yield parse_c03

@pytest.yield_fixture(scope='function')
def parse_c03_factory(request):
    """Preparsed c01 with factory option"""
    parse_c03_factory = CiscoConfParse(c03, factory=True)
     
    yield parse_c03_factory

@pytest.mark.skipif(sys.version_info[0]>=3,
    reason="No Python3 MockSSH support")
@pytest.mark.skipif('windows' in platform.system().lower(),
    reason="No Windows MockSSH support")
@pytest.yield_fixture(scope='session')
def cisco_sshd_mocked(request):
    """Mock Cisco IOS SSH"""
    from fixtures.devices.mock_cisco import start_cisco_mock, stop_cisco_mock

    try:
        ## Start the SSH Server
        start_cisco_mock()
        yield True
    except:
        yield False
        stop_cisco_mock()
    stop_cisco_mock()
