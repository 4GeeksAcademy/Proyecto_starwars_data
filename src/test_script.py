from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base, User, Character, Planet, Vehicle, CharacterFavorit, PlanetFavorit, VehicleFavorit

# Configura el motor de base de datos (SQLite en este caso)
engine = create_engine('sqlite:///starwars.db', echo=True)

# Crea todas las tablas en la base de datos
Base.metadata.create_all(engine)

# Configura una sesión para interactuar con la base de datos
Session = sessionmaker(bind=engine)
session = Session()

# --- PRUEBAS ---

# 1. Crear un usuario
user1 = User(email="luke@starwars.com", password="maytheforce")
session.add(user1)
session.commit()
print("Usuario creado:", user1.to_dict())

# 2. Añadir un personaje
character1 = Character(name="Luke Skywalker", hair_color="Blonde", eye_color="Blue", gender="Male", species="Human", height=172)
session.add(character1)
session.commit()
print("Personaje creado:", character1.to_dict())

# 3. Añadir un planeta
planet1 = Planet(name="Tatooine", terrain="Desert", population=200000, climate="Arid", gravity="1 standard")
session.add(planet1)
session.commit()
print("Planeta creado:", planet1.to_dict())

# 4. Añadir un vehículo
vehicle1 = Vehicle(name="X-Wing", vehicle_class="Starfighter", passenger=1, model="T-65B", max_speed=1050)
session.add(vehicle1)
session.commit()
print("Vehículo creado:", vehicle1.to_dict())

# 5. Añadir favoritos
fav_character = CharacterFavorit(user_id=user1.id, character_id=character1.id)
fav_planet = PlanetFavorit(user_id=user1.id, planet_id=planet1.id)
fav_vehicle = VehicleFavorit(user_id=user1.id, vehicle_id=vehicle1.id)
session.add_all([fav_character, fav_planet, fav_vehicle])
session.commit()
print(f"Favoritos de {user1.email} añadidos.")

# 6. Consultar datos
# Obtener todos los personajes
characters = session.query(Character).all()
print("Lista de personajes:")
for char in characters:
    print(char.to_dict())

# Obtener los favoritos de un usuario
user_favorites_characters = session.query(Character).join(CharacterFavorit).filter(CharacterFavorit.user_id == user1.id).all()
print(f"Personajes favoritos de {user1.email}:")
for fav_char in user_favorites_characters:
    print(fav_char.to_dict())

# Obtener planetas favoritos
user_favorites_planets = session.query(Planet).join(PlanetFavorit).filter(PlanetFavorit.user_id == user1.id).all()
print(f"Planetas favoritos de {user1.email}:")
for fav_planet in user_favorites_planets:
    print(fav_planet.to_dict())

# Obtener vehículos favoritos
user_favorites_vehicles = session.query(Vehicle).join(VehicleFavorit).filter(VehicleFavorit.user_id == user1.id).all()
print(f"Vehículos favoritos de {user1.email}:")
for fav_vehicle in user_favorites_vehicles:
    print(fav_vehicle.to_dict())

# --- LIMPIEZA ---
# Opcional: borrar datos después de las pruebas
session.close()
