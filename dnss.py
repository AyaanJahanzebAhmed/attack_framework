import dns.resolver
import sys
def dns_cap(domain):
    record_types = ['A', 'AAAA', 'NS', 'CNAME', 'MX', 'PTR', 'SOA', 'TXT']

    data = {}
    for records in record_types:
        try:
            answer = dns.resolver.query(domain, records)
            #print(type(answer))
            loopp = []
            #print(f'\n{records} Records')
            dictt = {}
            for server in answer:
                #print(server.to_text())
                loopp.append((server.to_text()))
            dictt[str(records)]= loopp
            data.update(dictt)
            print(loopp)
        except dns.resolver.NoAnswer:
            pass
        except dns.resolver.NXDOMAIN:
            #print(f'{domain} does not exist.')
            quit()
        except KeyboardInterrupt:
            #print('Quitting.')
            quit()
    print(data)
