CREATE TABLE test_table (
    name VARCHAR(10),
    surname VARCHAR(50),
    city VARCHAR(50),
    age INT CHECK (age > 0 AND age <= 150)
);

INSERT INTO test_table (name, surname, city, age) VALUES
('John', 'Doe', 'New York', 25),
('Anna', 'Smith', 'London', 30),
('Tom', 'Brown', 'Paris', 22),
('Eva', 'White', 'Berlin', 28),
('Mark', 'Black', 'Madrid', 35),
('Lucy', 'Green', 'Rome', 19),
('Sam', 'Grey', 'Athens', 45),
('Sofia', 'Red', 'Moscow', 40),
('Mick', 'Blue', 'Beijing', 37),
('Lily', 'Pink', 'Tokyo', 32),
('Jack', 'Yellow', 'Los Angeles', 28),
('Emma', 'Purple', 'Toronto', 55),
('Ava', 'Orange', 'Sydney', 60),
('James', 'Silver', 'Seoul', 20),
('Oliver', 'Gold', 'Dubai', 27),
('Isla', 'Copper', 'Hong Kong', 30),
('Chloe', 'Bronze', 'Cape Town', 34),
('Zoe', 'Platinum', 'Cairo', 26),
('Mason', 'Emerald', 'Lagos', 29),
('Leo', 'Diamond', 'Rio de Janeiro', 22);
