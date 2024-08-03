from fcntl import ioctl
from socket import AF_INET, SOCK_DGRAM, inet_ntoa, socket
from struct import pack
from sys import maxsize, modules
from sys import version_info

PY3 = version_info[0] == 3

MODULE_NAME = __name__.split(".")[-1]

def _ifinfo(sock, addr, ifname):
	if PY3:
		iface = pack('256s', bytes(ifname[:15], 'utf-8'))
	else:
		iface = pack('256s', ifname[:15])
	info = ioctl(sock.fileno(), addr, iface)
	if addr == 0x8927:
		if PY3:
			return ''.join(['%02x:' % ord(chr(char)) for char in info[18:24]])[:-1].upper()
		else:
			return ''.join(['%02x:' % ord(char) for char in info[18:24]])[:-1].upper()
	else:
		return inet_ntoa(info[20:24])


def getIfConfig(ifname):
	ifreq = {"ifname": ifname}
	infos = {}
	sock = socket(AF_INET, SOCK_DGRAM)
	# Offsets defined in /usr/include/linux/sockios.h on linux 2.6.
	infos["addr"] = 0x8915  # SIOCGIFADDR
	infos["brdaddr"] = 0x8919  # SIOCGIFBRDADDR
	infos["hwaddr"] = 0x8927  # SIOCSIFHWADDR
	infos["netmask"] = 0x891b  # SIOCGIFNETMASK
	try:
		for k, v in infos.items():
			ifreq[k] = _ifinfo(sock, v, ifname)
	except Exception as ex:
		print("[About] getIfConfig Ex: %s" % str(ex))
		pass
	sock.close()
	return ifreq

# For modules that do "from About import about"
about = modules[__name__]
