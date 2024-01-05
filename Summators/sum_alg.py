import sys
import os
import argparse
import time
import subprocess
from pathlib import Path


#Parser
def createParser ():
  parser = argparse.ArgumentParser()
  parser.add_argument ('-n', '--nsize', nargs='?', type=int, default=2)
  parser.add_argument ('-m', '--msize', nargs='?', type=int, default=2)
  parser.add_argument ('-t', '--addtype', nargs='?', type=str, default='Simple', help='{Simple, LogHeight}')
  return parser




if __name__ == '__main__':
	start_time = time.time()
	parser = createParser()
	namespace = parser.parse_args (sys.argv[1:])
	n = namespace.nsize
	m = namespace.msize
	t = namespace.addtype
	outaagfile = './aags/Sum' + str(t) + str(n) + '+' + str(m) + '.aag'
	outaigfile = './aigs/Sum' + str(t) + str(n) + '+' + str(m) + '.aig'

	randinp = 1
	while True:
		outcnffile = './cnfs/Sum' + str(t) + str(n) + '+' + str(m) + '_randinp_' + str(randinp) + '.cnf'
		if Path(outcnffile).is_file():
			randinp += 1
		else:
			break

	with open('sum_.alg', 'w') as f:
		print('__in bit A['+str(n)+'];', file=f)
		print('__in bit B['+str(m)+'];', file=f)
		print('__out bit result[' + str(n+1) +'];', file=f)
		print('', file=f)
		print('void main()', file=f)
		print('{', file=f)
		print('    result = A + B;', file=f)
		print('}', file=f)

	taparams = ['../Apps/transalg']
	taparams.extend(['-i', 'sum_.alg'])
	taparams.extend(['-f', 'aig'])
	taparams.extend(['-a', t])
	taparams.extend(['-o', outaagfile])
	transalg = subprocess.run(taparams, capture_output=True, text=True)
	print(taparams)
	print(transalg.stdout)
	os.remove('sum_.alg')
	print('AAG was saved to', outaagfile)
	print('--------------------------------------------------')
	aigtoaigparams = ['../Apps/aigtoaig']
	aigtoaigparams.append(outaagfile)
	aigtoaigparams.append(outaigfile)
	aigtoaig = subprocess.run(aigtoaigparams, capture_output=True, text=True)
	print(aigtoaig.stdout)
	print('AIG was saved to', outaigfile)
	print('--------------------------------------------------')
	cnfparams = ['python3']
	cnfparams.append('../Scripts/circuit2cnf_with_outp.py')
	cnfparams.extend(['-n', outaagfile])
	cnfparams.extend(['-o', outcnffile])
	aagtocnf = subprocess.run(cnfparams, capture_output=True, text=True)
	print(aagtocnf.stdout)
	print('CNF with output corresponding to random input was saved to', outcnffile)



