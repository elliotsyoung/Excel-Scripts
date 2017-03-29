INSERT INTO labors VALUES 
(UNHEX(REPLACE(UUID(), '-', '')), 0, 'raw material splitting machine', '0.083', (0.99*100), 27.6, 1, NOW(), NOW(), (select id from proposals where user_id in (select id from users where email = 'dummy@maker.com')), (select id from users where email = 'dummy@supplier.com')),
(UNHEX(REPLACE(UUID(), '-', '')), 0, 'Rotary Die Cut', '14', (0.82*100), 45, 1, NOW(), NOW(), (select id from proposals where user_id in (select id from users where email = 'dummy@maker.com')), (select id from users where email = 'dummy@supplier.com')),
(UNHEX(REPLACE(UUID(), '-', '')), 0, 'Labor', '120', (0.94*100), 3.52, 1, NOW(), NOW(), (select id from proposals where user_id in (select id from users where email = 'dummy@maker.com')), (select id from users where email = 'dummy@supplier.com')),
(UNHEX(REPLACE(UUID(), '-', '')), 0, 'Labor', '15', (0.99*100), 3.52, 1, NOW(), NOW(), (select id from proposals where user_id in (select id from users where email = 'dummy@maker.com')), (select id from users where email = 'dummy@supplier.com')),
(UNHEX(REPLACE(UUID(), '-', '')), 0, 'cutting machine', '30', (0.995*100), 6, 1, NOW(), NOW(), (select id from proposals where user_id in (select id from users where email = 'dummy@maker.com')), (select id from users where email = 'dummy@supplier.com')),
(UNHEX(REPLACE(UUID(), '-', '')), 0, 'CNC center', '240', (0.95*100), 10, 1, NOW(), NOW(), (select id from proposals where user_id in (select id from users where email = 'dummy@maker.com')), (select id from users where email = 'dummy@supplier.com')),
(UNHEX(REPLACE(UUID(), '-', '')), 0, 'CNC lathe', '180', (0.98*100), 8, 1, NOW(), NOW(), (select id from proposals where user_id in (select id from users where email = 'dummy@maker.com')), (select id from users where email = 'dummy@supplier.com')),
(UNHEX(REPLACE(UUID(), '-', '')), 0, 'None', '30', (0.98*100), 10, 1, NOW(), NOW(), (select id from proposals where user_id in (select id from users where email = 'dummy@maker.com')), (select id from users where email = 'dummy@supplier.com')),
(UNHEX(REPLACE(UUID(), '-', '')), 0, 'sandblasting machine', '60', (0.98*100), 8, 1, NOW(), NOW(), (select id from proposals where user_id in (select id from users where email = 'dummy@maker.com')), (select id from users where email = 'dummy@supplier.com')),
(UNHEX(REPLACE(UUID(), '-', '')), 0, 'anodize line', '60', (0.95*100), 10, 1, NOW(), NOW(), (select id from proposals where user_id in (select id from users where email = 'dummy@maker.com')), (select id from users where email = 'dummy@supplier.com')),
(UNHEX(REPLACE(UUID(), '-', '')), 0, 'laser machine', '30', (0.995*100), 6, 1, NOW(), NOW(), (select id from proposals where user_id in (select id from users where email = 'dummy@maker.com')), (select id from users where email = 'dummy@supplier.com')),
(UNHEX(REPLACE(UUID(), '-', '')), 0, 'None', '30', (0.995*100), 6, 1, NOW(), NOW(), (select id from proposals where user_id in (select id from users where email = 'dummy@maker.com')), (select id from users where email = 'dummy@supplier.com')),
(UNHEX(REPLACE(UUID(), '-', '')), 0, 'None', '20', (1*100), 6, 1, NOW(), NOW(), (select id from proposals where user_id in (select id from users where email = 'dummy@maker.com')), (select id from users where email = 'dummy@supplier.com')),
(UNHEX(REPLACE(UUID(), '-', '')), 0, 'None', 'None', (1*100), 0, 1, NOW(), NOW(), (select id from proposals where user_id in (select id from users where email = 'dummy@maker.com')), (select id from users where email = 'dummy@supplier.com')),
(UNHEX(REPLACE(UUID(), '-', '')), 0, 'None', 'None', (1*100), 0, 1, NOW(), NOW(), (select id from proposals where user_id in (select id from users where email = 'dummy@maker.com')), (select id from users where email = 'dummy@supplier.com')),
(UNHEX(REPLACE(UUID(), '-', '')), 0, 'None', 'None', (1*100), 0, 1, NOW(), NOW(), (select id from proposals where user_id in (select id from users where email = 'dummy@maker.com')), (select id from users where email = 'dummy@supplier.com')),
(UNHEX(REPLACE(UUID(), '-', '')), 0, 'None', 'None', (1*100), 0, 1, NOW(), NOW(), (select id from proposals where user_id in (select id from users where email = 'dummy@maker.com')), (select id from users where email = 'dummy@supplier.com')),
(UNHEX(REPLACE(UUID(), '-', '')), 0, 'None', 'None', (1*100), 0, 1, NOW(), NOW(), (select id from proposals where user_id in (select id from users where email = 'dummy@maker.com')), (select id from users where email = 'dummy@supplier.com')),
(UNHEX(REPLACE(UUID(), '-', '')), 0, 'None', 'None', (0.98*100), 0, 1, NOW(), NOW(), (select id from proposals where user_id in (select id from users where email = 'dummy@maker.com')), (select id from users where email = 'dummy@supplier.com')),
(UNHEX(REPLACE(UUID(), '-', '')), 0, 'None', 'None', (1*100), 0, 1, NOW(), NOW(), (select id from proposals where user_id in (select id from users where email = 'dummy@maker.com')), (select id from users where email = 'dummy@supplier.com')),
(UNHEX(REPLACE(UUID(), '-', '')), 0, 'None', 'None', (1*100), 0, 1, NOW(), NOW(), (select id from proposals where user_id in (select id from users where email = 'dummy@maker.com')), (select id from users where email = 'dummy@supplier.com')),
(UNHEX(REPLACE(UUID(), '-', '')), 0, 'None', 'None', (1*100), 0, 1, NOW(), NOW(), (select id from proposals where user_id in (select id from users where email = 'dummy@maker.com')), (select id from users where email = 'dummy@supplier.com')),
(UNHEX(REPLACE(UUID(), '-', '')), 0, 'None', 'None', (0.98*100), 0, 1, NOW(), NOW(), (select id from proposals where user_id in (select id from users where email = 'dummy@maker.com')), (select id from users where email = 'dummy@supplier.com')),
(UNHEX(REPLACE(UUID(), '-', '')), 0, 'cutting machine', '30', (0.995*100), 6, 1, NOW(), NOW(), (select id from proposals where user_id in (select id from users where email = 'dummy@maker.com')), (select id from users where email = 'dummy@supplier.com')),
(UNHEX(REPLACE(UUID(), '-', '')), 0, 'CNC center', '240', (0.95*100), 10, 1, NOW(), NOW(), (select id from proposals where user_id in (select id from users where email = 'dummy@maker.com')), (select id from users where email = 'dummy@supplier.com')),
(UNHEX(REPLACE(UUID(), '-', '')), 0, 'CNC lathe', '180', (0.98*100), 8, 1, NOW(), NOW(), (select id from proposals where user_id in (select id from users where email = 'dummy@maker.com')), (select id from users where email = 'dummy@supplier.com')),
(UNHEX(REPLACE(UUID(), '-', '')), 0, 'None', '30', (0.98*100), 10, 1, NOW(), NOW(), (select id from proposals where user_id in (select id from users where email = 'dummy@maker.com')), (select id from users where email = 'dummy@supplier.com')),
(UNHEX(REPLACE(UUID(), '-', '')), 0, 'sandblasting machine', '60', (0.98*100), 8, 1, NOW(), NOW(), (select id from proposals where user_id in (select id from users where email = 'dummy@maker.com')), (select id from users where email = 'dummy@supplier.com')),
(UNHEX(REPLACE(UUID(), '-', '')), 0, 'anodize line', '60', (0.95*100), 10, 1, NOW(), NOW(), (select id from proposals where user_id in (select id from users where email = 'dummy@maker.com')), (select id from users where email = 'dummy@supplier.com')),
(UNHEX(REPLACE(UUID(), '-', '')), 0, 'laser machine', '30', (0.995*100), 6, 1, NOW(), NOW(), (select id from proposals where user_id in (select id from users where email = 'dummy@maker.com')), (select id from users where email = 'dummy@supplier.com')),
(UNHEX(REPLACE(UUID(), '-', '')), 0, 'None', '30', (0.995*100), 6, 1, NOW(), NOW(), (select id from proposals where user_id in (select id from users where email = 'dummy@maker.com')), (select id from users where email = 'dummy@supplier.com')),
(UNHEX(REPLACE(UUID(), '-', '')), 0, 'None', '20', (1*100), 6, 1, NOW(), NOW(), (select id from proposals where user_id in (select id from users where email = 'dummy@maker.com')), (select id from users where email = 'dummy@supplier.com')),
(UNHEX(REPLACE(UUID(), '-', '')), 0, 'cutting machine', '30', (0.995*100), 6, 1, NOW(), NOW(), (select id from proposals where user_id in (select id from users where email = 'dummy@maker.com')), (select id from users where email = 'dummy@supplier.com')),
(UNHEX(REPLACE(UUID(), '-', '')), 0, 'CNC center', '200', (0.98*100), 8, 1, NOW(), NOW(), (select id from proposals where user_id in (select id from users where email = 'dummy@maker.com')), (select id from users where email = 'dummy@supplier.com')),
(UNHEX(REPLACE(UUID(), '-', '')), 0, 'CNC lathe', '150', (0.99*100), 8, 1, NOW(), NOW(), (select id from proposals where user_id in (select id from users where email = 'dummy@maker.com')), (select id from users where email = 'dummy@supplier.com')),
(UNHEX(REPLACE(UUID(), '-', '')), 0, 'None', '30', (0.99*100), 8, 1, NOW(), NOW(), (select id from proposals where user_id in (select id from users where email = 'dummy@maker.com')), (select id from users where email = 'dummy@supplier.com')),
(UNHEX(REPLACE(UUID(), '-', '')), 0, 'sandblasting machine', '60', (0.99*100), 8, 1, NOW(), NOW(), (select id from proposals where user_id in (select id from users where email = 'dummy@maker.com')), (select id from users where email = 'dummy@supplier.com')),
(UNHEX(REPLACE(UUID(), '-', '')), 0, 'anodize line', '60', (0.98*100), 8, 1, NOW(), NOW(), (select id from proposals where user_id in (select id from users where email = 'dummy@maker.com')), (select id from users where email = 'dummy@supplier.com')),
(UNHEX(REPLACE(UUID(), '-', '')), 0, 'laser machine', '30', (0.995*100), 6, 1, NOW(), NOW(), (select id from proposals where user_id in (select id from users where email = 'dummy@maker.com')), (select id from users where email = 'dummy@supplier.com')),
(UNHEX(REPLACE(UUID(), '-', '')), 0, 'None', '30', (0.995*100), 6, 1, NOW(), NOW(), (select id from proposals where user_id in (select id from users where email = 'dummy@maker.com')), (select id from users where email = 'dummy@supplier.com')),
(UNHEX(REPLACE(UUID(), '-', '')), 0, 'None', '20', (1*100), 6, 1, NOW(), NOW(), (select id from proposals where user_id in (select id from users where email = 'dummy@maker.com')), (select id from users where email = 'dummy@supplier.com')),
(UNHEX(REPLACE(UUID(), '-', '')), 0, 'cutting machine', '30', (0.995*100), 5, 1, NOW(), NOW(), (select id from proposals where user_id in (select id from users where email = 'dummy@maker.com')), (select id from users where email = 'dummy@supplier.com')),
(UNHEX(REPLACE(UUID(), '-', '')), 0, 'CNC center', '100', (0.995*100), 7, 1, NOW(), NOW(), (select id from proposals where user_id in (select id from users where email = 'dummy@maker.com')), (select id from users where email = 'dummy@supplier.com')),
(UNHEX(REPLACE(UUID(), '-', '')), 0, 'CNC lathe', '100', (0.995*100), 7, 1, NOW(), NOW(), (select id from proposals where user_id in (select id from users where email = 'dummy@maker.com')), (select id from users where email = 'dummy@supplier.com')),
(UNHEX(REPLACE(UUID(), '-', '')), 0, 'None', '30', (0.995*100), 7, 1, NOW(), NOW(), (select id from proposals where user_id in (select id from users where email = 'dummy@maker.com')), (select id from users where email = 'dummy@supplier.com')),
(UNHEX(REPLACE(UUID(), '-', '')), 0, 'sandblasting machine', '45', (0.995*100), 7, 1, NOW(), NOW(), (select id from proposals where user_id in (select id from users where email = 'dummy@maker.com')), (select id from users where email = 'dummy@supplier.com')),
(UNHEX(REPLACE(UUID(), '-', '')), 0, 'anodize line', '45', (0.995*100), 7, 1, NOW(), NOW(), (select id from proposals where user_id in (select id from users where email = 'dummy@maker.com')), (select id from users where email = 'dummy@supplier.com')),
(UNHEX(REPLACE(UUID(), '-', '')), 0, 'laser machine', '20', (0.995*100), 4, 1, NOW(), NOW(), (select id from proposals where user_id in (select id from users where email = 'dummy@maker.com')), (select id from users where email = 'dummy@supplier.com')),
(UNHEX(REPLACE(UUID(), '-', '')), 0, 'None', '15', (1*100), 4, 1, NOW(), NOW(), (select id from proposals where user_id in (select id from users where email = 'dummy@maker.com')), (select id from users where email = 'dummy@supplier.com')),
(UNHEX(REPLACE(UUID(), '-', '')), 0, 'None', '15', (1*100), 5, 1, NOW(), NOW(), (select id from proposals where user_id in (select id from users where email = 'dummy@maker.com')), (select id from users where email = 'dummy@supplier.com')),
(UNHEX(REPLACE(UUID(), '-', '')), 0, '"KBA" RAPIDA105  Six color Press', '0.5', (0.98*100), 5.6, 1, NOW(), NOW(), (select id from proposals where user_id in (select id from users where email = 'dummy@maker.com')), (select id from users where email = 'dummy@supplier.com')),
(UNHEX(REPLACE(UUID(), '-', '')), 0, 'P.P.Lamination Machine', '2', (0.98*100), 3.8, 1, NOW(), NOW(), (select id from proposals where user_id in (select id from users where email = 'dummy@maker.com')), (select id from users where email = 'dummy@supplier.com')),
(UNHEX(REPLACE(UUID(), '-', '')), 0, 'Automatic Die-cutting Machine', '6', (0.97*100), 3.8, 1, NOW(), NOW(), (select id from proposals where user_id in (select id from users where email = 'dummy@maker.com')), (select id from users where email = 'dummy@supplier.com')),
(UNHEX(REPLACE(UUID(), '-', '')), 0, 'Semi-Automatic Box Gluing Machine', '20', (0.97*100), 3.12, 1, NOW(), NOW(), (select id from proposals where user_id in (select id from users where email = 'dummy@maker.com')), (select id from users where email = 'dummy@supplier.com')),
(UNHEX(REPLACE(UUID(), '-', '')), 0, '"KBA" RAPIDA105  Six color Press', '0.5', (0.98*100), 5.6, 1, NOW(), NOW(), (select id from proposals where user_id in (select id from users where email = 'dummy@maker.com')), (select id from users where email = 'dummy@supplier.com')),
(UNHEX(REPLACE(UUID(), '-', '')), 0, 'P.P.Lamination Machine', '2', (0.98*100), 3.8, 1, NOW(), NOW(), (select id from proposals where user_id in (select id from users where email = 'dummy@maker.com')), (select id from users where email = 'dummy@supplier.com')),
(UNHEX(REPLACE(UUID(), '-', '')), 0, 'Automatic Die-cutting Machine', '6', (0.97*100), 3.8, 1, NOW(), NOW(), (select id from proposals where user_id in (select id from users where email = 'dummy@maker.com')), (select id from users where email = 'dummy@supplier.com')),
(UNHEX(REPLACE(UUID(), '-', '')), 0, 'Semi-Automatic Box Gluing Machine', '20', (0.97*100), 3.12, 1, NOW(), NOW(), (select id from proposals where user_id in (select id from users where email = 'dummy@maker.com')), (select id from users where email = 'dummy@supplier.com')),
(UNHEX(REPLACE(UUID(), '-', '')), 0, 'None', 'None', (1*100), 0, 1, NOW(), NOW(), (select id from proposals where user_id in (select id from users where email = 'dummy@maker.com')), (select id from users where email = 'dummy@supplier.com')),
(UNHEX(REPLACE(UUID(), '-', '')), 0, 'None', 'None', (1*100), 0, 1, NOW(), NOW(), (select id from proposals where user_id in (select id from users where email = 'dummy@maker.com')), (select id from users where email = 'dummy@supplier.com')),
(UNHEX(REPLACE(UUID(), '-', '')), 0, 'None', 'None', (1*100), 0, 1, NOW(), NOW(), (select id from proposals where user_id in (select id from users where email = 'dummy@maker.com')), (select id from users where email = 'dummy@supplier.com')),
(UNHEX(REPLACE(UUID(), '-', '')), 0, 'None', 'None', (1*100), 0, 1, NOW(), NOW(), (select id from proposals where user_id in (select id from users where email = 'dummy@maker.com')), (select id from users where email = 'dummy@supplier.com')),
(UNHEX(REPLACE(UUID(), '-', '')), 0, 'None', 'None', (1*100), 0, 1, NOW(), NOW(), (select id from proposals where user_id in (select id from users where email = 'dummy@maker.com')), (select id from users where email = 'dummy@supplier.com')),
(UNHEX(REPLACE(UUID(), '-', '')), 0, 'None', 'None', (0.98*100), 0, 1, NOW(), NOW(), (select id from proposals where user_id in (select id from users where email = 'dummy@maker.com')), (select id from users where email = 'dummy@supplier.com')),
(UNHEX(REPLACE(UUID(), '-', '')), 0, 'None', 'None', (1*100), 0, 1, NOW(), NOW(), (select id from proposals where user_id in (select id from users where email = 'dummy@maker.com')), (select id from users where email = 'dummy@supplier.com')),
(UNHEX(REPLACE(UUID(), '-', '')), 0, 'None', 'None', (1*100), 0, 1, NOW(), NOW(), (select id from proposals where user_id in (select id from users where email = 'dummy@maker.com')), (select id from users where email = 'dummy@supplier.com')),
(UNHEX(REPLACE(UUID(), '-', '')), 0, 'None', 'None', (1*100), 0, 1, NOW(), NOW(), (select id from proposals where user_id in (select id from users where email = 'dummy@maker.com')), (select id from users where email = 'dummy@supplier.com')),
(UNHEX(REPLACE(UUID(), '-', '')), 0, 'None', 'None', (0.98*100), 0, 1, NOW(), NOW(), (select id from proposals where user_id in (select id from users where email = 'dummy@maker.com')), (select id from users where email = 'dummy@supplier.com')),
(UNHEX(REPLACE(UUID(), '-', '')), 0, 'Pulping machine', '5', (0.98*100), 2.5, 1, NOW(), NOW(), (select id from proposals where user_id in (select id from users where email = 'dummy@maker.com')), (select id from users where email = 'dummy@supplier.com')),
(UNHEX(REPLACE(UUID(), '-', '')), 0, 'Wet-press', '20', (0.98*100), 3.8, 1, NOW(), NOW(), (select id from proposals where user_id in (select id from users where email = 'dummy@maker.com')), (select id from users where email = 'dummy@supplier.com')),
(UNHEX(REPLACE(UUID(), '-', '')), 0, 'Die-cutting machine', '4', (0.98*100), 2.5, 1, NOW(), NOW(), (select id from proposals where user_id in (select id from users where email = 'dummy@maker.com')), (select id from users where email = 'dummy@supplier.com')),
(UNHEX(REPLACE(UUID(), '-', '')), 0, 'Printing press', '0.5', (0.98*100), 5.6, 1, NOW(), NOW(), (select id from proposals where user_id in (select id from users where email = 'dummy@maker.com')), (select id from users where email = 'dummy@supplier.com')),
(UNHEX(REPLACE(UUID(), '-', '')), 0, 'P.P.Lamination Machine', '2', (0.98*100), 3.8, 1, NOW(), NOW(), (select id from proposals where user_id in (select id from users where email = 'dummy@maker.com')), (select id from users where email = 'dummy@supplier.com')),
(UNHEX(REPLACE(UUID(), '-', '')), 0, 'Automatic die-cutting machine', '1', (0.98*100), 3.8, 1, NOW(), NOW(), (select id from proposals where user_id in (select id from users where email = 'dummy@maker.com')), (select id from users where email = 'dummy@supplier.com')),
(UNHEX(REPLACE(UUID(), '-', '')), 0, 'None', '6', (0.98*100), 46.9, 1, NOW(), NOW(), (select id from proposals where user_id in (select id from users where email = 'dummy@maker.com')), (select id from users where email = 'dummy@supplier.com')),
(UNHEX(REPLACE(UUID(), '-', '')), 0, 'Printing press', '0.1', (0.98*100), 5.6, 1, NOW(), NOW(), (select id from proposals where user_id in (select id from users where email = 'dummy@maker.com')), (select id from users where email = 'dummy@supplier.com')),
(UNHEX(REPLACE(UUID(), '-', '')), 0, 'Automatic die-cutting machine', '0.3', (1*100), 3.8, 1, NOW(), NOW(), (select id from proposals where user_id in (select id from users where email = 'dummy@maker.com')), (select id from users where email = 'dummy@supplier.com')),
(UNHEX(REPLACE(UUID(), '-', '')), 0, 'Pulping machine', '3', (0.98*100), 2.5, 1, NOW(), NOW(), (select id from proposals where user_id in (select id from users where email = 'dummy@maker.com')), (select id from users where email = 'dummy@supplier.com')),
(UNHEX(REPLACE(UUID(), '-', '')), 0, 'Wet-press', '20', (0.98*100), 3.8, 1, NOW(), NOW(), (select id from proposals where user_id in (select id from users where email = 'dummy@maker.com')), (select id from users where email = 'dummy@supplier.com')),
(UNHEX(REPLACE(UUID(), '-', '')), 0, 'Die-cutting machine', '4', (0.98*100), 2.5, 1, NOW(), NOW(), (select id from proposals where user_id in (select id from users where email = 'dummy@maker.com')), (select id from users where email = 'dummy@supplier.com')),
(UNHEX(REPLACE(UUID(), '-', '')), 0, 'Pulping machine', '2', (0.98*100), 2.5, 1, NOW(), NOW(), (select id from proposals where user_id in (select id from users where email = 'dummy@maker.com')), (select id from users where email = 'dummy@supplier.com')),
(UNHEX(REPLACE(UUID(), '-', '')), 0, 'Wet-press', '20', (0.98*100), 3.8, 1, NOW(), NOW(), (select id from proposals where user_id in (select id from users where email = 'dummy@maker.com')), (select id from users where email = 'dummy@supplier.com')),
(UNHEX(REPLACE(UUID(), '-', '')), 0, 'Die-cutting machine', '4', (0.98*100), 2.5, 1, NOW(), NOW(), (select id from proposals where user_id in (select id from users where email = 'dummy@maker.com')), (select id from users where email = 'dummy@supplier.com'));