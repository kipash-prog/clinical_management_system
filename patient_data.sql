-- Active: 1703004728415@@127.0.0.1@3306
CREATE DATABASE clinic;

USE clinic;

CREATE TABLE clinical_management_system (
    roll_No INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(240),
    father_name VARCHAR(240),
    id_number VARCHAR(100) UNIQUE,
    phone_number VARCHAR(15),
    patient_case TEXT,
    date_created TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

select * from clinical_management_system;