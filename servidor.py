import socket
import threading
import sys
import pickle
import os

class Servidor():
	#pedimos el nuevo puerto
	print("Que puerto quieres utilizar?")
	def __init__(self, host=socket.gethostname(), port=input()):
		self.clientes = []
		self.sock = socket.socket()
		self.sock.bind((str(host), int(port)))
		self.sock.listen(20)
		self.sock.setblocking(False)

		print("Su IP actual es: " + socket.gethostbyname(host))
		aceptar = threading.Thread(target=self.aceptarC)
		procesar = threading.Thread(target=self.procesarC)
		
		print("DAEMON listo para aceptar conexiones")
		aceptar.daemon = True
		aceptar.start()

		print("DAEMON listo para procesar")
		procesar.daemon = True
		procesar.start()



		while True:
			msg = input('SALIR = Q\n')
			if msg == 'Q':
				print("**** TALOGOOO *****")
				self.sock.close()
				sys.exit()
			else:
				#numero de clientes conectados
				#print("El número de clientes conectados: "+ socket.)
				pass

	def broadcast(self, msg, cliente):
		for c in self.clientes:
			try:
				if c != cliente:
					c.send(msg)
			except:
				self.clientes.remove(c)

	def aceptarC(self):
		while True:
			try:
				conn, addr = self.sock.accept()
				print(f"\nConexion aceptada via {conn}\n")
				conn.setblocking(False)
				self.clientes.append(conn)
			except:
				pass

	def procesarC(self):
		print("Procesamiento de mensajes iniciado")
		while True:
			if len(self.clientes) > 0:
				for c in self.clientes:
					try:
						data = c.recv(32)
						if data:
							self.broadcast(data,c)
					except:
						pass

s = Servidor()