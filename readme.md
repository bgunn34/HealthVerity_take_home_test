##### Hello! This is my response to the HealthVerity take home test. 

##### This code was prepared using: 
	Python 3.9
	numpy 1.22.2
	pandas 1.4
	pytest 7.0.0
	notebook 6.4.8
	... and their dependencies. See requirements.txt for a full list.

##### I have answered questions 1 and 2 in the notebook Exploratory_Data_Analysis.

##### The tests I wrote for question 3 are in test_file_integrity.py. 
I found that the file had missing values in patient_id, claim_id, procedure_code, and date_service.
I found that there were multiple invalid cpt and icd codes.
I found that some rows had invalid service date formatting.
I found that some rows had service dates that occured after the received date (not logical for medical claims)
I found that some service dates had dates occuring many years in the future. 

However, the file columns were correct and the dtypes were good once the invalid pieces of data were filtered out.
