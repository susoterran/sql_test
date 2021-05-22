create table tb_affiliation (
area_id INT,
school_id INT,
FOREIGN KEY (area_id) REFERENCES tb_area (id),
FOREIGN KEY (school_id) REFERENCES tb_school (id));