const METHODS = `
_______________________________________________________________________________
|                                                                             |
|                           ATTACKING METHODS VIP                             |  
|_____________________________________________________________________________|
|                                                                             |
| Layer 7:                                                                    |
|                                                                             |
| Http Hunt: node http.js <IP> <THREADS> <TIME> <CF OR HTTP2>                 |
| Https Hunt: node https.js <IP> <THREADS> <TIME>                             |
|                                                                             |
|_____________________________________________________________________________|
|                                                                             |
| Layer 4:                                                                    |
|                                                                             |
| Udp Nuke: node udpnuke.js <IP> <PORT> <SIZE> <TIME>                         |
| LDoS: node ldos.js <IP> <PORT> <THREADS> <TIME>                             |
| Tcp Flood: node tcpflood.js <IP> <PORT> <SIZE> <TIME>                       |
| Dns Flood: node dns.js <IP> <PORT> <SIZE> <TIME>                            |
| Tls Flood: node tls.js <HOST> <PORT> <TIME>                                 |
| Syn Flood: node syn.js <IP> <PORT> <TIME   >                                |
| Minecraft: node minecraft.js <IP> <PORT> <SIZE> <TIME>                      |
| FiveM: node fivem.js <IP> <PORT> <SIZE> <TIME>                              |
| Message: node msg.js <TCP OR UDP> <IP> <PORT> <MESSAGE>                     |
| Comp: node comp.js                                                          |
|                                                                             |
|_____________________________________________________________________________|
|                                                                             |
| Layer 3:                                                                    |
|                                                                             |
| ICMP-RAW: icmp.py <IP> <PACKETS>                                            |
|                                                                             |
|_____________________________________________________________________________|                                                
`;

console.log(METHODS);
