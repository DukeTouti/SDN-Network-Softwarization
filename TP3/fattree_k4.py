from mininet.net import Mininet
from mininet.node import OVSBridge
from mininet.cli import CLI
from mininet.log import setLogLevel, info
from time import sleep

class STPBridge(OVSBridge):
	def __init__(self, name, **kwargs):
		super().__init__(name, stp=True, **kwargs)

def build_fattree_k4():
	net = Mininet(controller=None, switch=STPBridge)

	# k = 4 : 4 core, 8 aggregation, 8 edge, 16 hosts
	core = [net.addSwitch(f'c{i}') for i in range(1, 5)]

	host_id = 1
	for pod in range(1, 5):
		aggs = [net.addSwitch(f'a{pod}{j}') for j in range(1, 3)]
		edges = [net.addSwitch(f'e{pod}{j}') for j in range(1, 3)]

		# Chaque edge est relie aux 2 aggregation du pod
		for edge in edges:
			for agg in aggs:
				net.addLink(edge, agg)

			# 2 hosts par edge
			for _ in range(2):
				host = net.addHost(f'h{host_id}')
				net.addLink(host, edge)
				host_id += 1

		# Agg 1 -> groupe de core 1 ; Agg 2 -> groupe de core 2
		net.addLink(aggs[0], core[0])
		net.addLink(aggs[0], core[1])
		net.addLink(aggs[1], core[2])
		net.addLink(aggs[1], core[3])

	info('*** Demarrage Fat-Tree k=4\n')
	net.start()
	info('*** STP : attendre la convergence avant pingall (~40 s)\n')
	sleep(40)
	net.pingAll()
	CLI(net)
	net.stop()

if __name__ == '__main__':
	setLogLevel('info')
	build_fattree_k4()
