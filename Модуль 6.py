import json
 
class Model:
	a = 1
	b = 2
	def save(self):
		dct = {k: str(v) for k, v in vars(Model).items()}
		with open('file.txt', 'w', encoding='utf-8') as fout:
			json.dump(dct, fout)

obj = Model()
obj.save()
 

[guest@localhost py]$ cat file.txt 
{"__module__": "__main__", "a": "1", "b": "2", "save": "<function Model.save at 0x7f9650a8f400>", "__dict__": "<attribute '__dict__' of 'Model' objects>", "__weakref__": "<attribute '__weakref__' of 'Model' objects>", "__doc__": "None"}[guest@localhost py]$ 
[guest@localhost py]$

