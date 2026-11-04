from mininet.topo import Topo

class MicrosegTopo(Topo):
	def build(self):
		s1 = self.addSwitch('s1')
		s2 = self.addSwitch('s2')
		s3 = self.addSwitch('s3')
		h1 = self.addHost('h1')
		h2 = self.addHost('h2')
		h3 = self.addHost('h3')
		h4 = self.addHost('h4')
		
		self.addLink(h1, s1) # s1-eth1
		self.addLink(h2, s1) # s1-eth2
		self.addLink(s1, s2) # s1-eth3 / s2-eth1
		self.addLink(s2, s3) # s2-eth2 / s3-eth1
		self.addLink(h3, s3) # s3-eth2
		self.addLink(h4, s3) # s3-eth3
		
topos = {'microseg' : lambda : MicrosegTopo()}
