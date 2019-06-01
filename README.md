# Musical Bassoon
MITM software to intercept and change HTTP download packets to any sort of executable.

This works for redirection
- iptables -t nat -A OUTPUT -p tcp --dport 80 -j REDIRECT --to 8080
