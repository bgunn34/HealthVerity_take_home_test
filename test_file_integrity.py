import pytest
import pandas as pd

## specifying dtypes at load will produce an error if data is included that
## is incompatable with that type.
dtypes = {
	'patient_id': str,
	'claim_id': int,
	'diagnosis_code': str,
	'procedure_code': int,
	'date_service': str,
	'date_received': str,
}
df = pd.read_csv('data/sample_claims.csv', dtype=dtypes)
valid_cpts = pd.read_csv('data/valid_cpt_codes.csv')
valid_icds = pd.read_csv('data/valid_icd_10_codes.csv')

def test_table_def():
	# checks that the claims file matches the provided 
	pass


def test_cpt_codes():
	# checks that all cpt codes in the claims data are valid
	pass


def test_icd_codes():
	# checks that all icd codes in the claims data are valid
	pass


def test_date_format():
	# checks if all date values are in YYYY-MM-DD format
	pass


def test_date_values():
	# checks if all service dates < received dates.
	pass


def test_claim_id():
	# checks if all claim ids are numeric.
	pass


def test_patient_na():
	# checks to make sure all claims have patient ids.
	assert find_na('patient_id') == 0


def test_claim_id_na():
	# checks to make sure all claims have claim ids.
	assert find_na('claim_id')


def test_procedure_code_na():
	# checks to make sure all claims have procedure codes.
	assert find_na('procedure_code')


def test_service_date_na():
	# checks to make sure all claims have service dates.
	assert find_na('date_service')


def test_received_date_na():
	# checks to make sure all claims have received dates.
	assert find_na('date_received')


def find_na(col):
	# takes a column and checks for na in that column
	print(df.loc[df[col].isna(), 'claim_id'])
	return df.loc[df[col].isna()].size