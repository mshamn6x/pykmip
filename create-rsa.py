import ssl
from kmip.pie.client import ProxyKmipClient, enums
from kmip.pie import objects
from kmip.pie import client
from kmip import enums


#1633 thales
c = ProxyKmipClient(hostname='10.80.243.163',port=5696,cert='thales/cert.pem',key='thales/key.pem',ca='thales/rootca.pem',username='admin',password='Ami@1234',config='client')

#165 PYKMIP
#c = ProxyKmipClient(hostname='10.80.243.165',port=5696,cert='pykmip/cert.pem',key='pykmip/key.pem',ca='pykmip/rootca.pem',username='root',password='P@ssw0rd',config='client',config_file='server.conf')

#118 PYKMIP
#c = ProxyKmipClient(hostname='10.80.245.118',port=5696,cert='pykmip118/cert.pem',key='pykmip118/key.pem',ca='pykmip118/rootca.pem',username='root',password='P@ssw0rd',config='client',config_file='server.conf')


print("client")
print(c)


def AsymmetricKeyRSA():
    print("Perform AsymmetricKey Key OPERATION")
    with c:
        print("CREATE")
        key_id = c.create_key_pair(
            enums.CryptographicAlgorithm.RSA,
            1024,
            # operation_policy_name='default',
            # public_name='Test_2048_RSA_Public_Key',
            public_usage_mask=[
                enums.CryptographicUsageMask.VERIFY
            ],
            # private_name='Test_2048_RSA_Private_Key',
            private_usage_mask=[
                enums.CryptographicUsageMask.SIGN
            ]
        )  

        print("CREATED KEY ID ",key_id)
        print("Index one ",key_id[0])
        print("type ",type(key_id[0]))
        
        # print("GET KEY")
        # print(c.get(key_id[0]))

        # print("GET KEY")
        # print(c.get(key_id[1]))
        
        # print("GET KEY ATTRIBUTES [0]")
        # print(c.get_attributes(key_id[0]))
        
        # print("GET KEY ATTRIBUTES [1]")
        # print(c.get_attributes(key_id[1]))

        #print("DELETE PUBLIC KEY")
        #print(c.destroy(key_id[0]))

        #print("DELETE PRIVATE KEY")
        #print(c.destroy(key_id[1]))


def main():
    print("RSA KEY CREATION")
    AsymmetricKeyRSA()


if __name__ == "__main__":
    main()
