Authors: Haziq Usman, Moeed Ahmad, Alliya Fatima, Harram Khan, Asfandyar Bin Tassadaq

Client-Server virtual file-system:

Clients choose the server IP and connect to it. Once connected, they can perform functions on the .dat file,which acts as our harddrive.
All functions on our harddrive are perfomed on the client's side. The .dat file is maintained at the server. Every client gets their own thread, 
and  every thread maintains the filesystem. When any of the threads close, then the change made on that specific thread gets reflected globally.