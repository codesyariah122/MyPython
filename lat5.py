def pembuat_password(website, tahun):
	return website.lower() +', '+ str(tahun * 11)

websiteKu = pembuat_password('pujiermanto.netlify.app', 2020)

print(websiteKu)