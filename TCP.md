# TCP & UDP ( Transport Layer )

https://www.geeksforgeeks.org/tcp-and-udp-in-transport-layer/

Layer 3 or the Network layer uses IP or Internet Protocol which being a connection less protocol treats every packet individually and separately leading to lack of reliability during a transmission. For example, when data is sent from one host to another, each packet may take a different path even if it belongs to the same session. This means the packets may/may not arrive in the right order. Therefore, IP relies on the higher layer protocols to provide reliability.

- TCP : TCP is a layer 4 protocol which provides acknowledgement of the received packets and is also reliable as it resends the lost packets. It is better than UDP but due to these features it has an additional overhead. It is used by application protocols like HTTP and FTP.

- UDP : UDP is also a layer 4 protocol but unlike TCP it doesn’t provide acknowledgement of the sent packets. Therefore, it isn’t reliable and depends on the higher layer protocols for the same. But on the other hand it is simple, scalable and comes with lesser overhead as compared to TCP. It is used in video and voice streaming


### TCP v/s UDP

1. Session Multiplexing: A single host with a single IP address is able to communicate with multiple servers. While using TCP, first a connection must be established between the server and the receiver and the connection is closed when the transfer is completed. TCP also maintains reliability while the transfer is taking place.
UDP on the other hand sends no acknowledgement of receiving the packets. Therefore, provides no reliability.

2. Segmentation: Information sent is first broken into smaller chunks for transmission.

Maximum Transmission Unit or MTU of a Fastethernet is 1500 bytes whereas the theoretical value of TCP is 65495 bytes. Therefore, data has to be broken into smaller chunks before being sent to the lower layers. MSS or Maximum Segment Size should be set small enough to avoid fragmentation. TCP supports MSS and Path MTU discovery with which the sender and the receiver can automatically determine the maximum transmission capability.

UDP doesn’t support this; therefore it depends on the higher layer protocols for data segmentation.

3. Flow Control: If sender sends data faster than what receiver can process then the receiver will drop the data and then request for a retransmission, leading to wastage of time and resources. TCP provides end-to-end flow control which is realized using a sliding window. The sliding window sends an acknowledgement from receiver’s end regarding the data that the receiver can receive at a time.

UDP doesn’t implement flow control and depends on the higher layer protocols for the same.

4. Connection Oriented: TCP is connection oriented, i.e., it creates a connection for the transmission to take place, and once the transfer is over that connection is terminated.

UDP on the other hand is connectionless just like IP (Internet Protocol).


5. Reliability: TCP sends an acknowledgement when it receives a packet. It requests a retransmission in case a packet is lost.

UDP relies on the higher layer protocols for the same. 