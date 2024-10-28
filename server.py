import socket
import struct

def start_tcp_server(host='127.0.0.1', port=13000):
    # Crea il socket TCP
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.bind((host, port))
    server_socket.listen(1)
    print(f"Server in ascolto su {host}:{port}")

    # Dimensione della struttura: 2 UINT (2 * 2 bytes = 4 bytes totali)
    struct_size = 4
    
    try:
        while True:
            client_socket, client_address = server_socket.accept()
            print(f"Connessione accettata da {client_address}")
            
            while True:
                try:
                    # Legge esattamente struct_size bytes
                    data = client_socket.recv(struct_size)
                    
                    if not data or len(data) < struct_size:
                        print("Client disconnesso o dati incompleti")
                        break
                    
                    # Decodifica i due numeri UINT (16-bit unsigned)
                    numero, count = struct.unpack('<HH', data)
                    print(f"Dati ricevuti - numero: {numero}, count: {count}")
                    
                except Exception as e:
                    print(f"Errore nella ricezione: {e}")
                    break
            
            client_socket.close()
            
    except KeyboardInterrupt:
        print("\nServer terminato dall'utente")
    finally:
        server_socket.close()

if __name__ == "__main__":
    start_tcp_server()