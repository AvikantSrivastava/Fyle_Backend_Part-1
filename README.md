# [**Fyle Full Stack Coding Challenge**](https://www.notion.so/Fyle-Full-Stack-Coding-Challenge-db30c5cb91d54de1b330c16f22fc49f0) [Part 1]

## Live Demo [Link](https://flye-backend-avikant.herokuapp.com/)

## API usage
**1) Autocomplete API**
Autocomplete API to return possible matches based on the branch name ordered by IFSC code (ascending order) with limit and offset.

- **Endpoint: /api/branches/autocomplete?q=<>**

- **Example: /api/branches/autocomplete?q=**RTGS**&limit=3&offset=0**

```bash
curl -i -H "Accept: application/json" https://flye-backend-avikant.herokuapp.com/api/branches/autocomplete?q=bangalore&limit=5&offset=1

```

**API Response**
```json
{
   "branches":[
      {
         "ifsc":"ABNA0100318",
         "bank_id":110,
         "branch":"BANGALORE",
         "address":"PRESTIGE TOWERS', GROUND FLOOR, 99 & 100, RESIDENCY ROAD, BANGALORE 560 025.",
         "city":"BANGALORE",
         "district":"BANGALORE URBAN",
         "state":"KARNATAKA"
      },
      {
         "ifsc":"ADCB0000002",
         "bank_id":143,
         "branch":"BANGALORE",
         "address":"CITI CENTRE, 28, CHURCH STREET, OFF M. G. ROAD BANGALORE 560001",
         "city":"BANGALORE",
         "district":"BANGALORE URBAN",
         "state":"KARNATAKA"
      },
      {
         "ifsc":"ALLA0210326",
         "bank_id":11,
         "branch":"BANGALORE BASAVANGUDI",
         "address":"121, RM COMPLEX, DR.D.V.GUNDAPPA ROAD, BASAVANGUDI, BANGALORE - 560004",
         "city":"BANGALORE",
         "district":"BANGALORE URBAN",
         "state":"KARNATAKA"
      }
   ]
}
```

**2) Search API**

Search API to return possible matches across all columns and all rows, **ordered by IFSC code** (ascending order) with limit and offset.

```bash
curl -i -H "Accept: application/json" https://flye-backend-avikant.herokuapp.com/api/branches?q=delhi&limit=5&offset=1
```

-  **Endpoint: /api/branches?q=<>**
-  **Example: /api/branches?q=**Bangalore**&limit=4&offset=0**


**API Response**
```json
{
   "branches":[
      {
         "ifsc":"ABNA0100327",
         "bank_id":110,
         "branch":"HAUZ KHAS  NEW DELHI",
         "address":"M-6 HAUZ KHAS, NEW DELHI 110016",
         "city":"DELHI",
         "district":"NEW DELHI",
         "state":"DELHI"
      },
      {
         "ifsc":"ABNA0100328",
         "bank_id":110,
         "branch":"GK 1  NEW DELHI",
         "address":"R-67, GREATER KAILASH-I, NEW DELHI - 110048",
         "city":"DELHI",
         "district":"NEW DELHI",
         "state":"DELHI"
      },
      {
         "ifsc":"ABNA0100329",
         "bank_id":110,
         "branch":"RAJOURI GARDEN  NEW DELHI",
         "address":"J-12/11 RAJOURI GARDEN,NEW DELHI-110027",
         "city":"DELHI",
         "district":"NEW DELHI",
         "state":"DELHI"
      },
      {
         "ifsc":"ALLA0210145",
         "bank_id":11,
         "branch":"WRIGHTGANJ",
         "address":"HAPUR ROAD, WRIGHT GANJ, GHAZIABAD",
         "city":"DELHI",
         "district":"NEW DELHI",
         "state":"DELHI"
      },
      {
         "ifsc":"ALLA0210158",
         "bank_id":11,
         "branch":"CHANDNI CHOWK",
         "address":"4398, CHANDNI CHOWK, POST BOX NO. 1027",
         "city":"DELHI",
         "district":"NEW DELHI",
         "state":"DELHI"
      }
   ]
}
```

## Task List
- [X] Setup Flask Server
- [X] Setup Credentials in Environment variable
- [X] Setup Database Connection
- [X] Work on API
- [X] API Testing
- [X] Heroku Deployment