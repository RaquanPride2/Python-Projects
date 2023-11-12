# My udpserver
import  socket 
SERVER_HOST_STR = "localhost" 
SERVER_PORT_INT = 12000
MAX_BYTES_RX_INT = 2048 
with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as active_socket:
    active_socket.bind((SERVER_HOST_STR,SERVER_PORT_INT))
    print('The echo server is ready to recieve and SEND BACK')
    while True:
      print('...socket listening...press ctrl-c to quit')
      rxd_message_bytes, client_address = active_socket.recvfrom(MAX_BYTES_RX_INT)
      print('MESSAGE RXD:') 
      print('  FROM:', client_address)
      rxd_message_str = rxd_message_bytes.decode()
      print('  MSG :', rxd_message_str)
      tx_message_str = rxd_message_str.upper()
      print('MESSAGE TX:') 
      print('  TO:', client_address) 
      print('  MSG :', tx_message_str)
      tx_message_bytes = tx_message_str.encode()
      active_socket.sendto(tx_message_bytes, client_address)
      print('...sent data to the socket...') 


















 
 
 
