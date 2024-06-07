import pandas as pd

final_planet_list = []

for planet_data in planet_data_rows:
  temp_dict = {
      'name': planet_data[1],
      'distance_from_earth': planet_data[2],
      'planet_mass': planet_data[3],
      "planet_type": planet_data[6],
      "planet_radius": planet_data[7],
      "distance_from_thier_sun": planet_data[8],
      'orbital_period': planet_data[9],
      'gravity': planet_data[20],
      "orbital_speed": planet_data[21]
  }
  temp_dict['specifications'] = final_dict[planet_data[1]]
  final_planet_list.append(temp_dict)