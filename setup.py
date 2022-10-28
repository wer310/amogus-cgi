try:
	from setuptools import setup
except ImportError:
	os.system("pip3 install -U setuptools")
	from setuptools import setup
except ModuleNotFoundError:
	os.system("pip3 install -U setuptools")
	from setuptools import setup
import sys
import os
code_script = """
#! env/bin/python3
amogus = chr(3486)
import sys
if len(sys.argv) <  2:
	print(amogus)
	sys.exit(0)
elif "-h" in sys.argv or "--help" in sys.argv:
	print("amogus [count] [-h] [--help] [perfix]")
else:
	try:
		perfix = sys.argv[2]
	except IndexError:
		perfix = ""
	count = 1
	try:
		count = int(sys.argv[1])
	except ValueError:
		perfix = sys.argv[1]
	print(perfix, amogus*count)
"""
with open("amogus", "w") as f:
	f.write(code_script)
sys.argv.append("install")
setup(name="amogus-cgi", description="%s-cgi" % chr(3486), long_description="`amogus -h`", scripts=["amogus"])
print("\n"*34, "amogus-cgi installed! Using amogus-cgi:")
os.system("amogus -h")

