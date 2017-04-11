import boto3

dynamodb_client = boto3.client('dynamodb', region_name='us-west-2')


def lambda_handler(event, context):
    dynamodb_table = event['dynamodb_table']
    planets = get_targets()

    for planet in planets:
        dynamodb_client.put_item(
            TableName=dynamodb_table,
            Item={
                    'id': {
                        'S': str(planet['id'])
                     },
                     'planetName': {
                        'S': planet['planetName']
                     },
                     'militaryTarget': {
                        'BOOL': planet['militaryTarget']
                     },
                     'planetDesc': {
                        'S': planet['planetDesc']
                     },
                     'region': {
                        'S': planet['region']
                     }
            })


def get_targets():
    return [{
               "id": 56,
               "planetName": "Trandosha",
               "militaryTarget": True,
               "planetDesc": "Homeworld of the Trandoshan hunters. Close to Kashyyyk.",
               "region": "Mid Rim"
             },
             {
               "id": 31,
               "planetName": "Rishi",
               "militaryTarget": False,
               "planetDesc": "Tropical planet used by the Republic to monitor the nearby cloning facility on Kamino.",
               "region": "Outer Rim"
             },
             {
               "id": 9,
               "planetName": "Ilum",
               "militaryTarget": True,
               "planetDesc": "Remote ice planet where the crystals that focus lightsabers are mined.",
               "region": "Unknown"
             },
             {
               "id": 13,
               "planetName": "Ryloth",
               "militaryTarget": False,
               "planetDesc": "Dry and Hot home planet of Oola and other Twi'leks.",
               "region": "Outer Rim"
             },
             {
               "id": 86,
               "planetName": "Iridonia",
               "militaryTarget": False,
               "planetDesc": "Rumored birthplace of Darth Maul.",
               "region": "Mid Rim"
             },
             {
               "id": 72,
               "planetName": "Cato Neimoidia",
               "militaryTarget": False,
               "planetDesc": "The site of battles throughout the Clone Wars and is notable for its 'Bridge Cities.' Also the site of Plo Koon's death during the Jedi Purge.",
               "region": "Colonies"
             },
             {
               "id": 93,
               "planetName": "Coruscant",
               "militaryTarget": False,
               "planetDesc": "Urban world consists of a planet - wide city. Governmental center of the Galactic Republic and later the Galactic Empire.",
               "region": "Core Worlds"
             },
             {
               "id": 45,
               "planetName": "Bespin",
               "militaryTarget": False,
               "planetDesc": "Gas planet and the location of Cloud City.",
               "region": "Outer Rim"
             },
             {
               "id": 17,
               "planetName": "Alderaan",
               "militaryTarget": False,
               "planetDesc": "Home planet of Princess Leia and Bail Organa. Destroyed by the first Death Star as a demonstration of power.",
               "region": "Core Worlds"
             },
             {
               "id": 50,
               "planetName": "Kessel",
               "militaryTarget": True,
               "planetDesc": "A mining planet which has been fought over by crime lords for its valuable Spice.",
               "region": "Outer Rim"
             },
             {
               "id": 71,
               "planetName": "Rodia",
               "militaryTarget": False,
               "planetDesc": "Home planet of Greedo and other Rodians.",
               "region": "Outer Rim"
             },
             {
               "id": 19,
               "planetName": "Geonosis",
               "militaryTarget": False,
               "planetDesc": "Rocky desert planet where battle droids are manufactured, and the site of the opening battle of the Clone Wars. All life on the planet is presumed destroyed by the Empire in Star Wars Rebels. Close to Tatooine.",
               "region": "Outer Rim"
             },
             {
               "id": 49,
               "planetName": "Jakku",
               "militaryTarget": False,
               "planetDesc": "Desert planet. Site of a 'graveyard' of ships damaged during the final battle between the Rebel Alliance and the Empire.",
               "region": "Inner Rim"
             },
             {
               "id": 92,
               "planetName": "Devaron",
               "militaryTarget": False,
               "planetDesc": "Forest planet with an ancient Jedi Temple.",
               "region": "Colonies"
             },
             {
               "id": 64,
               "planetName": "Jedha",
               "militaryTarget": True,
               "planetDesc": "Cold desert moon, and a sacred place for believers in The Force. Source of kyber crystals used to power lightsabers and the Death Star's primary weapon.",
               "region": "Mid Rim"
             },
             {
               "id": 29,
               "planetName": "Lah'mu",
               "militaryTarget": False,
               "planetDesc": "A remote planet with black sands where Jyn Erso and her parents go into hiding.",
               "region": "Outer Rim"
             },
             {
               "id": 23,
               "planetName": "Hoth",
               "militaryTarget": True,
               "planetDesc": "Desolate ice planet and base for the Rebel Alliance.",
               "region": "Outer Rim"
             },
             {
               "id": 11,
               "planetName": "Corellia",
               "militaryTarget": False,
               "planetDesc": "Homeworld of Han Solo. An industrial planet with a strong culture of training pilots.",
               "region": "Core Worlds"
             },
             {
               "id": 57,
               "planetName": "Dathomir",
               "militaryTarget": False,
               "planetDesc": "Han Solo  wins the planet in a card game and lures Princess Leia  there to stop her from marrying someone else, and Luke Skywalker discovers that the infamous Nightsisters live there.",
               "region": "Outer Rim"
             },
             {
               "id": 99,
               "planetName": "Dantooine",
               "militaryTarget": True,
               "planetDesc": "Rural planet and the former site of a Rebel base.",
               "region": "Outer Rim"
             }
            ]
