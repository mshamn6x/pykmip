import ssl
from kmip.pie.client import ProxyKmipClient, enums
from kmip.pie import objects
from kmip.pie import client
from kmip import enums

c = ProxyKmipClient(hostname='10.80.243.165',port=5696,cert='/etc/pykmip/certs/client_certificate.pem',key='/etc/pykmip/certs/client_key.pem',ca='/etc/pykmip/certs/root_certificate.pem',username='root',password='P@ssw0rd',config='client',config_file='/etc/pykmip/server.conf')

print("client")
print(c)


# symmetric_key = objects.SymmetricKey(
#     enums.CryptographicAlgorithm.AES,
#      128,
#     (
#         b'\x00\x01\x02\x03\x04\x05\x06\x07'
#         b'\x08\x09\x0A\x0B\x0C\x0D\x0E\x0F'
#     )
# )


# with c:
#     key_id = c.register(symmetric_key)
#     c.activate(key_id)

# with c:
#     key_id = c.create(
#         enums.CryptographicAlgorithm.AES,
#         256,
#         operation_policy_name='default',
#         name='Test_256_AES_Symmetric_Key',
#         cryptographic_usage_mask=[
#             enums.CryptographicUsageMask.ENCRYPT,
#             enums.CryptographicUsageMask.DECRYPT
#         ]
#     )

#     print("key_id")
#     print(key_id)

    
#     print(c.get(key_id))

#     print(c.get_attribute_list(key_id))


# print("Asymmetric Key creation")

# with c:
#     key_id = c.create_key_pair(
#         enums.CryptographicAlgorithm.RSA,
#         2048,
#         operation_policy_name='default',
#         public_name='Test_2048_RSA_Public_Key',
#         public_usage_mask=[
#             enums.CryptographicUsageMask.VERIFY
#         ],
#         private_name='Test_2048_RSA_Private_Key',
#         private_usage_mask=[
#             enums.CryptographicUsageMask.SIGN
#         ]
#     )   

#     print("RSA key_id")
#     print(key_id)

#     print("Type of RSA key_id")
#     print(type(key_id))
    
#     print(c.get(key_id))

#     print(c.get_attribute_list(key_id[0]))
#     print(c.get_attribute_list(key_id[1]))

# with c:
#     key_id='18'
#     print("RSA key_id")
#     print(key_id)

#     print(c.get(key_id))
    
#     print("Attribute List")
#     print(c.get_attribute_list(key_id))

#     print("Attribute")
#     print(c.get_attributes(key_id))



def SymmetricKey():
    print("Perform Symmetric Key OPERATION")
    with c:
        print("CREATE")
        key_id = c.create(
            enums.CryptographicAlgorithm.AES,
            256,
            operation_policy_name='default',
            name='Test_256_AES_Symmetric_Key',
            cryptographic_usage_mask=[
                enums.CryptographicUsageMask.ENCRYPT,
                enums.CryptographicUsageMask.DECRYPT
            ]
        )

        print("CREATED KEY ID "+key_id)
        
        print("GET KEY")
        print(c.get(key_id))
        
        print("GET KEY ATTRIBUTES")
        print(c.get_attributes(key_id))

        # print("DELETE KEY")
        # print(c.destroy(key_id))


def AsymmetricKey():
    print("Perform AsymmetricKey Key OPERATION")
    with c:
        print("CREATE")
        key_id = c.create_key_pair(
            enums.CryptographicAlgorithm.RSA,
            2048,
            operation_policy_name='default',
            public_name='Test_2048_RSA_Public_Key',
            public_usage_mask=[
                enums.CryptographicUsageMask.VERIFY
            ],
            private_name='Test_2048_RSA_Private_Key',
            private_usage_mask=[
                enums.CryptographicUsageMask.SIGN
            ]
        )  

        print("CREATED KEY ID ",key_id)
        print("Index one ",key_id[0])
        print("type ",type(key_id[0]))
        
        print("GET KEY")
        print(c.get(key_id[0]))

        print("GET KEY")
        print(c.get(key_id[1]))
        
        print("GET KEY ATTRIBUTES [0]")
        print(c.get_attributes(key_id[0]))
        
        print("GET KEY ATTRIBUTES [1]")
        print(c.get_attributes(key_id[1]))

        print("DELETE PUBLIC KEY")
        print(c.destroy(key_id[0]))

        print("DELETE PRIVATE KEY")
        print(c.destroy(key_id[1]))


def main():
    print("Hello World!")
    #SymmetricKey()
    print("NEXT RSA KEY CREATION")
    AsymmetricKey()


if __name__ == "__main__":
    main()
