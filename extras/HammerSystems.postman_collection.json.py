{
	"info": {
		"_postman_id": "b513eed5-c984-4916-a43d-524f5c8verf4",
		"name": "HammerSystems",
		"schema": "https://schema.getpostman.com/json/collection/v2.1.0/collection.json"
	},
	"item": [
		{
			"name": "Landing Page",
			"request": {
				"method": "GET",
				"header": [],
				"url": {
					"raw": "http://51.159.148.219:1520/",
					"protocol": "http",
					"host": [
						"51",
						"159",
						"148",
						"219"
					],
					"port": "1520",
					"path": [
						""
					]
				}
			},
			"response": []
		},
		{
			"name": "Auth Page",
			"request": {
				"method": "GET",
				"header": [],
				"url": {
					"raw": "http://51.159.148.219:1520/auth",
					"protocol": "http",
					"host": [
						"51",
						"159",
						"148",
						"219"
					],
					"port": "1520",
					"path": [
						"auth"
					]
				}
			},
			"response": []
		},
		{
			"name": "Submit Phone Number",
			"request": {
				"method": "POST",
				"header": [],
				"body": {
					"mode": "raw",
					"raw": "{\"phone_number\": \"+79123456789\"}",
					"options": {
						"raw": {
							"language": "json"
						}
					}
				},
				"url": {
					"raw": "http://51.159.148.219:1520/api/auth",
					"protocol": "http",
					"host": [
						"51",
						"159",
						"148",
						"219"
					],
					"port": "1520",
					"path": [
						"api",
						"auth"
					]
				}
			},
			"response": []
		},
		{
			"name": "Validate Phone Number",
			"request": {
				"method": "POST",
				"header": [],
				"body": {
					"mode": "raw",
					"raw": "{\"phone_number\": \"+79123456789\", \"code\": 7598}",
					"options": {
						"raw": {
							"language": "json"
						}
					}
				},
				"url": {
					"raw": "http://51.159.148.219:1520/api/verify",
					"protocol": "http",
					"host": [
						"51",
						"159",
						"148",
						"219"
					],
					"port": "1520",
					"path": [
						"api",
						"verify"
					]
				}
			},
			"response": []
		},
		{
			"name": "Invalid Confirmation Code",
			"request": {
				"method": "POST",
				"header": [],
				"body": {
					"mode": "raw",
					"raw": "{\"phone_number\": \"+79123456789\", \"code\": 7598}",
					"options": {
						"raw": {
							"language": "json"
						}
					}
				},
				"url": {
					"raw": "http://51.159.148.219:1520/api/verify",
					"protocol": "http",
					"host": [
						"51",
						"159",
						"148",
						"219"
					],
					"port": "1520",
					"path": [
						"api",
						"verify"
					]
				}
			},
			"response": []
		},
		{
			"name": "Get Profile Fail Invalid JWT Headers",
			"request": {
				"method": "GET",
				"header": [
					{
						"key": "Cookie",
						"value": "access_token=;refresh_token=;",
						"type": "text"
					}
				],
				"url": {
					"raw": "http://51.159.148.219:1520/api/profile",
					"protocol": "http",
					"host": [
						"51",
						"159",
						"148",
						"219"
					],
					"port": "1520",
					"path": [
						"api",
						"profile"
					]
				}
			},
			"response": []
		},
		{
			"name": "Get Profile",
			"request": {
				"method": "GET",
				"header": [
					{
						"key": "Cookie",
						"value": "access_token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJhdWQiOiJoYW1tZXI6YXV0aCIsImlhdCI6MTY0ODA4NTY4OC4yOTU0MTgsImV4cCI6MTY0ODA4NTk4OC4yOTU0MjYsInBob25lX251bWJlciI6Iis3OTY4NTEyNzE1NyIsImlkZW50aWZpZXIiOiJbTVFVT10iLCJpZCI6MX0.mEPwQlXDQ7ag0zAXLo0sUy0Zrm-OHXNRDlIZso01oyo;refresh_token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJhdWQiOiJoYW1tZXI6YXV0aCIsImlhdCI6MTY0ODA4NTY4OC4yOTU2NzEsImV4cCI6MTY3OTYyMTY4OC4yOTU2NzMsInBob25lX251bWJlciI6Iis3OTY4NTEyNzE1NyIsImlkZW50aWZpZXIiOiJbTVFVT10iLCJpZCI6MX0.ie3cGGacKb2xdH8PS5B_iMOYhUrndwa6yoi84DzAuJQ;",
						"type": "text"
					}
				],
				"url": {
					"raw": "http://51.159.148.219:1520/api/profile",
					"protocol": "http",
					"host": [
						"51",
						"159",
						"148",
						"219"
					],
					"port": "1520",
					"path": [
						"api",
						"profile"
					]
				}
			},
			"response": []
		},
		{
			"name": "Register One More User",
			"request": {
				"method": "POST",
				"header": [
					{
						"key": "Cookie",
						"value": "access_token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJhdWQiOiJoYW1tZXI6YXV0aCIsImlhdCI6MTY0ODA4NTY4OC4yOTU0MTgsImV4cCI6MTY0ODA4NTk4OC4yOTU0MjYsInBob25lX251bWJlciI6Iis3OTY4NTEyNzE1NyIsImlkZW50aWZpZXIiOiJbTVFVT10iLCJpZCI6MX0.mEPwQlXDQ7ag0zAXLo0sUy0Zrm-OHXNRDlIZso01oyo;refresh_token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJhdWQiOiJoYW1tZXI6YXV0aCIsImlhdCI6MTY0ODA4NTY4OC4yOTU2NzEsImV4cCI6MTY3OTYyMTY4OC4yOTU2NzMsInBob25lX251bWJlciI6Iis3OTY4NTEyNzE1NyIsImlkZW50aWZpZXIiOiJbTVFVT10iLCJpZCI6MX0.ie3cGGacKb2xdH8PS5B_iMOYhUrndwa6yoi84DzAuJQ;",
						"type": "text",
						"disabled": true
					}
				],
				"body": {
					"mode": "raw",
					"raw": "{\"phone_number\": \"+79685127100\"}",
					"options": {
						"raw": {
							"language": "json"
						}
					}
				},
				"url": {
					"raw": "http://51.159.148.219:1520/api/auth",
					"protocol": "http",
					"host": [
						"51",
						"159",
						"148",
						"219"
					],
					"port": "1520",
					"path": [
						"api",
						"auth"
					]
				}
			},
			"response": []
		},
		{
			"name": "Enter As New User",
			"request": {
				"method": "POST",
				"header": [
					{
						"key": "Cookie",
						"value": "access_token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJhdWQiOiJoYW1tZXI6YXV0aCIsImlhdCI6MTY0ODA4NTY4OC4yOTU0MTgsImV4cCI6MTY0ODA4NTk4OC4yOTU0MjYsInBob25lX251bWJlciI6Iis3OTY4NTEyNzE1NyIsImlkZW50aWZpZXIiOiJbTVFVT10iLCJpZCI6MX0.mEPwQlXDQ7ag0zAXLo0sUy0Zrm-OHXNRDlIZso01oyo;refresh_token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJhdWQiOiJoYW1tZXI6YXV0aCIsImlhdCI6MTY0ODA4NTY4OC4yOTU2NzEsImV4cCI6MTY3OTYyMTY4OC4yOTU2NzMsInBob25lX251bWJlciI6Iis3OTY4NTEyNzE1NyIsImlkZW50aWZpZXIiOiJbTVFVT10iLCJpZCI6MX0.ie3cGGacKb2xdH8PS5B_iMOYhUrndwa6yoi84DzAuJQ;",
						"type": "text",
						"disabled": true
					}
				],
				"body": {
					"mode": "raw",
					"raw": "{\"phone_number\": \"+79685127100\", \"code\": 5679}",
					"options": {
						"raw": {
							"language": "json"
						}
					}
				},
				"url": {
					"raw": "http://51.159.148.219:1520/api/verify",
					"protocol": "http",
					"host": [
						"51",
						"159",
						"148",
						"219"
					],
					"port": "1520",
					"path": [
						"api",
						"verify"
					]
				}
			},
			"response": []
		},
		{
			"name": "Add Friend",
			"request": {
				"method": "POST",
				"header": [
					{
						"key": "Cookie",
						"value": "access_token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJhdWQiOiJoYW1tZXI6YXV0aCIsImlhdCI6MTY0ODA4NjA3Ny45Njg4MjIsImV4cCI6MTY0ODA4NjM3Ny45Njg4MywicGhvbmVfbnVtYmVyIjoiKzc5Njg1MTI3MTAwIiwiaWRlbnRpZmllciI6Ilg9Zz8zSSIsImlkIjozfQ.NLbh_Bkj2kluIeAoSoUILPVnnQj3PGa8nGKddwUVAS4;refresh_token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJhdWQiOiJoYW1tZXI6YXV0aCIsImlhdCI6MTY0ODA4NjA3Ny45NjkwNDMsImV4cCI6MTY3OTYyMjA3Ny45NjkwNDYsInBob25lX251bWJlciI6Iis3OTY4NTEyNzEwMCIsImlkZW50aWZpZXIiOiJYPWc_M0kiLCJpZCI6M30.5aJNcLVC7rVI9iEuswGORucfWp2nG3EX8DF5EKJSA3c;",
						"type": "text"
					}
				],
				"body": {
					"mode": "raw",
					"raw": "{\"friend_identifier\":\"[MQUO]\"}"
				},
				"url": {
					"raw": "http://51.159.148.219:1520/api/add/friend",
					"protocol": "http",
					"host": [
						"51",
						"159",
						"148",
						"219"
					],
					"port": "1520",
					"path": [
						"api",
						"add",
						"friend"
					]
				}
			},
			"response": []
		},
		{
			"name": "Invalid Phone Format",
			"request": {
				"method": "POST",
				"header": [
					{
						"key": "Cookie",
						"value": "access_token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJhdWQiOiJoYW1tZXI6YXV0aCIsImlhdCI6MTY0ODA4NjA3Ny45Njg4MjIsImV4cCI6MTY0ODA4NjM3Ny45Njg4MywicGhvbmVfbnVtYmVyIjoiKzc5Njg1MTI3MTAwIiwiaWRlbnRpZmllciI6Ilg9Zz8zSSIsImlkIjozfQ.NLbh_Bkj2kluIeAoSoUILPVnnQj3PGa8nGKddwUVAS4;refresh_token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJhdWQiOiJoYW1tZXI6YXV0aCIsImlhdCI6MTY0ODA4NjA3Ny45NjkwNDMsImV4cCI6MTY3OTYyMjA3Ny45NjkwNDYsInBob25lX251bWJlciI6Iis3OTY4NTEyNzEwMCIsImlkZW50aWZpZXIiOiJYPWc_M0kiLCJpZCI6M30.5aJNcLVC7rVI9iEuswGORucfWp2nG3EX8DF5EKJSA3c;",
						"type": "text",
						"disabled": true
					}
				],
				"body": {
					"mode": "raw",
					"raw": "{\"phone_number\":\"\"}"
				},
				"url": {
					"raw": "http://51.159.148.219:1520/api/auth",
					"protocol": "http",
					"host": [
						"51",
						"159",
						"148",
						"219"
					],
					"port": "1520",
					"path": [
						"api",
						"auth"
					]
				}
			},
			"response": []
		},
		{
			"name": "Refresh JWT",
			"protocolProfileBehavior": {
				"disableBodyPruning": true
			},
			"request": {
				"method": "GET",
				"header": [
					{
						"key": "Cookie",
						"value": "access_token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJhdWQiOiJoYW1tZXI6YXV0aCIsImlhdCI6MTY0ODA4NjA3Ny45Njg4MjIsImV4cCI6MTY0ODA4NjM3Ny45Njg4MywicGhvbmVfbnVtYmVyIjoiKzc5Njg1MTI3MTAwIiwiaWRlbnRpZmllciI6Ilg9Zz8zSSIsImlkIjozfQ.NLbh_Bkj2kluIeAoSoUILPVnnQj3PGa8nGKddwUVAS4;refresh_token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJhdWQiOiJoYW1tZXI6YXV0aCIsImlhdCI6MTY0ODA4NjA3Ny45NjkwNDMsImV4cCI6MTY3OTYyMjA3Ny45NjkwNDYsInBob25lX251bWJlciI6Iis3OTY4NTEyNzEwMCIsImlkZW50aWZpZXIiOiJYPWc_M0kiLCJpZCI6M30.5aJNcLVC7rVI9iEuswGORucfWp2nG3EX8DF5EKJSA3c;",
						"type": "text"
					}
				],
				"body": {
					"mode": "raw",
					"raw": "",
					"options": {
						"raw": {
							"language": "json"
						}
					}
				},
				"url": {
					"raw": "http://51.159.148.219:1520/api/token/refresh",
					"protocol": "http",
					"host": [
						"51",
						"159",
						"148",
						"219"
					],
					"port": "1520",
					"path": [
						"api",
						"token",
						"refresh"
					]
				}
			},
			"response": []
		}
	]
}