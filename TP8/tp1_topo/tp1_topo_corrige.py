"""TP1 ONOS : 3 switches OpenFlow 1.3 et 4 hôtes.

Commande :
    sudo mn --custom ~/tp-onos-26/tp1_topo.py --topo tp1 \
      --controller remote,ip=127.0.0.1,port=6653 \
      --switch ovsk,protocols=OpenFlow13
"""
from mininet.topo import Topo


class TP1Topo(Topo):
    def build(self):
        # Version OpenFlow explicitement imposée sur chaque switch.
        s1 = self.addSwitch('s1', dpid='0000000000000001', protocols='OpenFlow13')
        s2 = self.addSwitch('s2', dpid='0000000000000002', protocols='OpenFlow13')
        s3 = self.addSwitch('s3', dpid='0000000000000003', protocols='OpenFlow13')

        h1 = self.addHost('h1', ip='10.0.0.1/24', mac='00:00:00:00:00:01')
        h2 = self.addHost('h2', ip='10.0.0.2/24', mac='00:00:00:00:00:02')
        h3 = self.addHost('h3', ip='10.0.0.3/24', mac='00:00:00:00:00:03')
        h4 = self.addHost('h4', ip='10.0.0.4/24', mac='00:00:00:00:00:04')

        # L'ordre des liens fixe les numéros de ports des switches.
        self.addLink(h1, s1)  # s1-eth1
        self.addLink(h2, s1)  # s1-eth2
        self.addLink(h3, s2)  # s2-eth1
        self.addLink(h4, s3)  # s3-eth1
        self.addLink(s1, s2)  # s1-eth3 <-> s2-eth2
        self.addLink(s2, s3)  # s2-eth3 <-> s3-eth2


topos = {'tp1': lambda: TP1Topo()}
