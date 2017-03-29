INSERT INTO users (id, type,company,contact,email,password, picture, country, zip, created_at, updated_at) VALUES 
(UNHEX(REPLACE(UUID(), '-', '')),0, 'DummyMaker', 'DummyM', 'dummy@maker.com','$2a$10$kq9/Z90q2fX8rDN0vKfTNuEVpGoJYVJ/SUHLyFn4avW5g7v3D4zE6', null, 'USA', '10000', NOW(), NOW()),
(UNHEX(REPLACE(UUID(), '-', '')),1, 'DummySupplier', 'DummyS', 'dummy@supplier.com','$2a$10$kq9/Z90q2fX8rDN0vKfTNuEVpGoJYVJ/SUHLyFn4avW5g7v3D4zE6', null, 'USA', '10000', NOW(), NOW());


INSERT INTO proposals (id, status, product, quantity, completion, zip, audience, info, created_at, updated_at, user_id) 
VALUES (UNHEX(REPLACE(UUID(), '-', '')), 2, 'everything', 100, NOW()+100000000, '10000', 1,'dummyx23', NOW(), NOW(), (select id from users where email = 'dummy@maker.com' LIMIT 1));


INSERT INTO offers (status, first, follow, cavitation, days, life, sga, profit, overhead, tpp, total, completion, created_at, updated_at, proposal_id, user_id)
VALUES (2, 0, 0, 0, 1000, 1, 0,0,0,0,0, 1000, NOW(), NOW(), (select id from proposals where info = 'dummyx23' LIMIT 1), (select id from users where email = 'dummy@supplier.com' LIMIT 1));

select * from offers