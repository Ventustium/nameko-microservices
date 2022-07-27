CREATE DATABASE IF NOT EXISTS nameko_user;

USE nameko_user;

CREATE TABLE IF NOT EXISTS users
(
      id                INT AUTO_INCREMENT PRIMARY KEY,
      name              VARCHAR(255) NOT NULL,
      email_address     VARCHAR(255) NOT NULL,
      password          VARCHAR(255) NOT NULL,
      CONSTRAINT user_id_uindex
            UNIQUE (id),
      CONSTRAINT user_email_address_uindex
            UNIQUE (email_address)
);