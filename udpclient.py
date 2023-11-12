
import socket 
SERVER_PORT_INT  = 12000
SERVER_NAME_STR = 'localhost'
#SEVER_NAME_STR = '192.168.1.4' 
#SERVER_NAME_STR = 12000
#
with socket.socket(socket.AF_INET, socket.SOCK_DGRAM ) as client_socket:
  tx_message_str = input('Input lowercase sentance to transmit (tx):')
  print('TX:', tx_message_str)
  print('TO:', (SERVER_NAME_STR,SERVER_PORT_INT))
  client_socket.sendto(tx_message_str.encode(),(SERVER_NAME_STR,SERVER_PORT_INT))
  print('...sent...')
  print('...waiting...')
  rx_message_bytes, server_address = client_socket.recvfrom(2048)
  print('RX: ', rx_message_bytes.decode())
  print('FROM: ', server_address)
  


