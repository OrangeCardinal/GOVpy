from government.international.imf.imf import IMF

#bls = BureauOfLaborStatistics()
#popular_series = bls.popular_series()
#print(popular_series)


imf = IMF()
database_id = 'HPDD'
#database_id = IMF_Database.GOVERNMENT_FINANCE_STATISTICS.value
#metadata_structure = imf.metadata_structure(database_id)
#print(metadata_structure)

data_structure = imf.data_structure(database_id)
print(data_structure)


#data = imf.compact_data(database_id,'1975','2018')
#print(data)
