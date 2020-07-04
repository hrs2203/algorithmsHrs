# QoS: Quality of service ( Transport Layer )

https://www.geeksforgeeks.org/computer-network-quality-of-service-and-multimedia/

QoS refers to traffic control mechanisms that seek to either differentiate performance based on application or network-operator requirements or provide predictable or guaranteed performance to applications, sessions or traffic aggregates. Basic phenomenon for QoS means in terms of packet delay and losses of various kinds.

### Need

- Video and audio conferencing require bounded delay and loss rate.
- Video and audio streaming requires bounded packet loss rate, it may not be so sensitive to delay.
- Time-critical applications (real-time control) in which bounded delay is considered to be an important factor.
- Valuable applications should be provided better services than less valuable applications.

### QoS Specification –
QoS requirements can be specified as:

- Delay
- Delay Variation(Jitter)
- Throughput
- Error Rate

### Types of QoS Solutions 

- Stateless Solutions -> Routers maintain no fine grained state about traffic, one positive factor of it is that it is scalable and robust. But it has weak services as there is no guarantee about kind of delay or performance in a particular application which we have to encounter.

- Stateful Solutions -> Routers maintain per flow state as flow is very important in providing the Quality-of-Service i.e. providing powerful services such as guaranteed services and high resource utilization, provides protection and is much less scalable and robust. 