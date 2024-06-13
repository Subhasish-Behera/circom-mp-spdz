# -*- coding: utf-8 -*-
"""naive_search.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1vU3qtkYyHlHF_1UFmtfZir76Aq_3HcSs
"""

inlisttxt = "0.inlist";
intxt = "0.in";
outtxt = "0.out";

M = 3; # 3 parties for list + 1 party for item
N = 5;

list = [];
inlistdictlist = [];
for i in range(M):
    inlistdict = {};
    list.append({ "name": f"p{i}", "inputs": [], "outputs": [outtxt] });
    for j in range(N):
        inlistops = inlisttxt + "["+ str(i) + "]" + "["+ str(j) + "]";
        list[i]['inputs'].append(inlistops);
        inlistdict[inlistops] = j;
    inlistdictlist.append(inlistdict);

list.append({ "name": "bob", "inputs": [intxt], "outputs": [outtxt] });
inlistdictlist.append({intxt: 10});

print(list);
for inlistdict in inlistdictlist:
    print(inlistdict)
# print(in1dict);
# print(in2dict);

import json
with open('mpc_settings.json', 'w') as fp:
    json.dump(list, fp)

for i in range(M+1):
    with open(f"inputs_party_{i}.json", 'w') as fp:
        json.dump(inlistdictlist[i], fp)

### FIX BELOW
raw = """
def naive_search(n):
	# hardcoded "secret" list from Alice - in a real application this should be a private input
	a = [sint(i) for i in range(n)]
	print_ln("Waiting for search input from Bob")
	b = sint.get_input_from(1)

	eq_bits = [x == b for x in a]
	b_in_a = sum(eq_bits)
	print_ln("Is b in Alice's list? %s", b_in_a.reveal())

naive_search(1000)
""";

with open('raw_circuit.mpc', 'w') as fp:
    fp.write(raw);