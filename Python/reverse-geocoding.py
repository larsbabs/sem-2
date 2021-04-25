import reverse_geocoder as rg

coords = (51.361376, 5.321991)
babs = rg.search(coords)
print(babs)