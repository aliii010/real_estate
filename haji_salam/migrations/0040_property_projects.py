# Generated by Django 4.1.3 on 2023-09-12 20:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("haji_salam", "0039_alter_property_city_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="property",
            name="projects",
            field=models.CharField(
                choices=[
                    ("92 Towers", "Erbil, 92 Towers"),
                    ("American Village", "Erbil, American Village"),
                    ("Aram Village 1", "Erbil, Aram Village 1"),
                    ("Aram Village 2", "Erbil, Aram Village 2"),
                    ("Ashti City 2", "Erbil, Ashti City 2"),
                    ("Asuda City", "Erbil, Asuda City"),
                    ("Bafrin City", "Erbil, Bafrin City"),
                    ("Bakhtyari Twin Towers", "Erbil, Bakhtyari Twin Towers"),
                    ("Cavalli Tower", "Erbil, Cavalli Tower"),
                    ("Cihan City", "Erbil, Cihan City"),
                    ("Darwazay Hawler", "Erbil, Darwazay Hawler"),
                    ("Davos City", "Erbil, Davos City"),
                    ("Diplomati Safiran", "Erbil, Diplomati Safiran"),
                    ("Dream City", "Erbil, Dream City"),
                    ("Dubai City", "Erbil, Dubai City"),
                    ("Empire World", "Erbil, Empire World"),
                    ("English Tower", "Erbil, English Tower"),
                    ("English Village", "Erbil, English Village"),
                    ("Eskan Tower", "Erbil, Eskan Tower"),
                    ("FM Plaza", "Erbil, FM Plaza"),
                    ("Family Land", "Erbil, Family Land"),
                    ("Firdaws City", "Erbil, Firdaws City"),
                    ("Floria City", "Erbil, Floria City"),
                    ("Four Season Park", "Erbil, Four Season Park"),
                    ("Four Towers", "Erbil, Four Towers"),
                    ("Future City", "Erbil, Future City"),
                    ("Ganjan City", "Erbil, Ganjan City"),
                    ("Ganjan Life", "Erbil, Ganjan Life"),
                    ("Global city", "Erbil, Global city"),
                    ("Golden tower", "Erbil, Golden tower"),
                    ("Green Land", "Erbil, Green Land"),
                    ("Green World", "Erbil, Green World"),
                    ("Gullan Tower", "Erbil, Gullan Tower"),
                    ("Hana City", "Erbil, Hana City"),
                    ("Harsham city 1", "Erbil, Harsham city 1"),
                    ("Hiwa City", "Erbil, Hiwa City"),
                    ("Italian City 1", "Erbil, Italian City 1"),
                    ("Italian City 2", "Erbil, Italian City 2"),
                    ("Kurdistan City", "Erbil, Kurdistan City"),
                    ("Lalav Airport View", "Erbil, Lalav Airport View"),
                    ("Lalav City View", "Erbil, Lalav City View"),
                    ("Lalav city", "Erbil, Lalav city"),
                    ("Lalav sky view", "Erbil, Lalav sky view"),
                    ("Lana City", "Erbil, Lana City"),
                    ("Lawan city", "Erbil, Lawan city"),
                    ("Lebanese Village", "Erbil, Lebanese Village"),
                    ("Life Tower", "Erbil, Life Tower"),
                    ("Light City", "Erbil, Light City"),
                    ("MNW Towers", "Erbil, MNW Towers"),
                    ("MRF Towers", "Erbil, MRF Towers"),
                    ("Majidi View", "Erbil, Majidi View"),
                    ("Mamostayan City", "Erbil, Mamostayan City"),
                    ("Mass City", "Erbil, Mass City"),
                    ("Mass Hills", "Erbil, Mass Hills"),
                    ("Mass Village", "Erbil, Mass Village"),
                    ("Mini Slava", "Erbil, Mini Slava"),
                    ("Mnara Village", "Erbil, Mnara Village"),
                    ("Mountain View", "Erbil, Mountain View"),
                    ("Nawroz City", "Erbil, Nawroz City"),
                    ("Naz City", "Erbil, Naz City"),
                    ("New Azadi", "Erbil, New Azadi"),
                    ("New Eskan", "Erbil, New Eskan"),
                    ("Noble City", "Erbil, Noble City"),
                    ("North Holland", "Erbil, North Holland"),
                    ("One Tower Zanyari", "Erbil, One Tower Zanyari"),
                    ("Pank city", "Erbil, Pank city"),
                    ("Park View", "Erbil, Park View"),
                    ("Parosh Tower", "Erbil, Parosh Tower"),
                    ("Pavilion", "Erbil, Pavilion"),
                    ("Peshang Towers", "Erbil, Peshang Towers"),
                    ("Phoenix Tower", "Erbil, Phoenix Tower"),
                    ("Plus Life", "Erbil, Plus Life"),
                    ("Qaiwan Mirador", "Erbil, Qaiwan Mirador"),
                    ("Quattro Towers", "Erbil, Quattro Towers"),
                    ("Queen Towers", "Erbil, Queen Towers"),
                    ("Rami Towers", "Erbil, Rami Towers"),
                    ("Remas City", "Erbil, Remas City"),
                    ("Rona Tower", "Erbil, Rona Tower"),
                    ("Rona towers", "Erbil, Rona towers"),
                    ("Rose Tower", "Erbil, Rose Tower"),
                    ("Roya Towers", "Erbil, Roya Towers"),
                    ("Ruby Towers", "Erbil, Ruby Towers"),
                    ("Safiran City", "Erbil, Safiran City"),
                    ("Sky towers", "Erbil, Sky towers"),
                    ("Slava City", "Erbil, Slava City"),
                    ("Spanish Village", "Erbil, Spanish Village"),
                    ("Star towers", "Erbil, Star towers"),
                    ("Talar City", "Erbil, Talar City"),
                    ("The Atlantic", "Erbil, The Atlantic"),
                    ("The Boulevard", "Erbil, The Boulevard"),
                    ("True Star", "Erbil, True Star"),
                    ("Var Park", "Erbil, Var Park"),
                    ("Voyage Mall", "Erbil, Voyage Mall"),
                    ("Wavey avenue", "Erbil, Wavey avenue"),
                    ("Z Center Towers", "Erbil, Z Center Towers"),
                    ("Zaner City", "Erbil, Zaner City"),
                    ("Zanko Village", "Erbil, Zanko Village"),
                    ("Zanyari Towers", "Erbil, Zanyari Towers"),
                    ("Zaytoon Plus City", "Erbil, Zaytoon Plus City"),
                    ("Zerin City", "Erbil, Zerin City"),
                    ("Zilan City", "Erbil, Zilan City"),
                    ("Zin city", "Erbil, Zin city"),
                    ("sun towers", "Erbil, sun towers"),
                    ("varsan project", "Erbil, varsan project"),
                    ("white towers", "Erbil, white towers"),
                    ("Aram City", "Sulaymaniyah, Aram City"),
                    ("Asoy Gash", "Sulaymaniyah, Asoy Gash"),
                    ("Ban City", "Sulaymaniyah, Ban City"),
                    ("Chawy Slemany", "Sulaymaniyah, Chawy Slemany"),
                    ("City Towers", "Sulaymaniyah, City Towers"),
                    ("Dania City", "Sulaymaniyah, Dania City"),
                    ("Darwaza City", "Sulaymaniyah, Darwaza City"),
                    ("Empire towers", "Sulaymaniyah, Empire towers"),
                    ("Garden City", "Sulaymaniyah, Garden City"),
                    ("Goizha City", "Sulaymaniyah, Goizha City"),
                    ("Grand Boulevard", "Sulaymaniyah, Grand Boulevard"),
                    ("Gundy Almany", "Sulaymaniyah, Gundy Almany"),
                    ("Miran City", "Sulaymaniyah, Miran City"),
                    ("Nali City", "Sulaymaniyah, Nali City"),
                    ("Pak City", "Sulaymaniyah, Pak City"),
                    ("Park 77", "Sulaymaniyah, Park 77"),
                    ("Pasha city", "Sulaymaniyah, Pasha city"),
                    ("Qaiwan City", "Sulaymaniyah, Qaiwan City"),
                    ("Qaiwan height", "Sulaymaniyah, Qaiwan height"),
                    ("Saeb City", "Sulaymaniyah, Saeb City"),
                    ("Shary Daik", "Sulaymaniyah, Shary Daik"),
                    ("Shary Mamostayan", "Sulaymaniyah, Shary Mamostayan"),
                    ("Slemany height", "Sulaymaniyah, Slemany height"),
                    ("Titanic Towers", "Sulaymaniyah, Titanic Towers"),
                    ("Wais Tower", "Sulaymaniyah, Wais Tower"),
                    ("Kalekent Site", "Turkey, Kalekent Site"),
                    ("MSY Nefes", "Turkey, MSY Nefes"),
                ],
                max_length=35,
                null=True,
            ),
        ),
    ]
