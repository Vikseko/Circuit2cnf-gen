import sys
import os
import argparse
import time
import subprocess
from pathlib import Path


#Parser
def createParser ():
  parser = argparse.ArgumentParser()
  parser.add_argument ('-n', '--nof_numbers', nargs='?', type=int, default=2)
  parser.add_argument ('-s', '--number_size', nargs='?', type=int, default=2)
  parser.add_argument ('-t', '--sorttype', nargs='?', type=str, default='Bubble', help='{Bubble, Insert, Pancake, Selection}')
  return parser


def ta_bubble(n, s, f):
  print('define k '+str(n)+';', file=f)
  print('define n '+str(s)+';', file=f)
  print('__in bit data[k][n];', file=f)
  print('__out bit sorted_data[k][n];', file=f)
  print('void main()', file=f)
  print('{', file=f)
  print('  for(int i = 0; i < k - 1; i = i + 1)', file=f)
  print('  {', file=f)
  print('    for(int j = 0; j < k - i - 1; j = j + 1)', file=f)
  print('    {', file=f)
  print('      if(data[j] > data[j + 1])', file=f)
  print('      {', file=f)
  print('        bit t[n] = data[j];', file=f)
  print('        data[j] = data[j+1];', file=f)
  print('        data[j+1] = t;', file=f)
  print('      }', file=f)
  print('    }', file=f)
  print('  }', file=f)
  print('  sorted_data = data;', file=f)
  print('}', file=f)


def ta_insert(n, s, f):
  logsize = 0
  while True:
    if pow(2, logsize) >= n:
      break
    else:
      logsize += 1
  print('define nof_numbers '+str(n)+';', file=f)
  print('define log_size '+str(logsize)+';', file=f)
  print('define number_size '+str(s)+';', file=f)
  print('__in bit data[nof_numbers][number_size];', file=f)
  print('__out bit sorted_data[nof_numbers][number_size];', file=f)
  print('void main()', file=f)
  print('{', file=f)
  print('  for(int i = 1; i < nof_numbers; i = i + 1)', file=f)
  print('  {', file=f)
  print('    bit item[number_size] = data[i];', file=f)
  print('    bit cond = 1;', file=f)
  print('    bit index[log_size] = i;', file=f)
  print('    for(int j = i; j > 0; j = j - 1)', file=f)
  print('    {', file=f)
  print('      cond = cond & (data[j - 1] > item);', file=f)
  print('      if(cond)', file=f)
  print('      {', file=f)
  print('        data[j] = data[j - 1];', file=f)
  print('        index = j - 1;', file=f)
  print('      }', file=f)
  print('    }', file=f)
  print('    for(int k = 0; k < i; k = k + 1)', file=f)
  print('    {', file=f)
  print('      if(index == k)', file=f)
  print('      {', file=f)
  print('        data[k] = item;', file=f)
  print('      }', file=f)
  print('    }', file=f)
  print('  }', file=f)
  print('  sorted_data = data;', file=f)
  print('}', file=f)


def ta_pancake(n, s, f):
  logsize = 0
  while True:
    if pow(2, logsize) >= n:
      break
    else:
      logsize += 1
  print('define nof_numbers '+str(n)+';', file=f)
  print('define log_size '+str(logsize)+';', file=f)
  print('define number_size '+str(s)+';', file=f)
  print('__in bit data[nof_numbers][number_size];', file=f)
  print('__out bit sorted_data[nof_numbers][number_size];', file=f)
  print('void Flip(int p)', file=f)
  print('{', file=f)
  print('  for (int i = 0; i < p; i = i + 1)', file=f)
  print('  {', file=f)
  print('    p = p - 1;', file=f)
  print('    bit tmp[number_size] = data[i];', file=f)
  print('    data[i] = data[p];', file=f)
  print('    data[p] = tmp;', file=f)
  print('  }', file=f)
  print('}', file=f)
  print('void main()', file=f)
  print('{', file=f)
  print('    for(int i = nof_numbers - 1; i >= 0; i = i - 1)', file=f)
  print('  {', file=f)
  print('    bit max[log_size] = 0;', file=f)
  print('    for(int j = 1; j <= i; j = j + 1)', file=f)
  print('    {', file=f)
  print('      for(int d = 0; d <= i; d = d + 1)', file=f)
  print('      {', file=f)
  print('        if((max == d) & (data[d] < data[j]))', file=f)
  print('        {', file=f)
  print('          max = j;', file=f)
  print('        }', file=f)
  print('      }', file=f)
  print('    }', file=f)
  print('    for(int t = 1; t < i; t = t + 1)', file=f)
  print('    {', file=f)
  print('      if(max == t)', file=f)
  print('      {', file=f)
  print('        Flip(t + 1);', file=f)
  print('      }', file=f)
  print('    }', file=f)
  print('    if(max != i)', file=f)
  print('    {', file=f)
  print('      Flip(i + 1);', file=f)
  print('    }', file=f)
  print('  }', file=f)
  print('  sorted_data = data;', file=f)
  print('}', file=f)



def ta_selection(n, s, f):
  logsize = 0
  while True:
    if pow(2, logsize) >= n:
      break
    else:
      logsize += 1
  print('define nof_numbers '+str(n)+';', file=f)
  print('define log_size '+str(logsize)+';', file=f)
  print('define number_size '+str(s)+';', file=f)
  print('__in bit data[nof_numbers][number_size];', file=f)
  print('__out bit sorted_data[nof_numbers][number_size];', file=f)
  print('void main()', file=f)
  print('{', file=f)
  print('  for(int i = 0; i < nof_numbers - 1; i = i + 1)', file=f)
  print('  {', file=f)
  print('    bit min[log_size] = i;', file=f)
  print('    for(int j = i + 1; j < nof_numbers; j = j + 1)', file=f)
  print('    {', file=f)
  print('      for(int k = i; k < nof_numbers; k = k + 1)', file=f)
  print('      {', file=f)
  print('        if((min == k) & (data[j] < data[k]))', file=f)
  print('        {', file=f)
  print('          min = j;', file=f)
  print('        }', file=f)
  print('      }', file=f)
  print('    }', file=f)
  print('    for(int k = i; k < nof_numbers; k = k + 1)', file=f)
  print('    {', file=f)
  print('      if(min == k)', file=f)
  print('      {', file=f)
  print('        bit t[number_size] = data[i];', file=f)
  print('        data[i] = data[k];', file=f)
  print('        data[k] = t;', file=f)
  print('      }', file=f)
  print('    }', file=f)
  print('  }', file=f)
  print('  sorted_data = data;', file=f)
  print('}', file=f)


if __name__ == '__main__':
  start_time = time.time()
  parser = createParser()
  namespace = parser.parse_args (sys.argv[1:])
  n = namespace.nof_numbers
  s = namespace.number_size
  t = namespace.sorttype
  outaagfile = './aags/Sort' + str(t) + '_' + str(n) + '_' + str(s) + '.aag'
  outaigfile = './aigs/Sort' + str(t) + '_' + str(n) + '_' + str(s) + '.aig'

  randinp = 1
  while True:
    outcnffile = './cnfs/Sort' + str(t) + '_' + str(n) + '_' + str(s) + '_randinp_' + str(randinp) + '.cnf'
    if Path(outcnffile).is_file():
      randinp += 1
    else:
      break

  with open('sort_.alg', 'w') as f:
    if t == 'Bubble':
      ta_bubble(n, s, f)
    elif t == 'Insert':
      ta_insert(n, s, f)
    elif t == 'Pancake':
      ta_pancake(n, s, f)
    elif t == 'Selection':
      ta_selection(n, s, f)


  taparams = ['../Apps/transalg']
  taparams.extend(['-i', 'sort_.alg'])
  taparams.extend(['-f', 'aig'])
  taparams.extend(['-o', outaagfile])
  transalg = subprocess.run(taparams, capture_output=True, text=True)
  result = transalg.stdout.split('\n')
  errors = transalg.stderr
  print(taparams)
  print('TA result:\n', result)
  print('TA errors:\n', errors)
  os.remove('sort_.alg')
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
  print()

