INSERT INTO patient (medical_record_id, doctor_id, name, gender, phone, address, admission_date, discharge_date) 
VALUES 
(1, 1, "Ivanov Ivan Ivanovich", "male", "9111234567", "Moscow 1", "2020-01-01", "2020-01-01"),
(2, 1, "Astafyeva Ekaterina Sergeevna", "female", "+1111234567", "Moscow 2", "2020-01-01", "2020-01-01"),
(3, 1, "Popova Natalia Aleksandrovna", "female", "+2221234567", "Moscow 3", "2020-01-01", "2020-01-01"),
(4, 1, "Murt Sergey Leonidovich", "male", "+3331234567", "Moscow 4", "2020-01-01", "2020-01-01");

INSERT INTO medical_record (patient_id, diagnosis, prescription, treatment_plan)
VALUES
(1, "cold", "paracetamol", "rest"),
(2, "flu", "antibiotics", "rest"),
(3, "pneumonia", "antibiotics", "hospitalization"),
(4, "broken arm", "cast", "immobilization");