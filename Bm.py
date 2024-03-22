
print(f"IP address version: {version}")
    print(f"Is private: {is_private}")
    print(f"Is global: {is_global}")
    print(f"Is multicast: {is_multicast}")
    print(f"Is reserved: {is_reserved}")
    print(f"Is loopback: {is_loopback}")
    print(f"Is link-local: {is_link_local}")
    print(f"Is site-local: {is_site_local}")

except ValueError:
    print("Invalid IP address format.")
