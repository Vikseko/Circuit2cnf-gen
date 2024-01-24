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
  parser.add_argument ('-t', '--multtype', nargs='?', type=str, default='Column', help='{Column, Dadda, Karatsuba, Wallace}')
  return parser




if __name__ == '__main__':
	start_time = time.time()
	parser = createParser()
	namespace = parser.parse_args (sys.argv[1:])
	n = namespace.nsize
	m = namespace.msize
	t = namespace.multtype
	outaagfile = './aags/Mult' + str(t) + str(n) + 'x' + str(m) + '.aag'
	outaigfile = './aigs/Mult' + str(t) + str(n) + 'x' + str(m) + '.aig'

	randinp = 1
	while True:
		outcnffile = './cnfs/Mult' + str(t) + str(n) + 'x' + str(m) + '_randinp_' + str(randinp) + '.cnf'
		if Path(outcnffile).is_file():
			randinp += 1
		else:
			break

	with open('mult_.alg', 'w') as f:
		print('__in bit A['+str(n)+'];', file=f)
		print('__in bit B['+str(m)+'];', file=f)
		print('__out bit result[' + str(n+m) +'];', file=f)
		print('', file=f)
		print('void main()', file=f)
		print('{', file=f)
		print('    result = A * B;', file=f)
		print('}', file=f)

	taparams = ['../Apps/transalg_for_mults_and_sums']
	taparams.extend(['-i', 'mult_.alg'])
	taparams.extend(['-f', 'aig'])
	taparams.extend(['-m', t])
	taparams.extend(['-o', outaagfile])
	transalg = subprocess.run(taparams, capture_output=True, text=True)
	print(taparams)
	print(transalg.stdout)
	os.remove('mult_.alg')
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



