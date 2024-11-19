# DJ-AppStore Reverse Engineering (API)

## Overview

DJ-AppStore is a Tunisian AppStore (multi-platform)

**Server URL:**  
https://raw.githubusercontent.com/djopro-studios/DJ-APPSTORE/server-api-upd-side/server-api-universal


## Endpoints

### Apps

- **Get Apps List**  
  Fetch a list of available applications for the Windows platform.  
  `GET https://<URL>/get/windows`

- **Download App**  
  Initiate the download of an app by its ID. Specify the wallet ID to complete the transaction.  
  `GET https://<URL>/buy/windows/<ID>?wallet=<WALLET>`

- **Get App Icon**  
  Retrieve the icon of an app by its ID.  
  `GET https://<URL>/icon/windows/<ID>`

- **Add view**

   Add a view to an app.
   
  `POST https://<URL>/add_view/windows/ID`

### Wallet

- **Create Wallet**  
  Create a new wallet for transactions.  
  `POST https://<URL>/wallet/add`

- **Get Wallet (USELESS FOR NOW)**  
  Retrieve details about the current wallet.  
  `GET https://<URL>/wallet/`
We currenty have not found the variable where to put the wallet ID.
---

### Accounts

** Wait plz **


> Made by **EletrixTime**