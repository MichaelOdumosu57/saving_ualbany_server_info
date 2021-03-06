from socket import * #importing the socket module
from struct import* #importing the sturct module
from time import * #importing the time module
class TCP_Client_Header: #using class object to make TCP datagram header
	
    class packet_field:# linked list implementation, easier to transfer list values into class object
	
	def __init__(self):
		self.packet_field = 'b'
		self.packet_value = 'empty'
		self.next = None
       	
    def  __init__(self): # fill in boxes in the header rfr pg 60 transport layer
	self.headptr = None
	self.tailptr = None
	self.download = False

        """i_port_num =source port #
            e_port_num = dest port # which is 9998
            seq_num= sequence #
            ack_num = acknowlegdement #
            head_len = head length
            urg_data = urgent data (gen .not used)
            ack_vld = is ack # valid?
            push_data = push data now
            R_S_F = Connection estab (setup commands)RST,SYN,FIN
            recv_wdw = receive window
            checksum = internet checksum
            urg_ptr = urgent data pointer
            app_data = application data"""
   	        
 

    def __str__(self): # creates a readable text for the object

	runner = self.headptr
	retval = ""
	if self.headptr == None:
		return "nothing here, somethings up"
	
	while runner != self.tailptr:
		retval += runner.packet_field + "," + runner.packet_value + ","
		runner = runner.next
	retval += runner.packet_field + "," + runner.packet_value
	return retval

    def __len__(self):
	length = 0
	runner = self.headptr
	while runner != self.tailptr.next:
		runner = runner.next
		length += 1
	return length
    
    def insert(self,datagram):
	#self.headptr = None would use this but I am too far in the program
	x = 0
	y = 0
	cello = 'please work' #test value to see if argument is a file or string
	 
	if datagram.find('.txt') != -1 :
		datagram = datagram.strip(".txt")
		f = open(datagram,'r')
		fields = f.read()
		fields = fields.split(',')
	
		while x < len(fields):
			self.insert_packet(fields[x],fields[x+1])
			x+= 2
		self.download == True
		x = 0
	
	else:
		datagram = datagram.split(',')
		while y < len(datagram):
			self.insert_packet(datagram[y],datagram[y+1])
			y += 2
		y = 0

    def insert_packet(self,field,value):
		new_field =self.packet_field()
		new_field.packet_field = field
		new_field.packet_value = value	
		if self.headptr == None:
			self.headptr = new_field
        		self.tailptr = new_field
 		else:
			self.tailptr.next = new_field
			self.tailptr = new_field
    
    def check(self,header_field,header_value): #checks if everything matches up
	check = self.__str__()
	check = check.split(',')
	for i in range(len(check)):
		if check[i]== header_field:
			if check[i+1]== header_value:
				return True
	return False
    def replace(self,header_field,header_value): #Should only replace values in header fields 
	z = 0
	replace  =self. __str__()
	replace = replace.split(',')
	for i in range(len(replace)):
		if replace[i] == header_field:
			replace[i+1] = header_value
			self.headptr = None
			break
	while z < len(replace):
		self.insert_packet(str(replace[z]),str(replace[z+1]))
		z +=2
	z = 0

    def steal_a_part(self,header_field):
	x = 0
	part = self.__str__()
	part = part.split(",")
	for i in range(len(part)):
		if part[i] == header_field:
			value = part[i+1]
			field = part[i] 
			del part[i+1]
			del part[i]
			break
	while x <len(part):
		self.insert_packet(str(part[x]),str(part[x+1]))	
		x += 2
	x = 0
	return field,value
  	
if __name__ == "__main__":	
	Host = TCP_Client_Header() # to set up and open teardown commands
	serverName = "127.0.0.1" #name of server


	clientSocket = socket(AF_INET,SOCK_DGRAM) # type of connection set up
	Host.insert('init_packet_fields.txt')#now the packet is set up

	#the listen part where server listens for client

	Host.replace("SYNbit",1)
	Host.replace("seq_num",200)
	impt_field,impt_value = Host.steal_a_part("app_data")

	clientSocket.sendto(str(Host).encode(),(serverName,9998))
	Host.headptr = None
	print("Asking to make a connection with the server")
	#the answer part where server says its okay to recv

       	message,serveraddr = clientSocket.recvfrom(2048)
	message = message.decode()
	message = str(message)
	Host.headptr = None
	Host.insert(message)
	get_i_answer = Host.check("seq_num","201")
	get_ii_answer = Host.check("ACKbit","1")
	get_iii_answer = Host.check("ack_num","201")
	print(get_i_answer,get_ii_answer, get_iii_answer)
	if get_i_answer & get_ii_answer & get_iii_answer:
		print("The server has answered the client")
		Host.replace("ack_num",202)
		clientSocket.sendto(str(Host).encode(),(serverName,9998))
		Host.headptr = None
	else:
		print("Didnt get it")

	x = 1
	y = 0
	Client = TCP_Client_Header() # to send packets back and forth
	Client.insert_packet(impt_field,impt_value)
	while x != 32:
		x += 1	
		clientSocket.sendto(str(Host).encode(),(serverName,9998))
		message,serveraddr = clientSocket.recvfrom(2048)
		message = message.decode()
		message = str(message)
		print("This is everything you need to know about the message coming in")
		print(message,len(message),type(message))
		Host.headptr = None #allows for change of new data coming in
		Host.insert(message)
	print(x)
	
	while Host.download == False:
		
		if Host.check("FINbit","1") & Host.check("seq_num","204"):
			Host.replace("ack_num",204)
			clientSocket.sendto(str(Host).encode(),(serverName,9998))
			print("The server is starting to close its socket")
			clientSocket.close()
			Host.download = True

		elif Host.check("ACKbit","2") & Host.check ("ack_num","203"):
			time.wait(10)
			clientSocket.sendto(str(Host).encode(),(serverName,9998))
			print("Waiting for the server to close")
		# closing the connection
		elif get_i_answer & get_ii_answer & get_iii_answer:
			Host.replace("FINbit",1)
			Host.replace("seq_num",203)
			clientSocket.sendto(str(Host).encode(),(serverName,9998))
			print("The server is starting to close its connection")
		
		message, serveraddr = clientSocket.recvfrom(2048)
		message = message.decode()
		message = str(message)
		Host.headptr = None
		Host.insert(message)