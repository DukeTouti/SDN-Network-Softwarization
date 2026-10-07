from mininet.net import Mininet
from mininet.node import OVSBridge
from mininet.cli import CLI
from mininet.log import setLogLevel, info
from time import sleep

class STPBridge(OVSBridge):
	def __init__(self, name, **kwargs):
		super().__init__(name, stp=True, **kwargs)

def build_network():
	net = Mininet(controller=None, switch=STPBridge)

	info('*** Creation des spines\n')
	sp1 = net.addSwitch('sp1')
	sp2 = net.addSwitch('sp2')

	info('*** Creation des leaves et des hosts\n')
	leaves = []
	for i in range(1, 5):
		leaf = net.addSwitch(f'l{i}')
		leaves.append(leaf)
		h1 = net.addHost(f'h{2*i-1}')
		h2 = net.addHost(f'h{2*i}')
		net.addLink(h1, leaf)
		net.addLink(h2, leaf)
		net.addLink(leaf, sp1)
		net.addLink(leaf, sp2)

	info('*** Demarrage du reseau\n')
	net.start()
	info('*** STP : attendre la convergence avant pingall (~35 s)\n')
	sleep(35)
	net.pingAll()
	CLI(net)
	net.stop()

if __name__ == '__main__':
	setLogLevel('info')
	build_network()
