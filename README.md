# Shalish
MITM software to intercept and change HTTP download packets to any sort of executable.

First Test (Traffic towards victim)
- Figure out victim's ip address
- Create iptable rule that redirects every HTTP connection for that IP address towards a proxy server
  - Internet --> MITM -(iptable rule)-> Victim
- The proxy server checks if it is downloading a file and then changes accordingly

Second Test (Traffic exiting victim)
- Redirect all of victim's outgoing HTTP connection to proxy server
  - Internet <-- MITM <-(iptable rule)- Victim
- Proxy server then changes the source if it is downloading a file
