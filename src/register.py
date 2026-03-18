import pjsua2
import time

ASTERISK_IP = "10.10.40.60"  # fill in your Asterisk VM's IP
USERNAME = "btwphone"
PASSWORD = "btwphone123"


class MyAccount(pjsua2.Account):
    def onRegState(self, prm):
        info = self.getInfo()
        if info.regIsActive:
            print("Registered successfully!")
        elif prm.code == 200:
            print("Unregistered cleanly")
        else:
            print("Registration failed!")
        print(f"SIP status code: {prm.code}")


def main():
    # Create and initialize the endpoint (the pjsip engine)
    ep = pjsua2.Endpoint()
    ep.libCreate()
    ep_cfg = pjsua2.EpConfig()
    ep_cfg.logConfig.level = 0
    ep.libInit(ep_cfg)

    # Create a UDP transport on port 5060
    tcfg = pjsua2.TransportConfig()
    tcfg.port = 5060
    ep.transportCreate(pjsua2.PJSIP_TRANSPORT_UDP, tcfg)

    # Start the library
    ep.libStart()

    # Configure the account
    acc_cfg = pjsua2.AccountConfig()
    acc_cfg.idUri = f"sip:{USERNAME}@{ASTERISK_IP}"
    acc_cfg.regConfig.registrarUri = f"sip:{ASTERISK_IP}"
    cred = pjsua2.AuthCredInfo("digest", "*", USERNAME, 0, PASSWORD)
    acc_cfg.sipConfig.authCreds.append(cred)

    # Create the account and register
    acc = MyAccount()
    acc.create(acc_cfg)

    # Wait long enough to see the registration result
    time.sleep(5)

    # Clean up
    ep.libDestroy()


if __name__ == "__main__":
    main()
