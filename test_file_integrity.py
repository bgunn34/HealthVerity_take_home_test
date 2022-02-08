import pytest
import pandas as pd


df = pd.read_csv('data/sample_claims.csv')
valid_cpts = pd.read_csv('data/valid_cpt_codes.csv')
valid_icds = pd.read_csv('data/valid_icd_10_codes.csv')

def test_table_def():
	# checks that the claims file matches the provided table definition
	cols = [
		'patient_id',
		'claim_id',
		'diagnosis_codes',
		'procedure_code',
		'date_service',
		'date_received',
	]
	assert list(df.columns) == cols


def test_cpt_codes():
	# checks that all cpt codes in the claims data are valid
	assert df['procedure_code'].isin(valid_cpts['code']).all()


def test_icd_codes():
	# checks that all icd codes in the claims data are valid
	icd_lists = df['diagnosis_codes'].str.split('^')
	icds = icd_lists.explode()
	icds = icds.str.replace('.', '', regex=False)
	assert icds.isin(valid_icds['code']).all()


def test_service_date_na():
	# checks to make sure all claims have service dates.
	assert find_na('date_service') == 0


def test_received_date_na():
	# checks to make sure all claims have received dates.
	assert find_na('date_received') == 0


def test_serv_date_format():
	# checks if all date values are in YYYY-MM-DD format
	# the to_datetime call will error if the format is incorrect.
	serv_dts = df.loc[df['date_service'].notna(), 'date_service']
	serv_dts = pd.to_datetime(serv_dts, format='%Y-%m-%d', errors='raise')
	assert True


def test_rec_date_format():
	# checks if all date values are in YYYY-MM-DD format
	# the to_datetime call will error if the format is incorrect.
	rec_dts = df.loc[df['date_received'].notna(), 'date_received']
	rec_dts = pd.to_datetime(rec_dts, format='%Y-%m-%d', errors='raise')
	assert True


def test_date_values():
	# checks if all service dates < received dates.
	serv_dts = df.loc[df['date_service'].notna(), 'date_service']
	serv_dts = pd.to_datetime(serv_dts, format='%Y-%m-%d', errors='raise')

	rec_dts = df.loc[df['date_received'].notna(), 'date_received']
	rec_dts = pd.to_datetime(rec_dts, format='%Y-%m-%d', errors='raise')

	assert (serve_dts < rec_dts).all()


def test_claim_id_na():
	# checks to make sure all claims have claim ids.
	assert find_na('claim_id') == 0


def test_claim_id():
	# checks if all claim ids are ints. filters na's since we're testing those 
	# separately.
	claim_ids = df.loc[df['claim_id'].notna(), 'claim_id']
	assert claim_ids.eq(claim_ids.astype(int)).all()


def test_patient_na():
	# checks to make sure all claims have patient ids.
	assert find_na('patient_id') == 0


def test_procedure_code_na():
	# checks to make sure all claims have procedure codes.
	assert find_na('procedure_code') == 0


def find_na(col):
	# takes a column and checks for na in that column
	print(df.loc[df[col].isna(), 'claim_id'])
	return df.loc[df[col].isna()].size