import dns.resolver

def resolve_domains(input_file, dns_server):
    success_count = 0
    failure_count = 0

    try:
        with open(input_file, 'r') as file:
            domains = file.read().splitlines()

        resolver = dns.resolver.Resolver()
        if dns_server:
            resolver.nameservers = [dns_server]

        for domain in domains:
            try:
                answers = resolver.resolve(domain)
                for answer in answers:
                    print(f"Resolved {domain} to IP address: {answer.address}")
                success_count += 1
            except dns.resolver.NXDOMAIN:
                print(f"Failed to resolve {domain}: Domain does not exist")
                failure_count += 1
            except dns.resolver.NoAnswer:
                print(f"Failed to resolve {domain}: No answer found for the query")
                failure_count += 1
            except dns.resolver.NoNameservers:
                print(f"Failed to resolve {domain}: No nameservers found for the domain")
                failure_count += 1
            except dns.resolver.Timeout:
                print(f"Failed to resolve {domain}: Timeout while resolving")
                failure_count += 1
            except dns.resolver.NoRootNS:
                print(f"Failed to resolve {domain}: No root nameservers could be used")
                failure_count += 1
            except Exception as e:
                print(f"Failed to resolve {domain}: {str(e)}")
                failure_count += 1

        print("\nResolution summary:")
        print(f"Successful resolutions: {success_count}")
        print(f"Failed resolutions: {failure_count}")
        print(f"Total domains: {len(domains)}")
        print(f"Domains successfully resolved: {success_count}")
        print(f"Domains that failed to resolve: {failure_count}")

    except FileNotFoundError:
        print(f"File '{input_file}' not found.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    input_file = input("Enter the path to the text file containing domain names: ")
    dns_server = input("Enter the IP address of the DNS server (or press Enter to use default DNS): ")
    
    if not dns_server:
        dns_server = None
    
    resolve_domains(input_file, dns_server)

