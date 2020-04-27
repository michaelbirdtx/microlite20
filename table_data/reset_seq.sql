SELECT SETVAL('characters_armor_id_seq', (SELECT MAX(id) + 1 FROM characters_gear));
SELECT SETVAL('characters_class_id_seq', (SELECT MAX(id) + 1 FROM characters_class));
SELECT SETVAL('characters_clothing_id_seq', (SELECT MAX(id) + 1 FROM characters_clothing));
SELECT SETVAL('characters_gear_id_seq', (SELECT MAX(id) + 1 FROM characters_gear));
SELECT SETVAL('characters_race_id_seq', (SELECT MAX(id) + 1 FROM characters_race));
SELECT SETVAL('characters_weapon_id_seq', (SELECT MAX(id) + 1 FROM characters_weapon));