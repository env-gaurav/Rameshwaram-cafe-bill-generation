pin_code = int(input("ENTER YOUR PIN CODE: ")) #560037
cafe_name = "THE RAMESHWARAM CAFE"
address = "#1 Green Avenue , ITPM Road,"
city = "Banglore"
gstin = " 29ABYFA2044B1ZG"
cust_name = input("CUSTOMER NAME: ")
t_date = "24/12/24"
t_time = "20:38"
token_no = 1107
c_name = "Devika"
bill_no = "RC/00413707"
fssai_no = "11222333001923"
cafe= f'''
          {cafe_name}
          {address}
          {city}
          PIN :{pin_code}
          {gstin}
          
----------------------------------------
NAME: {cust_name}
----------------------------------------
Date: {t_date}   Self Service: SS
{t_time}
Cashier:{c_name}        Bill No:
                      {bill_no}
Token No:
{token_no}
---------------------------------------
No Item     QTY       Price    Amount
GHEE PUDI    2         128      256
IDLI         2         85       170
PLAIN IDLI   1         38       38
---------------------------------------
TOTAL QTY    5    SUB TOTAL 251 , 464

                  CGST 2.5%       11.67
                  SGST 2.5%       11.67
----------------------------------------
             GRAND TOTAL          RS 487
-----------------------------------------
FSSAI Lic N0.  {fssai_no}
           THANK YOU VISIT AGAIN
           
   BEST TO CONSUME THE FOOD WITHIN 4 MINS
         FROM THE BILLING TIME

'''
print(cafe)