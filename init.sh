iptables -t nat -A OUTPUT -p tcp --dport 80 -j REDIRECT --to 3000
