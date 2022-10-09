# rDNS_lookup
Scan a CIDR block for open DNS port 53 then attempt a reverse DNS lookup of each open port using dnsrecon. 

## Requirements
python3

nmap

dnsrecon

## Usage
`python3 rDNS_lookup.py`
`Enter CIDR: 8.8.8.0/24` < must be in this format. Will not take an IP range.
