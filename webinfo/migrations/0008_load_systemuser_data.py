# Generated by Django 3.2.5 on 2022-04-16 04: 55
from django.core.exceptions import ObjectDoesNotExist
from django.db import migrations

USERS = [
    {'first_name': 'Dar','last_name': 'Grinvalds','disambiguator': 'Training',},
    {'first_name': 'Abraham','last_name': 'Hatfull','disambiguator': '',},
    {'first_name': 'Milton','last_name': 'Harme','disambiguator': 'Accounting',},
    {'first_name': 'Hettie','last_name': 'Grove','disambiguator': '',},
    {'first_name': 'Fannie','last_name': 'Ranyell','disambiguator': '',},
    {'first_name': 'Camilla','last_name': 'Haseley','disambiguator': 'Legal',},
    {'first_name': 'Lavinie','last_name': 'Stimpson','disambiguator': '',},
    {'first_name': 'Raff','last_name': 'Matussov','disambiguator': '',},
    {'first_name': 'Walther','last_name': 'Antyshev','disambiguator': '',},
    {'first_name': 'Aeriell','last_name': 'Skule','disambiguator': '',},
    {'first_name': 'Karlotta','last_name': 'Hickenbottom','disambiguator': 'Human Resources',},
    {'first_name': 'Aigneis','last_name': 'Trevascus','disambiguator': 'Training',},
    {'first_name': 'Meggi','last_name': 'Dunkerton','disambiguator': 'Sales',},
    {'first_name': 'Alexei','last_name': 'Guirard','disambiguator': '',},
    {'first_name': 'Barron','last_name': 'Pigney','disambiguator': '',},
    {'first_name': 'Mair','last_name': 'Bickell','disambiguator': 'Legal',},
    {'first_name': 'Kaia','last_name': 'Bourtoumieux','disambiguator': '',},
    {'first_name': 'Wally','last_name': 'Bigg','disambiguator': '',},
    {'first_name': 'Rickie','last_name': 'Kaman','disambiguator': '',},
    {'first_name': 'Demetria','last_name': 'Gini','disambiguator': '',},
    {'first_name': 'Blaine','last_name': 'Esslement','disambiguator': '',},
    {'first_name': 'Andre','last_name': 'Jacobowits','disambiguator': '',},
    {'first_name': 'Thorn','last_name': 'Mapplethorpe','disambiguator': '',},
    {'first_name': 'Rosabella','last_name': 'Fillery','disambiguator': '',},
    {'first_name': 'Donella','last_name': 'Shakelady','disambiguator': 'Product Management',},
    {'first_name': 'Sholom','last_name': 'Aldus','disambiguator': '',},
    {'first_name': 'Viva','last_name': 'Corbet','disambiguator': 'Business Development',},
    {'first_name': 'Carmelina','last_name': 'Copperwaite','disambiguator': '',},
    {'first_name': 'Beck','last_name': 'Coggan','disambiguator': 'Product Management',},
    {'first_name': 'Carroll','last_name': 'Darey','disambiguator': '',},
    {'first_name': 'Horst','last_name': 'Sedworth','disambiguator': '',},
    {'first_name': 'Kelby','last_name': 'Joutapaitis','disambiguator': 'Research and Development',},
    {'first_name': 'Sonnie','last_name': 'Feares','disambiguator': '',},
    {'first_name': 'Freddy','last_name': 'Jeannesson','disambiguator': 'Marketing',},
    {'first_name': 'Isiahi','last_name': 'De la Eglise','disambiguator': '',},
    {'first_name': 'Franklin','last_name': 'Gavini','disambiguator': 'Sales',},
    {'first_name': 'Ali','last_name': 'Shanklin','disambiguator': 'Support',},
    {'first_name': 'Gardener','last_name': 'Campsall','disambiguator': 'Sales',},
    {'first_name': 'Lyn','last_name': 'Eldridge','disambiguator': 'Legal',},
    {'first_name': 'Gene','last_name': 'Haggis','disambiguator': '',},
    {'first_name': 'Ced','last_name': 'Gosland','disambiguator': '',},
    {'first_name': 'Wendall','last_name': 'Hartop','disambiguator': '',},
    {'first_name': 'Prent','last_name': 'Ygoe','disambiguator': 'Product Management',},
    {'first_name': 'Vina','last_name': 'Robelow','disambiguator': 'Sales',},
    {'first_name': 'Karalee','last_name': 'Semorad','disambiguator': 'Sales',},
    {'first_name': 'Joanie','last_name': 'Reinbach','disambiguator': '',},
    {'first_name': 'Janelle','last_name': 'Tuffin','disambiguator': '',},
    {'first_name': 'Aubrey','last_name': 'Ruby','disambiguator': 'Marketing',},
    {'first_name': 'Quinta','last_name': 'Zamora','disambiguator': '',},
    {'first_name': 'Birgitta','last_name': 'Sarson','disambiguator': 'Research and Development',},
    {'first_name': 'Pancho','last_name': 'Bauld','disambiguator': '',},
    {'first_name': 'Staford','last_name': 'MacDearmaid','disambiguator': '',},
    {'first_name': 'Marvin','last_name': 'Crummy','disambiguator': '',},
    {'first_name': 'Rebecka','last_name': 'Stobo','disambiguator': 'Legal',},
    {'first_name': 'Wallace','last_name': 'Gillise','disambiguator': 'Product Management',},
    {'first_name': 'Harp','last_name': 'Widger','disambiguator': '',},
    {'first_name': 'Shawnee','last_name': 'Goaley','disambiguator': '',},
    {'first_name': 'Gwenora','last_name': 'Copyn','disambiguator': 'Research and Development',},
    {'first_name': 'George','last_name': 'Feld','disambiguator': '',},
    {'first_name': 'Fin','last_name': 'Falshaw','disambiguator': 'Training',},
    {'first_name': 'Emmaline','last_name': 'Bramo','disambiguator': '',},
    {'first_name': 'Abby','last_name': 'Ruane','disambiguator': 'Services',},
    {'first_name': 'Heywood','last_name': 'Mauchlen','disambiguator': '',},
    {'first_name': 'Lanni','last_name': 'Segges','disambiguator': '',},
    {'first_name': 'Branden','last_name': 'Deeming','disambiguator': 'Accounting',},
    {'first_name': 'Boony','last_name': 'Grzelczyk','disambiguator': '',},
    {'first_name': 'Teresina','last_name': 'Matura','disambiguator': '',},
    {'first_name': 'Aloise','last_name': 'Huggill','disambiguator': '',},
    {'first_name': 'Terrill','last_name': 'Danser','disambiguator': '',},
    {'first_name': 'Alene','last_name': 'Greenroa','disambiguator': '',},
    {'first_name': 'Oralie','last_name': 'Aitkenhead','disambiguator': '',},
    {'first_name': 'Saree','last_name': 'Edgley','disambiguator': '',},
    {'first_name': 'Damaris','last_name': 'Attrey','disambiguator': '',},
    {'first_name': 'Lara','last_name': 'Stannis','disambiguator': '',},
    {'first_name': 'Gunther','last_name': 'De Bischop','disambiguator': '',},
    {'first_name': 'Kip','last_name': 'Sedgwick','disambiguator': '',},
    {'first_name': 'Liv','last_name': 'Kitlee','disambiguator': '',},
    {'first_name': 'Grazia','last_name': 'Howkins','disambiguator': '',},
    {'first_name': 'Charo','last_name': 'Verillo','disambiguator': 'Marketing',},
    {'first_name': 'Gordon','last_name': 'Grafom','disambiguator': '',},
    {'first_name': 'Oberon','last_name': 'Marsters','disambiguator': 'Accounting',},
    {'first_name': 'Jenni','last_name': 'Minall','disambiguator': '',},
    {'first_name': 'Brandyn','last_name': 'Kettlesing','disambiguator': '',},
    {'first_name': 'Mace','last_name': 'Edds','disambiguator': '',},
    {'first_name': 'Saunders','last_name': 'Puttan','disambiguator': 'Business Development',},
    {'first_name': 'Bobby','last_name': 'Miller','disambiguator': 'Engineering',},
    {'first_name': 'Katleen','last_name': 'Allone','disambiguator': '',},
    {'first_name': 'Revkah','last_name': 'MacHostie','disambiguator': '',},
    {'first_name': 'Carolina','last_name': 'Kedward','disambiguator': '',},
    {'first_name': 'Dwight','last_name': 'Connow','disambiguator': 'Human Resources',},
    {'first_name': 'Hadley','last_name': 'O Haire','disambiguator': '',},
    {'first_name': 'Devlen','last_name': 'Blackborne','disambiguator': '',},
    {'first_name': 'Newton','last_name': 'Grund','disambiguator': 'Engineering',},
    {'first_name': 'Tristan','last_name': 'Gamage','disambiguator': '',},
    {'first_name': 'Dorian','last_name': 'Overshott','disambiguator': 'Training',},
    {'first_name': 'Norry','last_name': 'Andreazzi','disambiguator': 'Business Development',},
    {'first_name': 'Essa','last_name': 'Nuzzi','disambiguator': '',},
    {'first_name': 'Michal','last_name': 'Skeat','disambiguator': 'Accounting',},
    {'first_name': 'Edgar','last_name': 'McClory','disambiguator': 'Accounting',},
    {'first_name': 'Roxanna','last_name': 'Bolsteridge','disambiguator': 'Services',},
    {'first_name': 'Gwenny','last_name': 'Robet','disambiguator': '',},
    {'first_name': 'Freedman','last_name': 'Trengrove','disambiguator': '',},
    {'first_name': 'Nappy','last_name': 'Haslewood','disambiguator': '',},
    {'first_name': 'Melisandra','last_name': 'Heinig','disambiguator': '',},
    {'first_name': 'Syd','last_name': 'MacAndie','disambiguator': '',},
    {'first_name': 'Bret','last_name': 'McKelvey','disambiguator': 'Research and Development',},
    {'first_name': 'Tadio','last_name': 'Blazewicz','disambiguator': 'Business Development',},
    {'first_name': 'Jaime','last_name': 'O Collopy','disambiguator': '',},
    {'first_name': 'Gillian','last_name': 'Cullity','disambiguator': '',},
    {'first_name': 'Nolly','last_name': 'Bowton','disambiguator': '',},
    {'first_name': 'Crystie','last_name': 'Ching','disambiguator': '',},
    {'first_name': 'Dana','last_name': 'Crocombe','disambiguator': 'Support',},
    {'first_name': 'Kerrie','last_name': 'Karolowski','disambiguator': 'Sales',},
    {'first_name': 'Dee dee','last_name': 'Helliar','disambiguator': '',},
    {'first_name': 'Suzanne','last_name': 'Denisard','disambiguator': '',},
    {'first_name': 'Niles','last_name': 'Cosley','disambiguator': 'Sales',},
    {'first_name': 'Rutledge','last_name': 'Garett','disambiguator': '',},
    {'first_name': 'Kirby','last_name': 'Muneely','disambiguator': 'Support',},
    {'first_name': 'Donnie','last_name': 'Usborn','disambiguator': '',},
    {'first_name': 'Susannah','last_name': 'Kivlehan','disambiguator': '',},
    {'first_name': 'Lavinia','last_name': 'Beldam','disambiguator': 'Product Management',},
    {'first_name': 'Fair','last_name': 'Bodechon','disambiguator': '',},
    {'first_name': 'Leanora','last_name': 'Wallsworth','disambiguator': '',},
    {'first_name': 'Jackie','last_name': 'Yakobowitz','disambiguator': 'Research and Development',},
    {'first_name': 'Cecilla','last_name': 'Derell','disambiguator': '',},
    {'first_name': 'Pippa','last_name': 'Martusov','disambiguator': '',},
    {'first_name': 'Roselle','last_name': 'Lideard','disambiguator': '',},
    {'first_name': 'Mitchel','last_name': 'Krinks','disambiguator': '',},
    {'first_name': 'Dyanne','last_name': 'Jouannot','disambiguator': '',},
    {'first_name': 'Nyssa','last_name': 'Yersin','disambiguator': '',},
    {'first_name': 'Maggy','last_name': 'Dable','disambiguator': '',},
    {'first_name': 'Lorrie','last_name': 'Janisson','disambiguator': '',},
    {'first_name': 'Tersina','last_name': 'Sams','disambiguator': 'Sales',},
    {'first_name': 'Bearnard','last_name': 'Rosbotham','disambiguator': '',},
    {'first_name': 'Carleen','last_name': 'Bartleman','disambiguator': 'Training',},
    {'first_name': 'Arvy','last_name': 'Station','disambiguator': 'Research and Development',},
    {'first_name': 'Jaclyn','last_name': 'Vittle','disambiguator': '',},
    {'first_name': 'Shellysheldon','last_name': 'Studman','disambiguator': 'Business Development',},
    {'first_name': 'Huntley','last_name': 'Linde','disambiguator': '',},
    {'first_name': 'Ive','last_name': 'Heintze','disambiguator': '',},
    {'first_name': 'Galen','last_name': 'Lochhead','disambiguator': '',},
    {'first_name': 'Osborn','last_name': 'Fomichkin','disambiguator': 'Product Management',},
    {'first_name': 'Malia','last_name': 'Lambourne','disambiguator': '',},
    {'first_name': 'Ethan','last_name': 'Okroy','disambiguator': '',},
    {'first_name': 'Quentin','last_name': 'Vasiliev','disambiguator': '',},
    {'first_name': 'Paulie','last_name': 'Lindell','disambiguator': '',},
    {'first_name': 'Jeanne','last_name': 'Cufley','disambiguator': '',},
    {'first_name': 'Marne','last_name': 'Sturm','disambiguator': '',},
    {'first_name': 'Daisy','last_name': 'Duggon','disambiguator': '',},
    {'first_name': 'Moe','last_name': 'Bachelor','disambiguator': '',},
    {'first_name': 'Veda','last_name': 'Marsy','disambiguator': '',},
    {'first_name': 'Abbye','last_name': 'Scoggans','disambiguator': '',},
    {'first_name': 'Kennith','last_name': 'Beirne','disambiguator': 'Human Resources',},
    {'first_name': 'Wilden','last_name': 'Sarjeant','disambiguator': 'Legal',},
    {'first_name': 'Odilia','last_name': 'Caveill','disambiguator': 'Sales',},
    {'first_name': 'Sarajane','last_name': 'Cure','disambiguator': '',},
    {'first_name': 'Nanine','last_name': 'Sille','disambiguator': 'Services',},
    {'first_name': 'Welch','last_name': 'Boch','disambiguator': 'Sales',},
    {'first_name': 'Ekaterina','last_name': 'Wais','disambiguator': '',},
    {'first_name': 'Sybil','last_name': 'Stichall','disambiguator': 'Services',},
    {'first_name': 'Gilly','last_name': 'Bridgens','disambiguator': '',},
    {'first_name': 'Milo','last_name': 'Dominguez','disambiguator': '',},
    {'first_name': 'Heriberto','last_name': 'Vogele','disambiguator': '',},
    {'first_name': 'Janelle','last_name': 'Langthorne','disambiguator': 'Research and Development',},
    {'first_name': 'Cristie','last_name': 'Dunmuir','disambiguator': '',},
    {'first_name': 'Skyler','last_name': 'Maurice','disambiguator': '',},
    {'first_name': 'Derk','last_name': 'Seczyk','disambiguator': 'Support',},
    {'first_name': 'Bren','last_name': 'Rounsefell','disambiguator': 'Services',},
    {'first_name': 'Nara','last_name': 'Edmed','disambiguator': 'Training',},
    {'first_name': 'Ettore','last_name': 'Leith','disambiguator': '',},
    {'first_name': 'Cyrillus','last_name': 'Rosenkranc','disambiguator': 'Accounting',},
    {'first_name': 'Terese','last_name': 'Dormand','disambiguator': '',},
    {'first_name': 'Avrit','last_name': 'Georg','disambiguator': 'Support',},
    {'first_name': 'Merry','last_name': 'Eye','disambiguator': 'Product Management',},
    {'first_name': 'Al','last_name': 'Caras','disambiguator': '',},
    {'first_name': 'Tynan','last_name': 'MacCague','disambiguator': 'Accounting',},
    {'first_name': 'Evvy','last_name': 'Kulic','disambiguator': 'Training',},
    {'first_name': 'Cedric','last_name': 'Pointer','disambiguator': 'Services',},
    {'first_name': 'Nickey','last_name': 'Humbey','disambiguator': '',},
    {'first_name': 'Eleonora','last_name': 'Ridesdale','disambiguator': 'Accounting',},
    {'first_name': 'Michaela','last_name': 'Beccles','disambiguator': '',},
    {'first_name': 'Etheline','last_name': 'Hanhardt','disambiguator': 'Sales',},
    {'first_name': 'Cilka','last_name': 'Dowdle','disambiguator': '',},
    {'first_name': 'Hanson','last_name': 'Cherm','disambiguator': 'Engineering',},
    {'first_name': 'Roley','last_name': 'Philbrick','disambiguator': '',},
    {'first_name': 'Teddie','last_name': 'Corking','disambiguator': '',},
    {'first_name': 'Lefty','last_name': 'Bon','disambiguator': '',},
    {'first_name': 'Eldin','last_name': 'O Cridigan','disambiguator': '',},
    {'first_name': 'Hermia','last_name': 'Whatsize','disambiguator': '',},
    {'first_name': 'Margeaux','last_name': 'Hubbucks','disambiguator': 'Legal',},
    {'first_name': 'Brod','last_name': 'Stidston','disambiguator': '',},
    {'first_name': 'Kaspar','last_name': 'Baldick','disambiguator': 'Sales',},
    {'first_name': 'Ulises','last_name': 'O Fergus','disambiguator': 'Services',},
    {'first_name': 'Corrine','last_name': 'Meachem','disambiguator': 'Services',},
    {'first_name': 'Carmon','last_name': 'Stallworth','disambiguator': '',},
    {'first_name': 'Edwin','last_name': 'Meriguet','disambiguator': 'Accounting',},
    {'first_name': 'Amber','last_name': 'Jukubczak','disambiguator': '',},
    {'first_name': 'Sophronia','last_name': 'Coat','disambiguator': '',},
    {'first_name': 'Piggy','last_name': 'Butting','disambiguator': 'Support',},
    {'first_name': 'Edee','last_name': 'Dodamead','disambiguator': 'Training',},
    {'first_name': 'Augustine','last_name': 'Headech','disambiguator': '',},
    {'first_name': 'Thornton','last_name': 'Spofford','disambiguator': '',},
    {'first_name': 'Craig','last_name': 'Bullivent','disambiguator': '',},
    {'first_name': 'Annora','last_name': 'Dishmon','disambiguator': 'Business Development',},
    {'first_name': 'Ludovika','last_name': 'Coan','disambiguator': '',},
    {'first_name': 'Lynett','last_name': 'Treagust','disambiguator': '',},
    {'first_name': 'Ignazio','last_name': 'Askew','disambiguator': '',},
    {'first_name': 'Matilde','last_name': 'Mullane','disambiguator': '',},
    {'first_name': 'Lynett','last_name': 'Richardeau','disambiguator': 'Services',},
    {'first_name': 'Fania','last_name': 'Davidwitz','disambiguator': 'Business Development',},
    {'first_name': 'Addie','last_name': 'Kindley','disambiguator': '',},
    {'first_name': 'Nerte','last_name': 'Allabarton','disambiguator': 'Accounting',},
    {'first_name': 'Victoir','last_name': 'Glowacki','disambiguator': 'Services',},
    {'first_name': 'Zarla','last_name': 'Rosingdall','disambiguator': 'Research and Development',},
    {'first_name': 'Karolina','last_name': 'Dallinder','disambiguator': '',},
    {'first_name': 'Marin','last_name': 'Lenthall','disambiguator': '',},
    {'first_name': 'Iorgo','last_name': 'Frail','disambiguator': 'Accounting',},
    {'first_name': 'Nikoletta','last_name': 'Leades','disambiguator': 'Research and Development',},
    {'first_name': 'Christi','last_name': 'Whitworth','disambiguator': 'Training',},
    {'first_name': 'Deana','last_name': 'Albrooke','disambiguator': 'Product Management',},
    {'first_name': 'Julieta','last_name': 'Dunwoody','disambiguator': '',},
    {'first_name': 'Obadias','last_name': 'Purslow','disambiguator': 'Training',},
    {'first_name': 'Reinhold','last_name': 'Sabin','disambiguator': '',},
    {'first_name': 'Jeanie','last_name': 'Rozea','disambiguator': '',},
    {'first_name': 'Davis','last_name': 'Pimmocke','disambiguator': 'Business Development',},
    {'first_name': 'Maible','last_name': 'Clementel','disambiguator': '',},
    {'first_name': 'Terri','last_name': 'Kristoffersson','disambiguator': '',},
    {'first_name': 'Jenn','last_name': 'Erbe','disambiguator': '',},
    {'first_name': 'Edlin','last_name': 'Lawler','disambiguator': 'Business Development',},
    {'first_name': 'Duff','last_name': 'Meneo','disambiguator': '',},
    {'first_name': 'Maddi','last_name': 'Calwell','disambiguator': '',},
    {'first_name': 'Delilah','last_name': 'Stubbins','disambiguator': 'Support',},
    {'first_name': 'Melita','last_name': 'Copin','disambiguator': '',},
    {'first_name': 'Killy','last_name': 'Nancekivell','disambiguator': 'Accounting',},
    {'first_name': 'Vail','last_name': 'Basillon','disambiguator': 'Human Resources',},
    {'first_name': 'Augustine','last_name': 'Lilly','disambiguator': '',},
    {'first_name': 'Winny','last_name': 'Flippelli','disambiguator': '',},
    {'first_name': 'Fallon','last_name': 'Oldacre','disambiguator': 'Training',},
    {'first_name': 'Darci','last_name': 'Stubbe','disambiguator': 'Marketing',},
    {'first_name': 'Cristian','last_name': 'Greenslade','disambiguator': '',},
    {'first_name': 'Pauly','last_name': 'Skahill','disambiguator': 'Engineering',},
    {'first_name': 'Franky','last_name': 'Amsberger','disambiguator': '',},
    {'first_name': 'Berry','last_name': 'Todarini','disambiguator': '',},
    {'first_name': 'Ruggiero','last_name': 'Snaddin','disambiguator': 'Sales',},
    {'first_name': 'Ealasaid','last_name': 'Dumbreck','disambiguator': '',},
    {'first_name': 'Stillmann','last_name': 'Hallows','disambiguator': '',},
    {'first_name': 'Larina','last_name': 'Skelly','disambiguator': '',},
    {'first_name': 'Heinrick','last_name': 'Featonby','disambiguator': '',},
    {'first_name': 'Etty','last_name': 'Heffernon','disambiguator': '',},
    {'first_name': 'Tab','last_name': 'Derges','disambiguator': 'Legal',},
    {'first_name': 'Nisse','last_name': 'Aleixo','disambiguator': '',},
    {'first_name': 'Rora','last_name': 'Pryn','disambiguator': '',},
    {'first_name': 'Desiri','last_name': 'Wimp','disambiguator': '',},
    {'first_name': 'Wynn','last_name': 'Krzyzanowski','disambiguator': '',},
    {'first_name': 'Chris','last_name': 'O Hanvey','disambiguator': '',},
    {'first_name': 'Vale','last_name': 'Pattisson','disambiguator': 'Support',},
    {'first_name': 'Glennie','last_name': 'Deetlefs','disambiguator': 'Training',},
    {'first_name': 'Trumaine','last_name': 'Shimuk','disambiguator': '',},
    {'first_name': 'Toddy','last_name': 'Leiden','disambiguator': '',},
    {'first_name': 'Willi','last_name': 'Norvill','disambiguator': 'Support',},
    {'first_name': 'Arliene','last_name': 'Furlong','disambiguator': '',},
    {'first_name': 'Cyndy','last_name': 'Itzcovichch','disambiguator': '',},
    {'first_name': 'Wendye','last_name': 'Bannon','disambiguator': '',},
    {'first_name': 'Oberon','last_name': 'Marchello','disambiguator': 'Support',},
    {'first_name': 'Birgitta','last_name': 'Aldwich','disambiguator': 'Research and Development',},
    {'first_name': 'Morie','last_name': 'Isaq','disambiguator': '',},
    {'first_name': 'Pattie','last_name': 'Beynke','disambiguator': 'Business Development',},
    {'first_name': 'Feliks','last_name': 'Gronaller','disambiguator': '',},
    {'first_name': 'Claudette','last_name': 'Deavall','disambiguator': 'Sales',},
    {'first_name': 'Kristofor','last_name': 'Gollin','disambiguator': '',},
    {'first_name': 'Bridget','last_name': 'McLay','disambiguator': 'Marketing',},
    {'first_name': 'Gabbie','last_name': 'Chennells','disambiguator': 'Marketing',},
    {'first_name': 'Batsheva','last_name': 'Boscott','disambiguator': 'Business Development',},
    {'first_name': 'Andre','last_name': 'Cruce','disambiguator': '',},
    {'first_name': 'Gabrila','last_name': 'Willimot','disambiguator': '',},
    {'first_name': 'Ive','last_name': 'Linsay','disambiguator': 'Research and Development',},
    {'first_name': 'Olivie','last_name': 'Mowlam','disambiguator': '',},
    {'first_name': 'Martainn','last_name': 'Coneau','disambiguator': 'Engineering',},
    {'first_name': 'Haily','last_name': 'Gerauld','disambiguator': '',},
    {'first_name': 'Doroteya','last_name': 'Lothean','disambiguator': 'Human Resources',},
    {'first_name': 'Antonietta','last_name': 'Howbrook','disambiguator': '',},
    {'first_name': 'Marya','last_name': 'Mance','disambiguator': '',},
    {'first_name': 'Cristal','last_name': 'Cready','disambiguator': 'Services',},
    {'first_name': 'Cynthia','last_name': 'Izard','disambiguator': '',},
    {'first_name': 'Minni','last_name': 'Menel','disambiguator': '',},
    {'first_name': 'Mia','last_name': 'Sainer','disambiguator': 'Accounting',},
    {'first_name': 'Kit','last_name': 'Follin','disambiguator': '',},
    {'first_name': 'Conrado','last_name': 'Vallance','disambiguator': 'Engineering',},
    {'first_name': 'Benedict','last_name': 'Sandwich','disambiguator': '',},
    {'first_name': 'Bernita','last_name': 'Titcumb','disambiguator': '',},
    {'first_name': 'Eveleen','last_name': 'Jenks','disambiguator': 'Support',},
    {'first_name': 'Kimberli','last_name': 'Chable','disambiguator': '',},
    {'first_name': 'Elaina','last_name': 'Brigstock','disambiguator': 'Support',},
    {'first_name': 'Loise','last_name': 'Waldren','disambiguator': 'Research and Development',},
    {'first_name': 'Diahann','last_name': 'Brough','disambiguator': 'Sales',},
    {'first_name': 'Letti','last_name': 'Plante','disambiguator': '',},
    {'first_name': 'Lilla','last_name': 'Cornilleau','disambiguator': 'Sales',},
    {'first_name': 'Nikos','last_name': 'Jeffray','disambiguator': 'Support',},
    {'first_name': 'Grace','last_name': 'Pennycook','disambiguator': '',},
    {'first_name': 'Felicia','last_name': 'Tulip','disambiguator': '',}
]


def add_user_data(apps, schema_editor): 
    user_class = apps.get_model('webinfo', 'systemuser')
    for user in USERS:
        try: 
            duplicate_object = user_class.objects.get(
                first_name=user['first_name'],
                last_name=user['last_name'],
                disambiguator=user['disambiguator']
            )
            print('Duplicate user entry not added to user table: ', user['first_name'], user['last_name'])
        except ObjectDoesNotExist: 
            user_object = user_class.objects.create(
                first_name=user['first_name'],
                last_name=user['last_name'],
                disambiguator=user['disambiguator']
            )


def remove_user_data(apps, schema_editor): 
    user_class = apps.get_model('webinfo', 'user')
    for user in USERS:
        user_object = user_class.objects.get(
            first_name=user['first_name'],
            last_name=user['last_name'],
            disambiguator=user['disambiguator']
        )
        user_object.delete()


class Migration(migrations.Migration): 

    dependencies = [
        ('webinfo', '0007_load_publisher_data'),
    ]

    operations = [
        migrations.RunPython(
            add_user_data,
            remove_user_data
        )
    ]
