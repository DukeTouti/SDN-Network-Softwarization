from mininet.net import Mininet
from mininet.node import OVSBridge
from mininet.cli import CLI
from mininet.log import setLogLevel, info

def build_network():
	net = Mininet(controller=none, switch=OVSBridge)
	
	core = net.addSwitch('c1')
	d1 = net.addSwitch('d1')
	d2 = net.addSwitch('d2')
	net.addLink(core, d1)
	net.addLink(core, d2)
	
	
	access = []
	for i, dist in enumerate ((d1, d1, d2, d2), start = 1):
		sw = net.addSwitch(f'a{i}')
		access.append(sw)
		net.addLink(dist, sw)
		
		
	host_id = 1
	for sw in access:
		for _ in range(2):
			h = net.addHost(f'h{host_id}')
			net.addLink(h, sw)
			host_id += 1
			
	
	info('*** Demarrage du reseau\n')
	net.start()
	net.pingAll()
	CLI(net)
	net.stop()
	
	
	if __name__ == '__main__':
		setLogLevel('info')
		build_network()
	
	
	
	
	
