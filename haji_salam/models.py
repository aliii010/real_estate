from django.db import models

# Create your models here.
class Property(models.Model):
  CITIES = [
    ("erbil", "erbil"),
    ("sulaymaniyah", "sulaymaniyah"),
    ("duhok", "duhok"),
  ]

  REGIONS = [
    ('100m road', 'Erbil, 100m road'), ('5 Hasarok', 'Erbil, 5 Hasarok'), ('Ainkawa', 'Erbil, Ainkawa'), ('Amin Amakan', 'Erbil, Amin Amakan'), ('Andazyaran', 'Erbil, Andazyaran'), ('Aras', 'Erbil, Aras'), ('Azadi', 'Erbil, Azadi'), ('Badawa', 'Erbil, Badawa'), ('Bakhtyari', 'Erbil, Bakhtyari'), ('Brayati', 'Erbil, Brayati'), ('Dolarawa', 'Erbil, Dolarawa'), ('Farmanbaran', 'Erbil, Farmanbaran'), ('Galawezh', 'Erbil, Galawezh'), ('Gulan', 'Erbil, Gulan'), ('Hamreen', 'Erbil, Hamreen'), ('Havalan', 'Erbil, Havalan'), ('Hawari Shar', 'Erbil, Hawari Shar'), ('Hawleri Nwe', 'Erbil, Hawleri Nwe'), ('Iskan', 'Erbil, Iskan'), ('Kani', 'Erbil, Kani'), ('Karezan', 'Erbil, Karezan'), ('Kark', 'Erbil, Kark'), ('Kasnazan', 'Erbil, Kasnazan'), ('Khanzad', 'Erbil, Khanzad'), ('Komari', 'Erbil, Komari'), ('Kuran', 'Erbil, Kuran'), ('Kurani Nwe', 'Erbil, Kurani Nwe'), ('Kwestan', 'Erbil, Kwestan'), ('Mamostayan', 'Erbil, Mamostayan'), ('Mamostayani Zanko', 'Erbil, Mamostayani Zanko'), ('Mantkawa', 'Erbil, Mantkawa'), ('Mardin', 'Erbil, Mardin'), ('Mnara', 'Erbil, Mnara'), ('Mohandisin', 'Erbil, Mohandisin'), ('Mufti', 'Erbil, Mufti'), ('Nawroz (Nishtiman)', 'Erbil, Nawroz (Nishtiman)'), ('Naz naz', 'Erbil, Naz naz'), ('Nusaran', 'Erbil, Nusaran'), ('Qarabu', 'Erbil, Qarabu'), ('Raparin', 'Erbil, Raparin'), ('Rasty', 'Erbil, Rasty'), ('Ronaki', 'Erbil, Ronaki'), ('Roshnbiry', 'Erbil, Roshnbiry'), ('Rzgari', 'Erbil, Rzgari'), ('Sarbasty (32 park)', 'Erbil, Sarbasty (32 park)'), ('Sarwaran', 'Erbil, Sarwaran'), ('Setaqan', 'Erbil, Setaqan'), ('Sharawani', 'Erbil, Sharawani'), ('Shorish', 'Erbil, Shorish'), ('Tairawa', 'Erbil, Tairawa'), ('Waziran', 'Erbil, Waziran'), ('Zanko Village', 'Erbil, Zanko Village'), ('Zhiyan', 'Erbil, Zhiyan'), ('Ziraa', 'Erbil, Ziraa'), ('zanyari', 'Erbil, zanyari'), ('60 road', 'Sulaymaniyah, 60 road'), ('Altun', 'Sulaymaniyah, Altun'), ('Andazyaran', 'Sulaymaniyah, Andazyaran'), ('Aqary', 'Sulaymaniyah, Aqary'), ('Ashty', 'Sulaymaniyah, Ashty'), ('Ashty', 'Sulaymaniyah, Ashty'), ('Azady', 'Sulaymaniyah, Azady'), ('Bahary shar', 'Sulaymaniyah, Bahary shar'), ('Bahashty shar', 'Sulaymaniyah, Bahashty shar'), ('Bakhtiari', 'Sulaymaniyah, Bakhtiari'), ('Bakrajo', 'Sulaymaniyah, Bakrajo'), ('Baranan', 'Sulaymaniyah, Baranan'), ('Bazrgani', 'Sulaymaniyah, Bazrgani'), ('Chwarbax', 'Sulaymaniyah, Chwarbax'), ('Chwarchra', 'Sulaymaniyah, Chwarchra'), ('Dukan', 'Sulaymaniyah, Dukan'), ('Family mall', 'Sulaymaniyah, Family mall'), ('Grdy Andazyaran', 'Sulaymaniyah, Grdy Andazyaran'), ('Grdy Sarchnar', 'Sulaymaniyah, Grdy Sarchnar'), ('Harawazy', 'Sulaymaniyah, Harawazy'), ('Hawara Barza', 'Sulaymaniyah, Hawara Barza'), ('Hawary shar', 'Sulaymaniyah, Hawary shar'), ('Hiron City', 'Sulaymaniyah, Hiron City'), ('Kani askan', 'Sulaymaniyah, Kani askan'), ('Kany kurda', 'Sulaymaniyah, Kany kurda'), ('Kaziwa', 'Sulaymaniyah, Kaziwa'), ('Majidbag', 'Sulaymaniyah, Majidbag'), ('Malkandi', 'Sulaymaniyah, Malkandi'), ('Mamostayan', 'Sulaymaniyah, Mamostayan'), ('Mawalawi', 'Sulaymaniyah, Mawalawi'), ('Qaradagh', 'Sulaymaniyah, Qaradagh'), ('Qaratoghan', 'Sulaymaniyah, Qaratoghan'), ('Raparin', 'Sulaymaniyah, Raparin'), ('Reaaya', 'Sulaymaniyah, Reaaya'), ('Rzgary', 'Sulaymaniyah, Rzgary'), ('Sarchnar', 'Sulaymaniyah, Sarchnar'), ('Sarwary', 'Sulaymaniyah, Sarwary'), ('Shahidany Sarchnar', 'Sulaymaniyah, Shahidany Sarchnar'), ('Shahidany Zargata', 'Sulaymaniyah, Shahidany Zargata'), ('Shexan', 'Sulaymaniyah, Shexan'), ('Silemani Nwe', 'Sulaymaniyah, Silemani Nwe'), ('Sitak', 'Sulaymaniyah, Sitak'), ('Tafan', 'Sulaymaniyah, Tafan'), ('Tasluja', 'Sulaymaniyah, Tasluja'), ('Tavga', 'Sulaymaniyah, Tavga'), ('Tavga', 'Sulaymaniyah, Tavga'), ('Twy malik', 'Sulaymaniyah, Twy malik'), ('Zanko', 'Sulaymaniyah, Zanko'), ('Zargata', 'Sulaymaniyah, Zargata'), ('Zerinok', 'Sulaymaniyah, Zerinok'), ('baxtyari', 'Sulaymaniyah, baxtyari'), ('hawary taza', 'Sulaymaniyah, hawary taza'), ('ibrahym ahmed', 'Sulaymaniyah, ibrahym ahmed'), ('kany ba', 'Sulaymaniyah, kany ba'), ('kany sard', 'Sulaymaniyah, kany sard'), ('kurdsat', 'Sulaymaniyah, kurdsat'), ('sarshaqam', 'Sulaymaniyah, sarshaqam'), ('shakraka', 'Sulaymaniyah, shakraka')
    ]

  PROJECTS = [
    ('92 Towers', 'Erbil, 92 Towers'), ('American Village', 'Erbil, American Village'), ('Aram Village 1', 'Erbil, Aram Village 1'), ('Aram Village 2', 'Erbil, Aram Village 2'), ('Ashti City 2', 'Erbil, Ashti City 2'), ('Asuda City', 'Erbil, Asuda City'), ('Bafrin City', 'Erbil, Bafrin City'), ('Bakhtyari Twin Towers', 'Erbil, Bakhtyari Twin Towers'), ('Cavalli Tower', 'Erbil, Cavalli Tower'), ('Cihan City', 'Erbil, Cihan City'), ('Darwazay Hawler', 'Erbil, Darwazay Hawler'), ('Davos City', 'Erbil, Davos City'), ('Diplomati Safiran', 'Erbil, Diplomati Safiran'), ('Dream City', 'Erbil, Dream City'), ('Dubai City', 'Erbil, Dubai City'), ('Empire World', 'Erbil, Empire World'), ('English Tower', 'Erbil, English Tower'), ('English Village', 'Erbil, English Village'), ('Eskan Tower', 'Erbil, Eskan Tower'), ('FM Plaza', 'Erbil, FM Plaza'), ('Family Land', 'Erbil, Family Land'), ('Firdaws City', 'Erbil, Firdaws City'), ('Floria City', 'Erbil, Floria City'), ('Four Season Park', 'Erbil, Four Season Park'), ('Four Towers', 'Erbil, Four Towers'), ('Future City', 'Erbil, Future City'), ('Ganjan City', 'Erbil, Ganjan City'), ('Ganjan Life', 'Erbil, Ganjan Life'), ('Global city', 'Erbil, Global city'), ('Golden tower', 'Erbil, Golden tower'), ('Green Land', 'Erbil, Green Land'), ('Green World', 'Erbil, Green World'), ('Gullan Tower', 'Erbil, Gullan Tower'), ('Hana City', 'Erbil, Hana City'), ('Harsham city 1', 'Erbil, Harsham city 1'), ('Hiwa City', 'Erbil, Hiwa City'), ('Italian City 1', 'Erbil, Italian City 1'), ('Italian City 2', 'Erbil, Italian City 2'), ('Kurdistan City', 'Erbil, Kurdistan City'), ('Lalav Airport View', 'Erbil, Lalav Airport View'), ('Lalav City View', 'Erbil, Lalav City View'), ('Lalav city', 'Erbil, Lalav city'), ('Lalav sky view', 'Erbil, Lalav sky view'), ('Lana City', 'Erbil, Lana City'), ('Lawan city', 'Erbil, Lawan city'), ('Lebanese Village', 'Erbil, Lebanese Village'), ('Life Tower', 'Erbil, Life Tower'), ('Light City', 'Erbil, Light City'), ('MNW Towers', 'Erbil, MNW Towers'), ('MRF Towers', 'Erbil, MRF Towers'), ('Majidi View', 'Erbil, Majidi View'), ('Mamostayan City', 'Erbil, Mamostayan City'), ('Mass City', 'Erbil, Mass City'), ('Mass Hills', 'Erbil, Mass Hills'), ('Mass Village', 'Erbil, Mass Village'), ('Mini Slava', 'Erbil, Mini Slava'), ('Mnara Village', 'Erbil, Mnara Village'), ('Mountain View', 'Erbil, Mountain View'), ('Nawroz City', 'Erbil, Nawroz City'), ('Naz City', 'Erbil, Naz City'), ('New Azadi', 'Erbil, New Azadi'), ('New Eskan', 'Erbil, New Eskan'), ('Noble City', 'Erbil, Noble City'), ('North Holland', 'Erbil, North Holland'), ('One Tower Zanyari', 'Erbil, One Tower Zanyari'), ('Pank city', 'Erbil, Pank city'), ('Park View', 'Erbil, Park View'), ('Parosh Tower', 'Erbil, Parosh Tower'), ('Pavilion', 'Erbil, Pavilion'), ('Peshang Towers', 'Erbil, Peshang Towers'), ('Phoenix Tower', 'Erbil, Phoenix Tower'), ('Plus Life', 'Erbil, Plus Life'), ('Qaiwan Mirador', 'Erbil, Qaiwan Mirador'), ('Quattro Towers', 'Erbil, Quattro Towers'), ('Queen Towers', 'Erbil, Queen Towers'), ('Rami Towers', 'Erbil, Rami Towers'), ('Remas City', 'Erbil, Remas City'), ('Rona Tower', 'Erbil, Rona Tower'), ('Rona towers', 'Erbil, Rona towers'), ('Rose Tower', 'Erbil, Rose Tower'), ('Roya Towers', 'Erbil, Roya Towers'), ('Ruby Towers', 'Erbil, Ruby Towers'), ('Safiran City', 'Erbil, Safiran City'), ('Sky towers', 'Erbil, Sky towers'), ('Slava City', 'Erbil, Slava City'), ('Spanish Village', 'Erbil, Spanish Village'), ('Star towers', 'Erbil, Star towers'), ('Talar City', 'Erbil, Talar City'), ('The Atlantic', 'Erbil, The Atlantic'), ('The Boulevard', 'Erbil, The Boulevard'), ('True Star', 'Erbil, True Star'), ('Var Park', 'Erbil, Var Park'), ('Voyage Mall', 'Erbil, Voyage Mall'), ('Wavey avenue', 'Erbil, Wavey avenue'), ('Z Center Towers', 'Erbil, Z Center Towers'), ('Zaner City', 'Erbil, Zaner City'), ('Zanko Village', 'Erbil, Zanko Village'), ('Zanyari Towers', 'Erbil, Zanyari Towers'), ('Zaytoon Plus City', 'Erbil, Zaytoon Plus City'), ('Zerin City', 'Erbil, Zerin City'), ('Zilan City', 'Erbil, Zilan City'), ('Zin city', 'Erbil, Zin city'), ('sun towers', 'Erbil, sun towers'), ('varsan project', 'Erbil, varsan project'), ('white towers', 'Erbil, white towers'), ('Aram City', 'Sulaymaniyah, Aram City'), ('Asoy Gash', 'Sulaymaniyah, Asoy Gash'), ('Ban City', 'Sulaymaniyah, Ban City'), ('Chawy Slemany', 'Sulaymaniyah, Chawy Slemany'), ('City Towers', 'Sulaymaniyah, City Towers'), ('Dania City', 'Sulaymaniyah, Dania City'), ('Darwaza City', 'Sulaymaniyah, Darwaza City'), ('Empire towers', 'Sulaymaniyah, Empire towers'), ('Garden City', 'Sulaymaniyah, Garden City'), ('Goizha City', 'Sulaymaniyah, Goizha City'), ('Grand Boulevard', 'Sulaymaniyah, Grand Boulevard'), ('Gundy Almany', 'Sulaymaniyah, Gundy Almany'), ('Miran City', 'Sulaymaniyah, Miran City'), ('Nali City', 'Sulaymaniyah, Nali City'), ('Pak City', 'Sulaymaniyah, Pak City'), ('Park 77', 'Sulaymaniyah, Park 77'), ('Pasha city', 'Sulaymaniyah, Pasha city'), ('Qaiwan City', 'Sulaymaniyah, Qaiwan City'), ('Qaiwan height', 'Sulaymaniyah, Qaiwan height'), ('Saeb City', 'Sulaymaniyah, Saeb City'), ('Shary Daik', 'Sulaymaniyah, Shary Daik'), ('Shary Mamostayan', 'Sulaymaniyah, Shary Mamostayan'), ('Slemany height', 'Sulaymaniyah, Slemany height'), ('Titanic Towers', 'Sulaymaniyah, Titanic Towers'), ('Wais Tower', 'Sulaymaniyah, Wais Tower'), ('Kalekent Site', 'Turkey, Kalekent Site'), ('MSY Nefes', 'Turkey, MSY Nefes')
    ]

  PURPOSES = [
    ("Sale", "Sale"),
    ("Rent", "Rent"),
    ("Commercial Sale", "Commercial Sale"),
    ("Commercial Rent", "Commercial Rent"),
  ]

  TYPES = [
    ("House", "House"),
    ("Villa", "Villa"),
    ("Apartment", "Apartment"),
    ("Commercial Apartment", "Commercial Apartment"),
    ("Office", "Office"),
    ("Land", "Land"),
    ("Residential Land", "Residential Land"),
    ("Shop", "Shop"),
    ("Market", "Market"),
    ("Building", "Building"),
    ("Farm", "Farm"),
    ("Medical Center", "Medical Center"),
    ("Restaurant", "Restaurant"),
    ("Hotel", "Hotel"),
  ]

  title = models.CharField(max_length=255)
  prop_slug = models.SlugField(unique=True, db_index=True, null=True)
  main_image = models.ImageField(upload_to="images", null=True)
  date = models.DateTimeField(auto_now_add=True)
  city = models.CharField(max_length=35, choices=CITIES)
  region = models.CharField(max_length=35, choices=REGIONS, null=True, blank=True)
  project = models.CharField(max_length=35, choices=PROJECTS, null=True, blank=True)
  price = models.CharField(max_length=10, null=True)
  purpose = models.CharField(max_length=35, choices=PURPOSES, default="Sale")
  type = models.CharField(max_length=35, choices=TYPES, default="House")
  area = models.IntegerField(null=True)
  reception_rooms = models.IntegerField(null=True, blank=True)
  kitchens = models.IntegerField(null=True, blank=True)
  bedrooms = models.IntegerField(null=True, blank=True)
  bathrooms = models.IntegerField(null=True, blank=True)
  garage = models.IntegerField(null=True, blank=True)
  balcony = models.IntegerField(null=True, blank=True)
  garden = models.BooleanField(default=False)
  furnishing = models.BooleanField(default=False)
  featured = models.BooleanField(default=False)


  def __str__(self) -> str:
    return self.title


class PropertyImage(models.Model):
  property = models.ForeignKey(Property, on_delete=models.CASCADE, related_name="image")
  image = models.ImageField(upload_to="images", null=True)

  def __str__(self) -> str:
    return f"{self.property.title} image"